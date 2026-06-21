# MEMORY

Durable state for the Human Mind Intelligence System. What this repo is, what it
promises, what it refuses, and what to record as it evolves.

## Version

**v0.1.0** — first engineered build. Twelve construct schemas, ontology,
response-prediction primitive, canon + doctrine.

The schema family version (`schemaVersion`, and the `const` in every schema) tracks
this: **0.1.0**.

### Additive since v0.1.0 (no schema change)

A visual + research layer was added around the schemas without touching their shape
or the observation/interpretation contract:

- `ontology/edges.json` — machine-readable companion to `ontology.md` (the 28 edges).
- `docs/research/` — research grounding (`research.json` source + `frontier-map.md`
  synthesis + `constructs/*.md`). Frames the System as a non-clinical prediction
  primitive, mapped to world-foundation-model + predictive-brain research. The
  non-clinical boundary is restated and held: grounds the models, never profiles a
  person.
- `docs/explorer/` — a self-contained, zero-build interactive explorer
  (`index.html` + generated `explorer-data.js`).
- `scripts/build-explorer.mjs` — zero-dependency generator (schemas + edges +
  research → explorer data); `--check` flags drift.

The schemas remain the single source of truth; this layer is read-only over them.

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
