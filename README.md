# Human Mind Intelligence System (HMIS)

> **Positioning**: HMIS is the **human-specific model layer** of the broader intelligence stack. It models how individual humans think, feel, behave, and learn — enabling AI systems to reason *about* humans, not *for* clinical diagnosis.
>
> ⚠️ **Guardrail**: This system is **NOT a clinical or medical tool**. It must not be used for psychiatric diagnosis, clinical treatment planning, or any regulated medical purpose. All models here are behavioral and cognitive primitives for AI interaction quality, not healthcare.

---

## Overview

HMIS provides a structured ontology of human psychological, cognitive, and behavioral primitives. It powers the Hermes agent layer and any downstream system that needs a rich model of human minds to improve interaction, personalization, and response prediction.

### What this repo contains

| Directory | Purpose |
|-----------|---------|
| `models/` | Core human mind model layers (cognitive, emotional, behavioral, social) |
| `schemas/` | JSON schemas for structured mind-state and profile data |
| `skills/` | Reusable AI skill definitions that leverage mind models |
| `workflows/` | Operational workflows (onboarding, inference, evaluation) |
| `.codex/` | Task board for AI agent execution |
| `.github/` | Issue templates and repo configuration |

### Key Documents

- [AGENTS.md](./AGENTS.md) — Agent roster and role definitions
- [HERMES.md](./HERMES.md) — Hermes agent specification
- [ROADMAP.md](./ROADMAP.md) — Versioned development roadmap
- [models/tribe-v2.md](./models/tribe-v2.md) — Tribe v2 social-cognitive model
- [humanmind.yaml](./humanmind.yaml) — System configuration

---

## Scope Boundaries

**In scope:**
- Modeling cognitive styles, emotional patterns, behavioral tendencies
- Predicting user response patterns and learning preferences
- Providing structured context for AI-human interaction design

**Out of scope:**
- Clinical diagnosis or treatment recommendations
- Regulated health data (PHI/HIPAA) processing
- Replacing licensed mental health professionals

---

## Contributing

See [AGENTS.md](./AGENTS.md) for the agent roster and task assignment model. All tasks are tracked in [.codex/tasks.md](./.codex/tasks.md).
