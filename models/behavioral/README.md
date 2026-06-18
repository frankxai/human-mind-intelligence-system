# Behavioral Model Layer

This layer captures action tendencies and turn-level response patterns.

## Tendencies

| Primitive | Description | Observable signals |
|-----------|-------------|--------------------|
| `proactive` | initiates without prompting | offers next steps, introduces topics |
| `reactive` | responds to prompts more than initiating | waits for direction, answer-oriented |
| `deliberate` | slow, measured execution | pauses, careful revisions |
| `impulsive` | rapid action with low dwell time | quick replies, corrections after send |
| `persistent` | continues toward a goal despite friction | repeated follow-ups, escalation attempts |
| `adaptive` | changes strategy with feedback | framing shifts after correction |
| `habitual` | repeats stable patterns | recurring phrases and structures |
| `exploratory` | experiments with new moves | varied requests, style switching |

## Signal contract

Behavior signals should validate against [schemas/behavior-signal.schema.json](../../schemas/behavior-signal.schema.json).
