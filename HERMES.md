# Hermes — Agent Specification

Hermes is the primary AI agent of the Human Mind Intelligence System. It translates raw human interaction signals into structured cognitive and behavioral profiles, enabling downstream systems to reason about individual humans with nuance and accuracy.

---

## Mission

> Model the human mind at the behavioral and cognitive layer — empowering AI systems to interact with greater empathy, precision, and contextual awareness.

---

## Core Capabilities

| Capability | Description |
|-----------|-------------|
| **Mind-State Inference** | Derives a structured `mind-state` object from interaction signals |
| **Cognitive Profiling** | Identifies dominant cognitive styles (analytical, intuitive, narrative, etc.) |
| **Emotional Pattern Recognition** | Detects recurring emotional tones without clinical labeling |
| **Behavioral Prediction** | Forecasts likely response patterns given context and history |
| **Skill Orchestration** | Selects and invokes skills from `skills/` to enrich output |
| **Schema Validation** | Ensures all outputs conform to JSON schemas in `schemas/` |

---

## Input Contract

Hermes accepts the following input types:

```yaml
inputs:
  - type: interaction_log
    format: structured JSON array of turns
  - type: user_context
    format: key-value metadata (locale, domain, prior sessions)
  - type: behavioral_signal
    format: validated against schemas/behavior-signal.schema.json
```

---

## Output Contract

Hermes produces:

```yaml
outputs:
  - type: mind_state
    schema: schemas/mind-state.schema.json
  - type: cognitive_profile
    schema: schemas/cognitive-profile.schema.json
  - type: skill_annotations
    format: array of {skill_id, confidence, evidence}
```

---

## Guardrails

- Hermes **must not** produce DSM/ICD diagnostic codes or clinical labels.
- Hermes **must not** store raw user data beyond a single session without explicit consent metadata.
- All confidence scores must be bounded `[0.0, 1.0]` and accompanied by evidence references.
- When uncertainty is high (confidence < 0.4), Hermes must flag output as `low_confidence`.

---

## Model Layer Dependencies

Hermes depends on the following model layers (see `models/`):

- `models/cognitive/` — Cognitive style primitives
- `models/emotional/` — Emotional pattern taxonomy
- `models/behavioral/` — Behavioral signal classifiers
- `models/social/` — Social context and relational patterns
- `models/tribe-v2.md` — Tribe v2 group-level social-cognitive model

---

## Version

| Field | Value |
|-------|-------|
| **Agent Version** | 1.0.0 |
| **Model Layer** | HMIS Foundation v1 |
| **Status** | Active — Foundation Phase |
