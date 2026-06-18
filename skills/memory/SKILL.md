# Memory Skill

The Memory skill enables Hermes to extract, reference, and leverage relevant prior context from within the current session to produce more coherent and personalized outputs.

---

## Skill Metadata

```yaml
skill:
  id: memory
  version: "1.0.0"
  status: scaffolded  # implementation pending (TASK-006)
  model_layers:
    - cognitive
    - behavioral
  confidence_output: true
  evidence_output: true
```

---

## Purpose

Within a session, humans build context incrementally. The Memory skill ensures Hermes does not treat each turn in isolation — it surfaces salient prior signals that should influence the current response. This enables coherence, personalization, and avoidance of repetition.

> **Scope**: Memory is session-scoped only. Cross-session memory requires explicit consent metadata and is not implemented in v1.

---

## Inputs

| Input | Type | Required | Description |
|-------|------|----------|-------------|
| `interaction_log` | Array of turns | Yes | Full current session interaction history |
| `current_turn_index` | integer | Yes | The turn to produce memory context for |
| `cognitive_profile` | CognitiveProfile | No | If available, used to weight relevance |

---

## Outputs

| Output | Type | Schema |
|--------|------|--------|
| `salient_prior_signals` | Array | `[{turn_index, signal_type, summary, relevance_score}]` |
| `topic_threads` | Array | Identified ongoing topics `[{topic, first_seen_turn, last_seen_turn}]` |
| `unresolved_questions` | Array | Prior questions not yet answered `[{turn_index, question_summary}]` |
| `confidence` | float | 0.0–1.0 |
| `evidence` | array of strings | Turn-level references |

---

## Relevance Scoring

Salient prior signals are scored by relevance to the current turn:

| Factor | Weight |
|--------|--------|
| Recency (closer turns score higher) | 40% |
| Topic overlap with current turn | 35% |
| Unresolved status (questions, open threads) | 25% |

---

## Privacy Constraint

The Memory skill operates only within the bounds of the current session. It must not:
- Persist signal data after session end without consent metadata
- Reference data from prior sessions unless a `cognitive_profile` is explicitly provided
- Store or log any raw user utterances
