# Skills — HMIS

Skills are modular enrichers that Hermes invokes during inference.

## Available skills

| Skill | Directory | Purpose |
|-------|-----------|---------|
| Empathy | `empathy/` | Read emotional register and response adaptation cues |
| Reasoning | `reasoning/` | Detect cognitive style and load signals |
| Memory | `memory/` | Surface relevant prior-session-turn context |

## Skill contract

```yaml
skill:
  id: string
  version: string
  model_layers:
    - string
  inputs:
    - type: string
  outputs:
    - type: string
  confidence_output: true
  evidence_output: true
```

## Rules

1. Skills are invoked by Hermes, not by end users directly.
2. Skills must remain non-clinical and research-only.
3. Skills must emit evidence with high-confidence claims.
4. Skills must tolerate partial context and degrade gracefully.
