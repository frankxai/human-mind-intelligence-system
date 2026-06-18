# Memory Skill

The memory skill helps Hermes preserve coherence within a session by surfacing relevant prior turns, unresolved threads, and repeated signals.

## Metadata

```yaml
skill:
  id: memory
  version: "1.0.0"
  status: scaffolded
  model_layers:
    - cognitive
    - behavioral
```

## Outputs

- `salient_prior_signals`
- `topic_threads`
- `unresolved_questions`
- `confidence`
- `evidence`

## Privacy rule

The v1 memory skill is session-scoped only and must not persist raw interaction data beyond approved research workflows.
