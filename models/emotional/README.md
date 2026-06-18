# Emotional Model Layer

This layer defines the emotional pattern primitives used by Hermes. These are **not** clinical emotion categories — they are behavioral pattern signatures observable in interaction signals.

---

## Emotional Pattern Primitives

| Pattern | Description | Observable Signals |
|---------|-------------|-------------------|
| `engaged` | High positive energy and interest | Expressive language, questions, elaboration |
| `withdrawn` | Low energy, minimal engagement | Short responses, monosyllabic, passive tone |
| `frustrated` | Tension, resistance, or blocked goals | Interruptions, repetition, assertive framing |
| `curious` | Open, exploratory, seeking | Questions, hypotheticals, "what if" framing |
| `confident` | High certainty, declarative | Direct statements, low hedging |
| `uncertain` | Low certainty, hesitant | Hedging language, qualifications, questions |
| `collaborative` | Seeking shared understanding | "We", inclusive framing, agreement-seeking |
| `guarded` | Protective, low disclosure | Vague responses, topic deflection |

---

## Tone Tendency Model

Tone tendencies describe the individual's default emotional register across interactions:

```yaml
tone_tendency:
  primary: string        # e.g., "warm", "formal", "direct", "playful"
  secondary: string      # secondary tone modifier
  variability: float     # 0.0 = very stable, 1.0 = highly variable
```

---

## Guardrail

Emotional patterns are **observational**, not diagnostic. Hermes must not map any pattern to a clinical emotion disorder label (e.g., depression, anxiety disorder). Emotional primitives describe communication style, not mental health status.

---

## Schema Reference

Emotional patterns contribute to `mind-state.type.emotional_pattern` in:
`schemas/mind-state.schema.json`
