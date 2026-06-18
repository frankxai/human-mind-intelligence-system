---
name: Hermes Task
about: Structured task request for Hermes, Codex, or a human collaborator
title: "[HERMES] "
labels: hermes, agent-task
assignees: ""
---

## Summary

Describe the requested task in one or two clear paragraphs.

## Task Type

- [ ] Mind-state inference
- [ ] Cognitive profile update
- [ ] Schema change
- [ ] Skill implementation
- [ ] Model layer update
- [ ] Workflow refinement
- [ ] Research artifact
- [ ] Other

## Assigned execution mode

- [ ] Hermes
- [ ] Codex
- [ ] Human operator

## Inputs

```yaml
inputs:
  - type: interaction_log
    format: json
```

## Expected outputs

```yaml
outputs:
  - type: mind_state
    schema: schemas/mind-state.schema.json
```

## Guardrail checks

- [ ] Research-only use is preserved
- [ ] No clinical or diagnostic output is requested
- [ ] Evidence references are required for strong claims
- [ ] Confidence values are bounded `[0.0, 1.0]`

## Acceptance criteria

- [ ] Output or change is reviewable and agent-readable
- [ ] Related schema or model references are linked
- [ ] Doctrine remains consistent with README and HERMES

## Reference swarm

- Relevant model layer:
- Related skill:
- Related workflow:
- Related task ID:
