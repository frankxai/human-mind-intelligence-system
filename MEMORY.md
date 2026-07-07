# MEMORY

Durable state for the Human Mind Intelligence System. What this repo is, what it
promises, what it refuses, and what to record as it evolves.

## Version

**v0.1.0** — first engineered build. Twelve construct schemas, ontology,
response-prediction primitive, canon + doctrine.

The schema family version (`schemaVersion`, and the `const` in every schema) tracks
this: **0.1.0**.

### Human Atlas layer (added 2026-07-07)

A second operationalized model alongside human-mind: the **dispositional layer**
(core qualities + Ofman quadrants). Shares the schema family version and every
discipline. Canon lives upstream in `mind-intelligence-systems`; this repo
operationalizes it. Design: [`docs/human-atlas.md`](docs/human-atlas.md).

Added: `schemas/quality.schema.json`, `schemas/quality-observation.schema.json`,
`schemas/quadrant-hypothesis.schema.json`; the English-essential lexicon at
`models/human-atlas/qualities/core-qualities.en.json` (14 qualities); the quadrant
primitive doc; and a zero-dependency toolkit at `tools/` (loader, filter, eval,
shared subset validator).

Decisions recorded so they are not re-litigated:

- **English is essential, foreign terms are additional.** Every quality's English
  name + definition + quadrant is complete alone. `precisionAnchors` are optional
  overlays. This was a direct instruction: lean on English, add other languages
  only where they raise resolution.
- **Anchors must earn their place, measurably.** `tools/hma_filter.py` scores each
  anchor (novelty × elaboration × richness, an MDL proxy for embedding distance)
  and writes `earned`/`resolutionScore`. Decorative anchors stay flagged
  `earned: false`, not deleted — the verdict is recorded in-data. Seed data: 14
  earned, 2 decoys cut.
- **The quadrant is a hypothesis generator, not a personality type.** Routed
  through the response-prediction discipline. `tools/hma_eval.py` tests the allergy
  edge against labelled scenarios (seed: 0.78 accuracy, 2.33× over baseline).
- **The non-clinical guardrail is executable.** `tools/hma_loader.py` enforces the
  confidence caps and a clinical-vocabulary denylist in code, not just prose.
- **A quality is not a thirteenth cognitive construct.** It is dispositional and
  redefines none of the twelve.

## Commitments

These hold across every version. Breaking one is a regression, not a feature.

- **Non-clinical.** No diagnosis, no disorder names, no treatment advice — ever.
  Observe and predict responses; a human decides.
- **Schema-stable.** The twelve schemas share one shape so a single loader validates
  all of them. Shape changes bump the version everywhere at once and get recorded
  here.
- **Canon-aligned.** Terminology tracks the upstream
  [human-mind model](https://github.com/frankxai/mind-intelligence-systems). If this
  repo and the canon disagree, the canon wins.
- **Stages stay separate.** Observation, interpretation, hypothesis, evidence,
  decision are always labelled and never collapsed.

## What to record here

When you change the System, append to this file:

- Schema shape or version changes (and why).
- New or retired constructs (should only happen if the upstream canon changes).
- Changes to the ontology edge set or relationship types.
- Changes to the response-prediction primitive's rules.
- Any decision that future sessions need to not re-litigate.

## What this is NOT (anti-scope)

- **Not a diagnostic or clinical tool.** It does not assess, screen, or treat.
- **Not a lived OS.** Daily personal operation lives in
  [agentic-mind-os](https://github.com/frankxai/agentic-mind-os) and
  [starlight-mind-os-pro](https://github.com/frankxai/starlight-mind-os-pro).
- **Not the canon.** The model itself lives upstream in
  [mind-intelligence-systems](https://github.com/frankxai/mind-intelligence-systems).
  This repo operationalizes it; it does not own it.
- **Not a memory-palace store.** Blessed work-as-data lives in
  [frankx-mind-palace](https://github.com/frankxai/frankx-mind-palace) and
  [mind-palace-agent-skills](https://github.com/frankxai/mind-palace-agent-skills).
- **Not a personality engine or persuasion system.** It predicts likely responses
  under stated conditions; it does not profile, score, or manipulate people.

## Composes from

- **SIP** — [Starlight Intelligence Protocol](https://github.com/frankxai/Starlight-Intelligence-System).
  Attestation + sovereignty.
- **mind-intelligence-systems** — the human-mind canon. Source of truth for the
  twelve constructs.

Built on SIP.
