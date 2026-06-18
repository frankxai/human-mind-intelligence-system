# AGENTS — Human Mind Intelligence System

This document defines the agent roster for HMIS: who owns what, their responsibilities, and how they coordinate.

---

## Agent Roster

### Hermes

| Field | Value |
|-------|-------|
| **Role** | Primary orchestrator and mind-model reasoner |
| **Owner** | @frankxai |
| **Spec** | [HERMES.md](./HERMES.md) |
| **Responsibilities** | Schema inference, profile synthesis, workflow orchestration, skill invocation |
| **Input** | Raw interaction signals, behavioral logs, user context |
| **Output** | Structured mind-state objects, response predictions, annotated profiles |

### Codex (Task Executor)

| Field | Value |
|-------|-------|
| **Role** | Autonomous task executor for repo maintenance and scaffolding |
| **Owner** | GitHub Copilot Agent |
| **Task Board** | [.codex/tasks.md](./.codex/tasks.md) |
| **Responsibilities** | Creating files, updating schemas, running structured build tasks |

---

## Coordination Model

```
User / Operator
      │
      ▼
  [Hermes]  ──── reads ────▶  models/, schemas/, skills/
      │
      ├── invokes ──▶  skills/empathy/
      ├── invokes ──▶  skills/reasoning/
      ├── invokes ──▶  skills/memory/
      │
      └── emits ──▶  mind-state JSON (schemas/mind-state.schema.json)
```

---

## Agent Rules

1. No agent may produce clinical outputs (diagnosis, treatment, prognosis).
2. All structured outputs must validate against schemas in `schemas/`.
3. Agents must log reasoning steps to support auditability.
4. Hermes owns the canonical mind-state object; no other agent may overwrite it without Hermes approval.
5. Codex tasks must reference an issue or task ID from `.codex/tasks.md`.
