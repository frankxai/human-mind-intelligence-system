# Codex Task Board — HMIS

This task board is the canonical queue for repository execution work.

## Task format

```text
### TASK-{ID}: {Title}
- Status: open | in-progress | done | blocked
- Agent: codex | hermes | human
- Priority: P0 | P1 | P2
- Ref: issue/pr/or N/A
- Description: concise execution target
```

## Active

### TASK-001: HMIS foundation v1 scaffolding
- Status: done
- Agent: codex
- Priority: P0
- Ref: N/A
- Description: Create the full repository foundation, doctrine docs, models, schemas, skills, and workflows.

## Backlog

### TASK-002: Hermes inference engine
- Status: open
- Agent: hermes
- Priority: P0
- Ref: N/A
- Description: Implement the first executable inference loop that emits `mind-state` JSON.

### TASK-003: Schema validation automation
- Status: open
- Agent: codex
- Priority: P1
- Ref: N/A
- Description: Validate sample artifacts and future outputs against all schemas.

### TASK-004: Evaluation dataset design
- Status: open
- Agent: human
- Priority: P1
- Ref: N/A
- Description: Define anonymized evaluation inputs and review protocol for research calibration.

### TASK-005: Skill implementation plan
- Status: open
- Agent: hermes
- Priority: P1
- Ref: N/A
- Description: Turn empathy, reasoning, and memory skill contracts into executable modules.

### TASK-006: Downstream consumption review
- Status: open
- Agent: hermes
- Priority: P2
- Ref: N/A
- Description: Confirm the foundation is consumable by adjacent lived-OS and research-oriented systems.
