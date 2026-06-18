# Codex Task Board — HMIS

This file is the canonical task board for AI agent execution within the Human Mind Intelligence System. Tasks here are assigned to the Codex agent for autonomous execution.

---

## Task Format

```
### TASK-{ID}: {Title}
- **Status**: open | in-progress | done | blocked
- **Agent**: codex | hermes
- **Priority**: P0 | P1 | P2
- **Ref**: #{issue_number} or N/A
- **Description**: ...
```

---

## Active Tasks

### TASK-001: Foundation Scaffolding
- **Status**: done
- **Agent**: codex
- **Priority**: P0
- **Ref**: N/A
- **Description**: Create all foundation files and folder structure per HMIS Foundation v1 spec. Includes README, AGENTS.md, HERMES.md, ROADMAP.md, humanmind.yaml, models/, schemas/, skills/, workflows/.

---

## Backlog

### TASK-002: Implement Hermes Inference Engine
- **Status**: open
- **Agent**: hermes
- **Priority**: P0
- **Ref**: N/A
- **Description**: Build the core inference engine that accepts interaction logs and produces mind-state JSON conforming to `schemas/mind-state.schema.json`.

### TASK-003: Implement Schema Validation Pipeline
- **Status**: open
- **Agent**: codex
- **Priority**: P1
- **Ref**: N/A
- **Description**: Set up automated validation of all output JSON against schemas in `schemas/` as part of CI.

### TASK-004: Implement Empathy Skill
- **Status**: open
- **Agent**: codex
- **Priority**: P1
- **Ref**: N/A
- **Description**: Implement the empathy skill per `skills/empathy/SKILL.md`.

### TASK-005: Implement Reasoning Skill
- **Status**: open
- **Agent**: codex
- **Priority**: P1
- **Ref**: N/A
- **Description**: Implement the reasoning skill per `skills/reasoning/SKILL.md`.

### TASK-006: Implement Memory Skill
- **Status**: open
- **Agent**: codex
- **Priority**: P1
- **Ref**: N/A
- **Description**: Implement the memory skill per `skills/memory/SKILL.md`.

### TASK-007: Add CI/CD Pipeline
- **Status**: open
- **Agent**: codex
- **Priority**: P2
- **Ref**: N/A
- **Description**: Add GitHub Actions workflows for linting, schema validation, and unit tests.

### TASK-008: Tribe v2 Model Integration
- **Status**: open
- **Agent**: hermes
- **Priority**: P2
- **Ref**: N/A
- **Description**: Integrate the Tribe v2 group-level social-cognitive model into Hermes inference.
