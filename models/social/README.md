# Social Model Layer

This layer defines the social context primitives and relational pattern models used by Hermes. It focuses on how an individual engages in relationships and communicates within social contexts.

---

## Relational Pattern Primitives

| Primitive | Description | Observable Signals |
|-----------|-------------|-------------------|
| `high_trust` | Open, vulnerable, assumes good faith | Personal disclosure, low hedging, collaborative tone |
| `low_trust` | Guarded, skeptical, verification-seeking | Questions motives, requests evidence, formal tone |
| `authority_oriented` | Defers to or challenges authority structures | References credentials, title-conscious |
| `peer_oriented` | Values horizontal relationships | First-name basis, informal tone, equality framing |
| `independent` | Self-reliant, low need for validation | Low question rate, confident assertions |
| `interdependent` | Values collective, seeks consensus | High question rate, inclusive language |

---

## Communication Style Model

```yaml
communication_style:
  directness: float       # 0.0 = very indirect, 1.0 = very direct
  formality: float        # 0.0 = very informal, 1.0 = very formal
  verbosity: float        # 0.0 = terse, 1.0 = verbose
  questioning_rate: float # proportion of turns containing questions
```

---

## Relationship to Tribe v2

The Social model layer provides individual-level primitives. [Tribe v2](../tribe-v2.md) extends this to group-level dynamics. Together they provide:

- Individual social stance (this layer)
- Group membership and role (Tribe v2)
- Inter-group dynamics (Tribe v2)

---

## Schema Reference

Social primitives contribute to the `mind-state.social_context` field in:
`schemas/mind-state.schema.json`
