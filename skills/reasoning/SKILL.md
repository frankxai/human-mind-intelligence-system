# Reasoning Skill

The reasoning skill identifies how a person appears to be thinking so Hermes can match depth, structure, and explanation style.

## Metadata

```yaml
skill:
  id: reasoning
  version: "1.0.0"
  status: scaffolded
  model_layers:
    - cognitive
```

## Outputs

- `dominant_style`
- `secondary_style`
- `attention_mode`
- `cognitive_load_signal`
- `reasoning_annotation`
- `confidence`
- `evidence`

## v1 heuristics

- causal connectors suggest `analytical`
- metaphor and synthesis leaps suggest `intuitive`
- story framing suggests `narrative`
- principle-first framing suggests `abstract`
- example-first framing suggests `concrete`
