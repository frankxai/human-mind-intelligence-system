#!/usr/bin/env python3
"""The one loader. Validates every Human Atlas data file against the schemas
and enforces the disciplines the schema alone cannot express:

  1. Structural validity  — each instance validates against its schema.
  2. Confidence caps       — an interpretation/prediction is never more
                             confident than the observation it rests on.
  3. Non-clinical guardrail — no clinical label leaks into the data. The
                             prime directive, made executable.

Negative fixtures (``*.invalid.json``) are expected to FAIL structural
validation; the loader reports them as passing tests when they do.

Exit code 0 = everything holds. Non-zero = a discipline was violated.

Usage:  python3 tools/hma_loader.py
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from jsonschema_min import validate  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
SCHEMAS = ROOT / "schemas"
LEXICON = ROOT / "models/human-atlas/qualities/core-qualities.en.json"
FIXTURES = ROOT / "tests/fixtures"

# Clinical vocabulary that must never appear in Atlas data. Word-boundary
# matched, case-insensitive. The guardrail from CANON.md, enforced in code.
CLINICAL_DENYLIST = [
    "diagnosis", "diagnose", "disorder", "symptom of", "pathology",
    "pathological", "clinical", "psychiatric", "depression", "bipolar",
    "adhd", "ptsd", "narcissist", "sociopath", "psychopath", "syndrome",
    "treatment", "therapy", "medication", "prognosis", "comorbid",
]


def _schema_for(obj) -> str:
    if not isinstance(obj, dict):
        return ""
    if "predictions" in obj and "from" in obj:
        return "quadrant-hypothesis"
    if obj.get("construct") == "quality" and "observation" in obj:
        return "quality-observation"
    if "quadrant" in obj and "quality" in obj:
        return "quality"
    return ""


def _clinical_hits(obj, path="$") -> list[str]:
    hits = []
    if isinstance(obj, str):
        for term in CLINICAL_DENYLIST:
            if re.search(r"\b" + re.escape(term) + r"\b", obj, re.IGNORECASE):
                hits.append(f"{path}: clinical term '{term}' in {obj!r}")
    elif isinstance(obj, dict):
        for k, v in obj.items():
            hits.extend(_clinical_hits(v, f"{path}.{k}"))
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            hits.extend(_clinical_hits(v, f"{path}[{i}]"))
    return hits


def _confidence_caps(obj: dict, kind: str) -> list[str]:
    errs = []
    if kind == "quality-observation":
        interp = obj.get("interpretation")
        if isinstance(interp, dict) and "confidence" in interp and "confidence" in obj:
            if interp["confidence"] > obj["confidence"]:
                errs.append(
                    f"interpretation confidence {interp['confidence']} exceeds "
                    f"observation confidence {obj['confidence']}"
                )
    if kind == "quadrant-hypothesis":
        confidences = [f["confidence"] for f in obj.get("from", []) if isinstance(f, dict) and "confidence" in f]
        cap = min(confidences, default=1.0)
        for i, pred in enumerate(obj.get("predictions", [])):
            if isinstance(pred, dict) and "confidence" in pred and pred["confidence"] > cap:
                errs.append(
                    f"predictions[{i}] confidence {pred['confidence']} exceeds "
                    f"source-observation cap {cap}"
                )
    return errs


def main() -> int:
    schemas = {p.stem.replace(".schema", ""): json.loads(p.read_text()) for p in SCHEMAS.glob("*.schema.json")}
    failures = 0
    checked = 0

    # 1. The lexicon: validate every entry against quality.schema.json.
    lex = json.loads(LEXICON.read_text())
    qualities = lex.get("qualities", []) if isinstance(lex, dict) else []
    for entry in qualities:
        checked += 1
        entry_id = entry.get("id", "unknown") if isinstance(entry, dict) else "<non-object>"
        errs = validate(entry, schemas["quality"], f"quality:{entry_id}")
        errs += _clinical_hits(entry, f"quality:{entry_id}")
        if errs:
            failures += 1
            print(f"FAIL  lexicon '{entry_id}'")
            for e in errs:
                print(f"      {e}")
    print(f"lexicon: {len(qualities)} entries checked")

    # 2. Fixtures: positive validate, negative expected-to-fail.
    for fx in sorted(FIXTURES.glob("*.json")):
        if fx.name == "eval-scenarios.json":
            continue
        obj = json.loads(fx.read_text())
        kind = _schema_for(obj)
        if not kind:
            print(f"WARN  {fx.name}: no schema matched, skipped")
            continue
        checked += 1
        errs = validate(obj, schemas[kind], fx.name) + _confidence_caps(obj, kind) + _clinical_hits(obj, fx.name)
        negative = fx.name.endswith(".invalid.json")
        if negative:
            if errs:
                print(f"ok    {fx.name}: correctly rejected ({len(errs)} error(s))")
            else:
                failures += 1
                print(f"FAIL  {fx.name}: expected rejection but validated clean")
        else:
            if errs:
                failures += 1
                print(f"FAIL  {fx.name}")
                for e in errs:
                    print(f"      {e}")
            else:
                print(f"ok    {fx.name} ({kind})")

    print(f"\n{checked} document(s) checked, {failures} failure(s)")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
