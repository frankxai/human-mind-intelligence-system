# Research grounding

This layer answers one question: **what is the best current research that grounds each construct model in this System** — from frontier AI labs and from cognitive science — and why it is relevant here.

It exists because the System is, at its core, a **prediction primitive**: it observes cognitive signals and predicts likely responses with confidence. That is not a loose metaphor. It is the human-mind analog of the paradigm frontier labs are building toward in machines — **world models** and **predictive processing** — where intelligence is framed as predicting the next state of a system in a learned latent space. The same frame runs through cognitive science as the predictive (Bayesian) brain, and through affective computing as the line on **predicting emotional response to viewed content**. We borrow the framing; we refuse the autonomy. The human owns every decision.

## Non-clinical boundary (non-waivable)

The research below — including the affective-computing work on emotion and the theory-of-mind work on models — grounds the **construct models**. It is cited to ground the model, **not** to profile, score, surveil, or diagnose any person. Per [`../../CANON.md`](../../CANON.md) this boundary does not bend. The emotion anchors model emotion *elicited by content/media*; nothing here licenses emotion-detection-on-people or any clinical reading.

## What's here

| File | What it is |
|---|---|
| [`research.json`](research.json) | The structured source of truth — frontier anchors + per-construct grounding. The visual explorer reads this. |
| [`frontier-map.md`](frontier-map.md) | The synthesis: the prediction frame, world foundation models, the predictive brain, emotion-from-content, theory of mind in models — and what we borrow vs. refuse. |
| [`constructs/`](constructs) | One short prose file per construct, mapping it to its anchors and lenses. |
| [`../explorer/index.html`](../explorer/index.html) | The interactive explorer that surfaces all of the above inline, per construct. |

## Keeping it in sync

The explorer's data is generated from the schemas, the ontology edges, and `research.json`:

```bash
node scripts/build-explorer.mjs          # regenerate docs/explorer/explorer-data.js
node scripts/build-explorer.mjs --check  # fail if stale (CI-friendly)
```

The schemas remain the single source of truth for construct shape; this layer adds grounding around them and changes nothing about the observation/interpretation contract.

Built on SIP.
