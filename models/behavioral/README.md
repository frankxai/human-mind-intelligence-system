# Behavioral Model Layer

This layer defines the behavioral signal classifiers and tendency models used by Hermes to predict and interpret human actions and response patterns.

---

## Behavioral Tendency Primitives

| Primitive | Description | Observable Signals |
|-----------|-------------|-------------------|
| `proactive` | Initiates, leads, takes action without prompting | Unsolicited suggestions, first-mover in dialogue |
| `reactive` | Responds to stimuli, waits for cues | Responds to questions, rarely initiates |
| `deliberate` | Thinks before acting, measured pace | Long response latency, careful word choice |
| `impulsive` | Quick reactions, acts before reflecting | Fast responses, frequent corrections, high edit rate |
| `persistent` | Continues despite obstacles | Re-asks questions, follows up, escalates |
| `adaptive` | Changes approach based on feedback | Style shifts after correction, flexible framing |
| `habitual` | Consistent patterns across contexts | Repeated phrases, consistent structure |
| `exploratory` | Tries new approaches, low habit lock-in | Varied vocabulary, experiments with framing |

---

## Behavior Signal Schema

Individual behavioral signals are validated against:
`schemas/behavior-signal.schema.json`

A signal represents a single observable unit:
```yaml
signal:
  timestamp: ISO8601
  type: string           # e.g., "initiated_topic", "requested_clarification"
  context: string        # brief description of the interaction context
  intensity: float       # 0.0–1.0
```

---

## Response Pattern Prediction

Hermes uses behavioral primitives to predict likely next actions:
- A `proactive + analytical` profile predicts structured proposals.
- A `reactive + guarded` profile predicts minimal disclosure until trust-building.
- A `persistent + frustrated` profile predicts escalation if not resolved.
