# CANON

This System composes two upstream canons and declares no vertical canon of its own.

## Composes

- **SIP** — the [Starlight Intelligence Protocol](https://github.com/frankxai/Starlight-Intelligence-System).
  This System inherits SIP's attestation and sovereignty discipline. Generated
  artifacts carry the "Built on SIP" attestation.
- **mind-intelligence-systems canon** — the
  [human-mind model](https://github.com/frankxai/mind-intelligence-systems/tree/main/models/human-mind).
  The twelve cognitive modules, their Definitions, Key Processes, Related
  Constructs, and Research Notes are the source of truth. This System does not
  redefine them; it operationalizes them into schemas, ontology, and the
  response-prediction primitive.

## Declines

This System declines to author its own vertical canon. It introduces no new
constructs, no new module taxonomy, and no competing definitions. If a term here
disagrees with the upstream canon, the upstream canon wins and this repo is the bug.

## Key terms (operational, not redefinitions)

These define how upstream canon is *used* here. They are engineering terms, not new
psychology.

- **Construct** — one of the twelve canonical modules (attention, memory, emotion,
  motivation, identity, learning, belief, behavior, consciousness, metacognition,
  decision-making, social-cognition). Defined upstream; named here.
- **Observation** — a recorded, plain-language description of something that
  happened, attached to one construct. No inference. The `observation` field.
- **Indicator** — a discrete, observable marker drawn from a construct's canon Key
  Processes. A thing you can point at. The `indicators` field.
- **Interpretation** — a labelled, falsifiable hypothesis about what an observation
  might mean. Strictly separate from the observation. The `interpretation` object.
- **Prediction** — a conditional, probabilistic hypothesis about a likely response,
  derived from observations and ontology edges. Never a diagnosis. See
  [`docs/response-prediction.md`](docs/response-prediction.md).
- **Provenance** — where an observation came from and how much the source is
  trusted. The `provenance` field.

## Non-clinical clause

This System is non-clinical by construction. It models, hypothesizes, and predicts
responses. It does not diagnose, does not name disorders, and does not recommend
treatment. Observation, interpretation, hypothesis, evidence, and decision stay
labelled and separate (see [`CLAUDE.md`](CLAUDE.md)). This clause is non-waivable.

## Sovereignty

Per SIP § Sovereignty clause, the operator owns their data and the decisions made
from it. This System surfaces structured observations and labelled hypotheses; the
operator decides what they mean and what to do.

Built on SIP.
