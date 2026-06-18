# Models — Human Mind Intelligence System

This directory contains the core model layers for HMIS. Each layer represents a distinct dimension of the human mind that Hermes uses to construct profiles and inferences.

---

## Model Layers

| Layer | Directory | Description |
|-------|-----------|-------------|
| Cognitive | `cognitive/` | Thinking styles, reasoning patterns, attention modes |
| Emotional | `emotional/` | Emotional patterns, tone tendencies, affect regulation |
| Behavioral | `behavioral/` | Action tendencies, response patterns, habit signals |
| Social | `social/` | Relational dynamics, group roles, communication styles |

## Special Models

- [tribe-v2.md](./tribe-v2.md) — Tribe v2: group-level social-cognitive model

---

## Model Design Principles

1. **Non-clinical**: All primitives are behavioral/cognitive, never diagnostic.
2. **Composable**: Layers can be combined to form richer profiles.
3. **Evidence-based**: Each primitive maps to observable signals, not inferred pathology.
4. **Updatable**: Models should be independently versioned and replaceable.

---

## How Models Feed Hermes

```
models/cognitive/  ──┐
models/emotional/  ──┤──▶  Hermes Inference  ──▶  mind-state JSON
models/behavioral/ ──┤
models/social/     ──┘
```

Each layer exposes a vocabulary of primitives. Hermes selects relevant primitives based on input signals and synthesizes them into a unified `mind-state` object.
