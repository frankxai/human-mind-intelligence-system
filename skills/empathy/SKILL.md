# Empathy Skill

The Empathy skill enables Hermes to detect the emotional register of an interaction and surface signals that inform how responses should be adapted for maximum resonance with the individual.

---

## Skill Metadata

```yaml
skill:
  id: empathy
  version: "1.0.0"
  status: scaffolded  # implementation pending (TASK-004)
  model_layers:
    - emotional
    - social
  confidence_output: true
  evidence_output: true
```

---

## Purpose

Empathy in HMIS is not about simulating human feelings — it is about **accurately reading emotional signals** and using them to calibrate communication style. The skill answers the question: *"What emotional state is this person most likely in, and how should that shape the response?"*

---

## Inputs

| Input | Type | Required | Description |
|-------|------|----------|-------------|
| `interaction_log` | Array of turns | Yes | The current session's interaction history |
| `emotional_model` | Model primitives | Yes | From `models/emotional/` |
| `social_context` | Social primitives | No | From `models/social/` |

---

## Outputs

| Output | Type | Schema |
|--------|------|--------|
| `emotional_pattern` | string | Enum from `models/emotional/` |
| `tone_tendency` | object | See `models/emotional/README.md` |
| `empathy_signal` | object | `{register: string, adaptation_hint: string}` |
| `confidence` | float | 0.0–1.0 |
| `evidence` | array of strings | Turn-level references |

---

## Adaptation Hints

The skill produces `adaptation_hint` to guide Hermes response generation:

| Emotional Pattern | Adaptation Hint |
|-------------------|----------------|
| `frustrated` | Acknowledge the friction before providing solutions |
| `withdrawn` | Use shorter, lower-pressure turns |
| `curious` | Provide rich detail and open-ended invitations |
| `guarded` | Avoid probing questions; build trust gradually |
| `confident` | Match assertive register; be direct |
| `uncertain` | Provide scaffolding and structured guidance |

---

## Guardrail

This skill must not produce outputs suggesting the user has a mental health condition. `frustrated` ≠ anxiety disorder. `withdrawn` ≠ depression. These are interaction style signals only.
