# Human Atlas — the dispositional layer

The Human Atlas operationalizes a second upstream model alongside the human-mind
model: **core qualities** — dispositions like decisiveness, tact, or composure —
and the relations between them. Where the twelve cognitive constructs model *how a
mind works*, the Atlas models *how a person characteristically leans*.

It is built to the same discipline as the rest of this System: observation and
interpretation stay separate, confidence in a reading never exceeds confidence in
what was observed, and nothing here diagnoses. A quality is a disposition to
describe, never a label to assign.

> The canon for the Atlas model lives upstream in
> [mind-intelligence-systems](https://github.com/frankxai/mind-intelligence-systems).
> This repo operationalizes it into schemas, a lexicon, and tools; it does not own
> the model. If this repo and the canon disagree, the canon wins.

## Two design rules

### 1. English is essential; foreign terms are additional

English carries the model. Every quality has an English name, an English
definition, and an English quadrant that is complete on its own. Reach comes from
English — anyone can read the lexicon and use it without a second language.

Some languages lexicalize a distinction English can only approximate with a phrase:
`Fingerspitzengefühl` (a near-tactile feel for the right touch), `Augenmaß` (a sense
of the right measure judged by eye), `Haltung` (a moral posture held under
pressure), `気配り`/kikubari (anticipatory care for others' unspoken needs). These
are **precision anchors** — optional overlays that raise resolution where English
blurs. They are never required, and no consumer of the lexicon needs to speak the
language to use the English layer.

The failure mode this guards against is aesthetic inflation: piling on foreign
words that look precise but only restate the English one. So the second rule.

### 2. An anchor must earn its place — measurably

A precision anchor is a *claim*: "this term carries meaning the English definition
leaves implicit." The System tests the claim instead of taking it on faith.

[`tools/hma_filter.py`](../tools/hma_filter.py) scores each anchor's information
residual with a minimum-description-length proxy — three factors, multiplied:

- **novelty** — does the term's explanation add content the English definition and
  name lack?
- **elaboration** — does the explanation go beyond restating the term's own
  translation? (A decorative anchor fails here: its `adds` just echoes its `gloss`.)
- **richness** — does the explanation clear an absolute floor of distinct content?

An anchor below threshold is marked `earned: false` and stays flagged in the data
as a recorded verdict, not silently kept. On the seed lexicon this cuts the two
planted decoys (`sorgfältig` → 0.000, `flexibel` → 0.083) and keeps fourteen
genuine kernels (0.69–1.00). The lexical scorer is a documented proxy for embedding
distance; swap `_novelty` for a cosine-distance implementation and the same
three-factor contract holds.

This is the balance the Atlas is built for: the human-science content (qualities,
quadrants, cross-lingual nuance) is only allowed in once a computational test says
it earns its keep.

## The quadrant primitive

The relation between qualities is the [Ofman core-quality
quadrant](quadrant.md): a quality overextended becomes a **pitfall**; the pitfall's
positive opposite is the **challenge**; the challenge overextended in someone else
is the **allergy** — what the person tends to find hardest to tolerate.

The Atlas treats the quadrant as a **hypothesis generator, not a personality type**.
Given an observed quality it predicts a likely pitfall, challenge, and allergy —
each conditional, probabilistic, and falsifiable, routed through the same
[response-prediction](response-prediction.md) discipline as everything else.

That prediction is checkable, so it is checked.
[`tools/hma_eval.py`](../tools/hma_eval.py) tests one edge — "a person is most
irritated by their allergy" — against labelled scenarios and reports accuracy
against a random baseline. On the seed scenarios the quadrant scores 0.78 (7/9),
a 2.33× lift over chance, with two honest misses. A quality model that cannot beat
chance on its own eval is signalling that it is decorative for that data. That is
what the eval is for.

## What makes this a system, not a lexicon

| Concern | Where it lives |
|---|---|
| The qualities and quadrants (data) | [`models/human-atlas/qualities/core-qualities.en.json`](../models/human-atlas/qualities/core-qualities.en.json) |
| Typed contracts | [`schemas/quality*.schema.json`](../schemas), [`schemas/quadrant-hypothesis.schema.json`](../schemas/quadrant-hypothesis.schema.json) |
| One loader, all validation + guardrails | [`tools/hma_loader.py`](../tools/hma_loader.py) |
| Self-curation (anchors earn their place) | [`tools/hma_filter.py`](../tools/hma_filter.py) |
| Falsifiable eval | [`tools/hma_eval.py`](../tools/hma_eval.py) |

The loader makes the non-clinical guardrail **executable**: it scans every data
file against a clinical-vocabulary denylist and enforces the confidence caps in
code, not just in prose. A lexicon asserts; a system validates, scores, and can be
run.

## Running it

```bash
python3 tools/hma_loader.py           # validate all data + enforce guardrails
python3 tools/hma_filter.py           # score precision anchors (dry run)
python3 tools/hma_filter.py --write   # persist earned / resolutionScore
python3 tools/hma_eval.py             # score the quadrant against baseline
```

Zero dependencies — Python 3 standard library only.

## Boundaries

- **Not the twelve constructs.** A quality is dispositional; it is not a thirteenth
  cognitive module and does not redefine any of the twelve.
- **Not a personality engine.** The quadrant predicts likely reactions under stated
  conditions; it does not type, score, or rank people.
- **Not clinical.** No diagnosis, no disorder names, ever. Enforced by the loader.

Built on SIP.
