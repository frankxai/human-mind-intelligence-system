#!/usr/bin/env python3
"""Self-curating precision-anchor filter.

The claim behind a foreign-language "precision anchor" is that it carries
meaning the English definition leaves implicit. This tool tests that claim
instead of taking it on faith, using a minimum-description-length proxy:

    An anchor earns its place only to the extent that its meaning cannot be
    cheaply reconstructed from what is already on the table.

A naive "is it novel vs the definition?" proxy fails on decorative terms: a term
glossed "careful, conscientious" shares few *stems* with a definition phrased
"takes care to do things properly", so pure novelty scores it high even though
it adds nothing. Semantic residual needs three factors, multiplied:

    resolutionScore = novelty(adds | definition+quality)   # says more than the English disposition
                    * elaboration(adds | gloss)            # explanation goes beyond restating the translation
                    * richness(adds)                       # clears an absolute floor of distinct content

A decorative anchor whose 'adds' just echoes its own gloss scores ~0 on
elaboration and is cut, regardless of surface novelty. A genuine kernel clears
all three and is kept.

``_novelty`` is the single pluggable primitive: it is the offline lexical
stand-in for embedding distance. Replace it with a cosine-distance
implementation when a model is available; the three-factor formula and the
threshold are the contract, not the lexical mechanics.

Usage:
    python3 tools/hma_filter.py                 # report only
    python3 tools/hma_filter.py --write         # write earned/resolutionScore back
    python3 tools/hma_filter.py --threshold 0.5 # override earn threshold (default 0.45)
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

LEXICON = Path(__file__).resolve().parent.parent / "models/human-atlas/qualities/core-qualities.en.json"
DEFAULT_THRESHOLD = 0.45

# Words that carry no distinguishing content — leaning on them is not resolution.
_STOP = {
    "a", "an", "and", "the", "of", "to", "in", "on", "at", "by", "for", "with",
    "as", "or", "not", "is", "are", "be", "that", "this", "it", "its", "than",
    "but", "into", "from", "how", "much", "one", "own", "more", "less", "very",
    "just", "merely", "only", "rather", "while", "which", "who", "whom", "what",
    "when", "where", "specific", "specifically", "sense", "thing", "things",
    "person", "people", "something", "someone", "them", "their", "others",
    "other", "english", "term", "word", "quality",
}


def _stems(text: str) -> set[str]:
    """Crude content-stem set: lowercase word tokens, stop words removed,
    trailing inflections trimmed so 'carried'/'carries'/'carry' collide."""
    stems: set[str] = set()
    for tok in re.findall(r"[a-zA-Z]+", text.lower()):
        if tok in _STOP or len(tok) < 3:
            continue
        for suffix in ("ing", "edly", "ed", "es", "ly", "s"):
            if tok.endswith(suffix) and len(tok) - len(suffix) >= 3:
                tok = tok[: -len(suffix)]
                break
        stems.add(tok)
    return stems


RICHNESS_FLOOR = 6  # distinct content stems a real kernel's explanation carries


def _novelty(text: str, reference: str) -> float:
    """Fraction of content stems in ``text`` absent from ``reference``, in
    [0,1]. The pluggable primitive: swap for embedding cosine distance and keep
    the signature identical."""
    stems = _stems(text)
    if not stems:
        return 0.0
    return len(stems - _stems(reference)) / len(stems)


def score_anchor(anchor: dict, entry: dict) -> float:
    adds = anchor.get("adds", "")
    gloss = anchor.get("gloss", "")
    definition = f"{entry.get('quality', '')} {entry.get('definition', '')}"
    novelty = _novelty(adds, definition)          # beyond the English disposition
    elaboration = _novelty(adds, gloss)           # beyond restating the translation
    richness = min(1.0, len(_stems(adds)) / RICHNESS_FLOOR)
    return round(novelty * elaboration * richness, 3)


def score_entry(entry: dict) -> list[dict]:
    return [
        {"anchor": anchor, "score": score_anchor(anchor, entry)}
        for anchor in entry.get("precisionAnchors", [])
    ]


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--write", action="store_true", help="write earned/resolutionScore back into the lexicon")
    ap.add_argument("--threshold", type=float, default=DEFAULT_THRESHOLD, help=f"earn threshold (default {DEFAULT_THRESHOLD})")
    args = ap.parse_args()

    data = json.loads(LEXICON.read_text())
    kept = cut = 0
    print(f"precision-anchor filter  (threshold {args.threshold}, MDL lexical proxy)\n")
    for entry in data["qualities"]:
        scored = score_entry(entry)
        if not scored:
            continue
        print(f"  {entry['quality']} ({entry['id']})")
        for s in scored:
            anchor = s["anchor"]
            earned = s["score"] >= args.threshold
            anchor["resolutionScore"] = s["score"]
            anchor["earned"] = earned
            mark = "keep" if earned else "CUT "
            kept += earned
            cut += not earned
            print(f"    [{mark}] {anchor['term']:<22} {s['score']:.3f}  {anchor['lang']}  {anchor['gloss']}")
        print()

    print(f"summary: {kept} earned, {cut} cut")
    if args.write:
        LEXICON.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
        print(f"wrote scores back to {LEXICON.name}")
    else:
        print("(dry run — pass --write to persist earned/resolutionScore)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
