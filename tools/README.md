# tools

Zero-dependency Python 3 toolkit for the Human Atlas layer. Standard library only
— nothing to install, runs offline.

| Tool | Does | Exit code |
|---|---|---|
| `hma_loader.py` | Validates every Atlas data file against the schemas; enforces confidence caps and the non-clinical denylist in code. The "one loader validates all." | non-zero on any violation |
| `hma_filter.py` | Scores each precision anchor's information residual (MDL proxy) and marks whether it earns its place. `--write` persists `earned`/`resolutionScore`. | 0 |
| `hma_eval.py` | Tests the quadrant's allergy prediction against labelled scenarios; reports accuracy and lift over a random baseline. | non-zero if it fails to beat baseline |
| `jsonschema_min.py` | Shared draft-2020-12 subset validator. Not a general engine — supports exactly the keywords these schemas use. | — |

```bash
# from the repo root
python3 tools/hma_loader.py
python3 tools/hma_filter.py            # dry run
python3 tools/hma_filter.py --write   # persist scores into the lexicon
python3 tools/hma_eval.py
```

`hma_loader.py` and `hma_eval.py` are runnable gates — wire them into CI to keep the
lexicon valid and the quadrant honest. `jsonschema_min._novelty` and
`hma_filter._novelty` are the documented swap points for a real embedding model;
keep their signatures and the three-factor formula intact.
