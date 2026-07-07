# models/human-atlas

The dispositional layer of the Human Mind Intelligence System: **core qualities**
and the quadrant relations between them. English-canonical, foreign precision
anchors optional and filter-gated, non-clinical by construction.

Design and rationale: [`../../docs/human-atlas.md`](../../docs/human-atlas.md).

## Contents

| Path | What |
|---|---|
| `qualities/core-qualities.en.json` | The English-essential lexicon (14 qualities, quadrants, earned anchors) |
| `quadrant.md` | The Ofman core-quality quadrant primitive |

## Layout of a quality entry

```jsonc
{
  "id": "tactful",                       // stable lowercase key
  "quality": "Tactful",                  // ESSENTIAL — English name
  "definition": "Handles delicate situations and people without causing offence.",
  "indicators": ["reads the room", "times hard messages well"],
  "quadrant": {                          // hypothesis structure, not a type
    "coreQuality": "Tact",
    "pitfall": "Evasiveness",            // tact overextended
    "challenge": "Directness",           // balancing opposite
    "allergy": "Bluntness"               // what a tactful person can least tolerate
  },
  "precisionAnchors": [                   // OPTIONAL — additional, must earn place
    {
      "lang": "de",
      "term": "Fingerspitzengefühl",
      "gloss": "fingertip feeling",
      "adds": "an embodied, near-tactile sense for the exact right touch ...",
      "resolutionScore": 0.852,          // written by tools/hma_filter.py
      "earned": true                     // written by tools/hma_filter.py
    }
  ]
}
```

The English fields are required and complete on their own. `precisionAnchors` is
optional; `earned` / `resolutionScore` are written by
[`../../tools/hma_filter.py`](../../tools/hma_filter.py), never by hand.

## Validate

```bash
python3 tools/hma_loader.py   # from repo root
```

Built on SIP.
