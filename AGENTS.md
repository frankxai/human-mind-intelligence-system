# AGENTS — HMIS Operating Roster

This file defines the agents, ownership boundaries, and coordination rules for the Human Mind Intelligence System.

## Agent roster

### Hermes

| Field | Value |
|-------|-------|
| Role | Primary mind-model orchestrator |
| Owner | @frankxai |
| Spec | [HERMES.md](./HERMES.md) |
| Reads | `models/`, `schemas/`, `skills/`, `workflows/` |
| Produces | `mind-state`, `cognitive-profile`, skill annotations |
| Mode | Research-only, non-clinical |

### Codex

| Field | Value |
|-------|-------|
| Role | Repository task executor and scaffolder |
| Owner | GitHub Copilot Coding Agent |
| Task board | [.codex/tasks.md](./.codex/tasks.md) |
| Reads | issues, tasks, repo docs |
| Produces | file changes, schema updates, workflow scaffolds |

### Human operator

| Field | Value |
|-------|-------|
| Role | Sets doctrine, acceptance criteria, and release direction |
| Control surface | Issues, pull requests, roadmap, direct review |
| Final authority | Approves changes and decides production use |

## Coordination model

```text
Human operator
   │
   ├── sets doctrine / tasks
   ▼
Hermes ── reads models + schemas + skills ──▶ emits structured human-state artifacts
   │
   └── invokes skill contracts for richer interpretation

Codex ── maintains repository structure, tasks, and implementation scaffolding
```

## Operating rules

1. HMIS is **research-only** in v1.
2. No agent may emit clinical diagnosis, treatment advice, or regulated medical output.
3. All structured outputs must validate against files in `schemas/`.
4. Hermes owns inference; Codex owns scaffolding; humans own approval.
5. Every high-confidence claim must carry evidence references.
6. Reference swarm links should be maintained when adding new core artifacts.

## Reference swarm

- [README.md](./README.md)
- [HERMES.md](./HERMES.md)
- [humanmind.yaml](./humanmind.yaml)
- [.codex/tasks.md](./.codex/tasks.md)
