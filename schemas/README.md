# Schemas

Twelve JSON Schemas (draft 2020-12), one per cognitive module. Each models an
**observation** of a construct — not the construct itself, and never a diagnosis.

Every schema shares one shape so a single loader can validate any of them:

| Field | What it holds | Required |
|---|---|---|
| `schemaVersion` | Schema-family version (`0.1.0`) | no |
| `construct` | Which module this is about (a fixed `const`) | yes |
| `observation` | Plain-language description of what was observed — no inference | yes |
| `indicators` | Discrete observable markers, drawn from the module's canon Key Processes | no |
| `context` | Setting, task, duration | no |
| `confidence` | 0–1 confidence in the **observation** | yes |
| `interpretation` | A labelled, falsifiable hypothesis — kept **separate** from observation | no |
| `provenance` | Source, observer, timestamp, source reliability | no |

The hard line: `observation` records what happened; `interpretation` records what
it might mean. They never blur. `interpretation` carries its own `confidence`,
`evidence`, and `alternatives`, and it is always optional. See
[`../docs/response-prediction.md`](../docs/response-prediction.md) for how a
hypothesis turns into a (non-clinical) predicted response.

## Index

| Construct | Schema | Canon module |
|---|---|---|
| Attention | [`attention.schema.json`](attention.schema.json) | [attention](https://github.com/frankxai/mind-intelligence-systems/blob/main/models/human-mind/attention.md) |
| Memory | [`memory.schema.json`](memory.schema.json) | [memory](https://github.com/frankxai/mind-intelligence-systems/blob/main/models/human-mind/memory.md) |
| Emotion | [`emotion.schema.json`](emotion.schema.json) | [emotion](https://github.com/frankxai/mind-intelligence-systems/blob/main/models/human-mind/emotion.md) |
| Motivation | [`motivation.schema.json`](motivation.schema.json) | [motivation](https://github.com/frankxai/mind-intelligence-systems/blob/main/models/human-mind/motivation.md) |
| Identity | [`identity.schema.json`](identity.schema.json) | [identity](https://github.com/frankxai/mind-intelligence-systems/blob/main/models/human-mind/identity.md) |
| Learning | [`learning.schema.json`](learning.schema.json) | [learning](https://github.com/frankxai/mind-intelligence-systems/blob/main/models/human-mind/learning.md) |
| Belief | [`belief.schema.json`](belief.schema.json) | [belief](https://github.com/frankxai/mind-intelligence-systems/blob/main/models/human-mind/belief.md) |
| Behavior | [`behavior.schema.json`](behavior.schema.json) | [behavior](https://github.com/frankxai/mind-intelligence-systems/blob/main/models/human-mind/behavior.md) |
| Consciousness | [`consciousness.schema.json`](consciousness.schema.json) | [consciousness](https://github.com/frankxai/mind-intelligence-systems/blob/main/models/human-mind/consciousness.md) |
| Metacognition | [`metacognition.schema.json`](metacognition.schema.json) | [metacognition](https://github.com/frankxai/mind-intelligence-systems/blob/main/models/human-mind/metacognition.md) |
| Decision-making | [`decision-making.schema.json`](decision-making.schema.json) | [decision-making](https://github.com/frankxai/mind-intelligence-systems/blob/main/models/human-mind/decision-making.md) |
| Social cognition | [`social-cognition.schema.json`](social-cognition.schema.json) | [social-cognition](https://github.com/frankxai/mind-intelligence-systems/blob/main/models/human-mind/social-cognition.md) |

## Example: a valid attention observation

```json
{
  "schemaVersion": "0.1.0",
  "construct": "attention",
  "observation": "Switched browser tabs 14 times in 10 minutes while drafting.",
  "indicators": ["task-switching", "mind-wandering", "cognitive-load-high"],
  "context": { "task": "writing a proposal", "duration": "PT10M" },
  "confidence": 0.9,
  "interpretation": {
    "hypothesis": "Attention may be fragmenting under high cognitive load.",
    "lens": "resource-model",
    "evidence": ["14 switches in 10 min", "self-reported feeling scattered"],
    "alternatives": ["Tab-switching is task-required research, not fragmentation."],
    "confidence": 0.45
  },
  "provenance": {
    "source": "behavioral-log",
    "observer": "focus-tracker",
    "timestamp": "2026-06-18T14:30:00Z",
    "reliability": 0.8
  }
}
```

Note that observation confidence (`0.9`) sits well above interpretation confidence
(`0.45`), and the interpretation carries an explicit alternative. That gap is the
discipline the schema exists to enforce.
