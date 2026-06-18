# Skills — Human Mind Intelligence System

Skills are modular, reusable AI capabilities that Hermes invokes during mind-state inference to enrich output quality. Each skill operates on specific model layer inputs and produces annotated signals.

---

## Available Skills

| Skill | Directory | Description |
|-------|-----------|-------------|
| Empathy | `empathy/` | Detects emotional register and adjusts communication accordingly |
| Reasoning | `reasoning/` | Identifies reasoning patterns and cognitive style signals |
| Memory | `memory/` | Extracts and references relevant prior context within a session |

---

## Skill Interface Contract

Every skill must conform to the following interface:

```yaml
skill:
  id: string               # unique skill identifier
  version: string          # semver
  inputs:                  # list of required input types
    - type: string
      schema: string       # optional schema reference
  outputs:                 # list of produced outputs
    - type: string
      schema: string
  model_layers:            # which model layers this skill reads
    - string
  confidence_output: true  # must always produce a confidence score
  evidence_output: true    # must always produce evidence references
```

---

## Skill Invocation Rules

1. Skills are invoked by Hermes, never directly by users.
2. Each skill must return a confidence score bounded `[0.0, 1.0]`.
3. Each skill must return evidence references (not just conclusions).
4. Skills must not produce clinical labels.
5. Skills are stateless — they receive input and produce output per invocation.

---

## Adding a New Skill

1. Create a directory under `skills/{skill-name}/`.
2. Add a `SKILL.md` file conforming to the interface contract above.
3. Register the skill in `humanmind.yaml` under `skills:`.
4. Add a task to `.codex/tasks.md` for implementation.
