# Human Mind Intelligence System (HMIS)

> **Positioning**: Human Mind Intelligence System is the human-specific model layer for Mind Intelligence Systems. It models attention, memory, emotion, behavior, social context, and response tendencies so AI systems can reason about humans as humans — without drifting into diagnosis, treatment, or any regulated medical use.
>
> **Extended research scope**: The foundation is intended to support later modeling of motivation, perception, learning, belief, identity, consciousness, social cognition, metacognition, and neural response prediction through explicit schemas and skills rather than implicit speculation.
>
> **Guardrail**: HMIS is **research-only** and **non-clinical**. It must not be used for psychiatric diagnosis, clinical treatment planning, crisis triage, or any medical decision-making workflow.

---

## Why this repository exists

HMIS provides the foundation artifacts for building agent-readable, schema-driven, human-centered intelligence systems. The repository defines the doctrine, model layers, skills, workflows, and schemas required for Hermes and related agents to infer human mind-state primitives in a disciplined, explainable way.

## Doctrine

HMIS follows a simple doctrine that keeps the stack aligned:

- **OS is lived** — the human being, their biography, and their actual experience are never reducible to software.
- **System is engineered** — HMIS is an engineered inference layer that represents observed patterns, not the full person.
- **Systems is the category** — this repository belongs to the broader family of Mind Intelligence Systems and supplies the human-specific layer inside that category.

## Quick start

Start with `humanmind.yaml`, then read `HERMES.md`, `models/`, `schemas/`, `skills/`, and `workflows/` in that order.

## Repository map

| Path | Purpose |
|------|---------|
| `AGENTS.md` | Operating roster for Hermes, Codex, and human collaborators |
| `HERMES.md` | Canonical agent specification for Hermes |
| `ROADMAP.md` | Versioned plan from foundation through implementation |
| `humanmind.yaml` | Machine-readable system manifest |
| `.codex/tasks.md` | Task board for agent execution |
| `models/` | Human model layers and doctrine-aligned primitives |
| `schemas/` | JSON Schemas for structured outputs and inputs |
| `skills/` | Reusable skill contracts for Hermes orchestration |
| `workflows/` | Operational flows for onboarding, inference, and evaluation |

## Foundation scope

**In scope**
- Attention, reasoning style, and cognitive load primitives
- Emotional and behavioral interaction patterns
- Social context and tribe-aware framing
- Agent-readable schemas and workflow contracts
- Research scaffolding for future implementation

**Out of scope**
- Medical, psychiatric, or therapeutic decisions
- Identity claims beyond observable interaction signals
- Population scoring, protected-class inference, or discriminatory targeting
- Production persistence of raw human interaction data in v1

## Reference swarm

- [AGENTS.md](./AGENTS.md)
- [HERMES.md](./HERMES.md)
- [ROADMAP.md](./ROADMAP.md)
- [models/README.md](./models/README.md)
- [models/tribe-v2.md](./models/tribe-v2.md)
- [skills/SKILL.md](./skills/SKILL.md)
- [workflows/inference.md](./workflows/inference.md)
- [schemas/mind-state.schema.json](./schemas/mind-state.schema.json)

## Acceptance criteria for foundation v1

- The repository structure is present and navigable.
- Core docs are consistent, non-clinical, and agent-readable.
- Schemas are valid JSON Schema draft-07 documents.
- Hermes has explicit guardrails, inputs, outputs, and dependencies.
- The repo is ready for research and implementation work in later versions.
