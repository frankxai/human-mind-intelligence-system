#!/usr/bin/env python3
"""Falsifiable eval for the quadrant primitive.

The Ofman quadrant makes a checkable prediction: a person operating from a core
quality tends to be most irritated by that quality's *allergy* (the balancing
challenge overextended in someone else). This harness tests that prediction
against labelled scenarios and reports whether it beats a random baseline.

  model prediction = lexicon[subject core quality].quadrant.allergy
  baseline         = random guess among the candidate irritants
  metric           = accuracy, and lift over baseline

A model that cannot beat chance here is signalling that the quadrant is
decorative for this data — which is exactly what an eval is for. Exit code is
non-zero when the model fails to beat baseline, so this doubles as a regression
gate.

Usage:  python3 tools/hma_eval.py
"""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LEXICON = ROOT / "models/human-atlas/qualities/core-qualities.en.json"
SCENARIOS = ROOT / "tests/fixtures/eval-scenarios.json"


def main() -> int:
    lex = {q["id"]: q for q in json.loads(LEXICON.read_text())["qualities"]}
    scenarios = json.loads(SCENARIOS.read_text())["scenarios"]

    hits = 0
    baseline_sum = 0.0
    scored = 0
    print("quadrant eval — does the allergy prediction beat chance?\n")
    for sc in scenarios:
        quality_id = sc.get("subjectCoreQuality")
        if quality_id not in lex:
            print(f"  [skip] {str(quality_id):<13} (not in lexicon)")
            continue
        predicted = lex[quality_id].get("quadrant", {}).get("allergy", "").lower()
        actual = str(sc.get("observedStrongestIrritation", "")).lower()
        candidates = [c.lower() for c in sc.get("candidateIrritants", [])]
        hit = bool(predicted) and predicted == actual
        hits += hit
        scored += 1
        baseline_sum += 1.0 / len(candidates) if candidates else 0.0  # expected accuracy of a random pick
        mark = "hit " if hit else "miss"
        print(f"  [{mark}] {quality_id:<13} predict={predicted:<14} actual={actual}")

    n = scored
    model_acc = hits / n if n else 0.0
    baseline_acc = baseline_sum / n if n else 0.0
    lift = model_acc / baseline_acc if baseline_acc else float("inf")
    print(f"\nscenarios      : {n}")
    print(f"model accuracy : {model_acc:.3f}  ({hits}/{n})")
    print(f"random baseline: {baseline_acc:.3f}")
    print(f"lift           : {lift:.2f}x")
    beats = model_acc > baseline_acc
    print(f"verdict        : {'quadrant beats chance' if beats else 'NO SIGNAL — quadrant is decorative here'}")
    return 0 if beats else 1


if __name__ == "__main__":
    raise SystemExit(main())
