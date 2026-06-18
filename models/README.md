# Models — HMIS

The `models/` tree contains the human-model layers used by Hermes. Each layer captures a different slice of observable human interaction without claiming to describe the total person.

## Layer map

| Layer | Directory | Focus |
|-------|-----------|-------|
| Cognitive | `cognitive/` | Attention, reasoning style, cognitive load |
| Emotional | `emotional/` | Emotional interaction patterns and tone |
| Behavioral | `behavioral/` | Action tendencies and response habits |
| Social | `social/` | Trust stance, directness, and relational framing |

## Doctrine rules for models

1. Model observable patterns, not identities.
2. Prefer evidence-linked primitives over hidden-variable speculation.
3. Stay non-clinical and research-only.
4. Keep layers composable for downstream systems.

## Special model

- [tribe-v2.md](./tribe-v2.md) — group-context and role dynamics model.

## Reference swarm

- [README.md](../README.md)
- [schemas/mind-state.schema.json](../schemas/mind-state.schema.json)
- [HERMES.md](../HERMES.md)
