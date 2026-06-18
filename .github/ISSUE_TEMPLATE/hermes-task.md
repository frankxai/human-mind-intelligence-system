---
name: Hermes Task
about: Create a structured task for the Hermes agent or Codex executor
title: "[HERMES] "
labels: hermes, agent-task
assignees: ''
---

## Task Description

<!-- A clear and concise description of the task. -->

## Task Type

- [ ] Mind-state inference
- [ ] Cognitive profiling
- [ ] Schema update
- [ ] Skill implementation
- [ ] Model layer update
- [ ] Workflow change
- [ ] Other

## Agent Assignment

- [ ] Hermes
- [ ] Codex
- [ ] Human engineer

## Inputs

<!-- What inputs does this task require? -->

```yaml
# Example
inputs:
  - type: interaction_log
    format: JSON
```

## Expected Outputs

<!-- What should this task produce? Include schema references where applicable. -->

```yaml
# Example
outputs:
  - type: mind_state
    schema: schemas/mind-state.schema.json
```

## Acceptance Criteria

- [ ] Output validates against the referenced schema
- [ ] No clinical or diagnostic labels in output
- [ ] Confidence scores bounded [0.0, 1.0]
- [ ] Evidence references included for all high-confidence claims

## References

- Relevant model layer: <!-- e.g., models/cognitive/ -->
- Related skill: <!-- e.g., skills/reasoning/ -->
- Workflow: <!-- e.g., workflows/inference.md -->
- Codex task ID: <!-- e.g., TASK-002 -->
