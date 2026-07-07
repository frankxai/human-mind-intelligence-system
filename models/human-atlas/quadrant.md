# The core-quality quadrant

The Atlas's structural primitive is Daniel Ofman's core-quality quadrant
(*kernkwadrant*). It relates four dispositions around a single core quality:

```
        core quality  ───(too much)──▶   pitfall
             │                              │
     (positive opposite)            (positive opposite)
             │                              │
        challenge     ◀──(too much)───    allergy
```

- **Core quality** — a strength a person naturally operates from (e.g. decisiveness).
- **Pitfall** — the core quality overextended; too much of a good thing (pushiness).
- **Challenge** — the balancing positive opposite of the pitfall (patience).
- **Allergy** — the challenge overextended, usually in *someone else*; what the
  person finds hardest to tolerate (passivity).

The diagonal is the tell: a person tends to be most irritated by their **allergy**,
which is the far corner from their core quality. Decisive people bristle at
passivity; tactful people bristle at bluntness.

## How the Atlas uses it

As a **hypothesis generator, not a personality type.** Given an observed core
quality, the quadrant proposes a likely pitfall, challenge, and allergy. Each is:

- **conditional** — "given decisiveness observed, *if* the pattern holds, *then*
  passivity is the likely allergy";
- **probabilistic** — carries a confidence in `[0,1]`, capped by the confidence in
  the source observation;
- **falsifiable** — phrased so a later observation can disconfirm it;
- **plural** — the pitfall reading and the allergy reading are competing
  hypotheses, not a verdict.

This routes through the same [five-stage discipline](../../docs/response-prediction.md)
as every other prediction in the System. The quadrant never becomes a label stuck
to a person; it is a lens that generates checkable guesses.

Schema: [`schemas/quadrant-hypothesis.schema.json`](../../schemas/quadrant-hypothesis.schema.json).
Eval: [`tools/hma_eval.py`](../../tools/hma_eval.py) tests the allergy edge against
labelled scenarios.

## What it is not

- Not a typology. It does not sort people into fixed categories.
- Not a diagnosis. Pitfalls and allergies are dispositions, never conditions.
- Not deterministic. The quadrant predicts a *tendency*, disconfirmable by the next
  observation.

Built on SIP.
