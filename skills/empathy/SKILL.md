# Empathy Skill

The empathy skill reads emotional and social cues so Hermes can adapt response posture without pretending to practice therapy or diagnosis.

## Metadata

```yaml
skill:
  id: empathy
  version: "1.0.0"
  status: scaffolded
  model_layers:
    - emotional
    - social
```

## Inputs

- `interaction_log`
- `models/emotional/`
- optional `models/social/`

## Outputs

- `emotional_pattern`
- `tone_tendency`
- `adaptation_hint`
- `confidence`
- `evidence`

## Example adaptation hints

| Pattern | Hint |
|---------|------|
| `frustrated` | acknowledge friction, then narrow solution space |
| `withdrawn` | reduce pressure and verbosity |
| `curious` | provide room for exploration |
| `guarded` | avoid invasive probing |
| `uncertain` | add structure and reassurance |

## Guardrail

Empathy in HMIS means emotional calibration, not clinical interpretation.
