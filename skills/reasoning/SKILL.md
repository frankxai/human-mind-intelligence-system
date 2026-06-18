# Reasoning Skill

The Reasoning skill enables Hermes to identify the cognitive reasoning patterns present in an interaction and map them to the cognitive model layer primitives.

---

## Skill Metadata

```yaml
skill:
  id: reasoning
  version: "1.0.0"
  status: scaffolded  # implementation pending (TASK-005)
  model_layers:
    - cognitive
  confidence_output: true
  evidence_output: true
```

---

## Purpose

Different people reason differently. The Reasoning skill identifies *how* a person is thinking — not just *what* they are thinking — enabling Hermes to match explanation style, depth, and structure to the individual's cognitive approach.

---

## Inputs

| Input | Type | Required | Description |
|-------|------|----------|-------------|
| `interaction_log` | Array of turns | Yes | Current session interaction history |
| `cognitive_model` | Model primitives | Yes | From `models/cognitive/` |

---

## Outputs

| Output | Type | Schema |
|--------|------|--------|
| `dominant_style` | string | Enum from `models/cognitive/` |
| `secondary_style` | string | Enum from `models/cognitive/` |
| `attention_mode` | string | Enum from `models/cognitive/` |
| `cognitive_load_signal` | string | `low`, `moderate`, `high`, `unknown` |
| `reasoning_annotation` | string | Free-text note on observed reasoning pattern |
| `confidence` | float | 0.0–1.0 |
| `evidence` | array of strings | Turn-level references |

---

## Detection Heuristics (v1)

| Cognitive Style | Key Signals |
|-----------------|-------------|
| `analytical` | Numbered lists, "because/therefore" connectives, data requests |
| `intuitive` | Metaphors, "it feels like", rapid conclusions without justification |
| `narrative` | "Let me give you an example", personal stories, sequential storytelling |
| `abstract` | "In principle", "conceptually", theoretical framing, avoids specifics |
| `concrete` | "Specifically", "for example", action-oriented requests, avoids abstraction |

---

## Cognitive Load Detection

Markers that suggest elevated cognitive load:
- Response length decreasing over turns
- Increased clarification requests
- Fragmented sentence structure
- Topic repetition (asking the same question again)
