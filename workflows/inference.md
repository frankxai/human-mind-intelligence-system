# Workflow: Inference

This workflow describes the continuous inference loop that Hermes runs on each new interaction turn. It is the core operational cycle of HMIS.

---

## Overview

```
New Interaction Turn
        │
        ▼
  [Extract Behavior Signals]
        │
        ▼
  [Validate Signals]  ──▶  schemas/behavior-signal.schema.json
        │
        ▼
  [Route to Model Layers]
        │
        ├──▶  Cognitive Layer  ──▶  [Reasoning Skill]
        ├──▶  Emotional Layer  ──▶  [Empathy Skill]
        ├──▶  Behavioral Layer
        └──▶  Social Layer
        │
        ▼
  [Synthesize Mind-State]
        │
        ▼
  [Validate Output]  ──▶  schemas/mind-state.schema.json
        │
        ▼
  [Emit Mind-State]
```

---

## Steps

### 1. Extract Behavior Signals

For each new turn, extract observable behavior signals matching the `BehaviorSignal` schema:

- Signal type (from the enum in `schemas/behavior-signal.schema.json`)
- Context description
- Intensity estimate (0.0–1.0)
- Model layer hint

### 2. Validate Signals

Validate each extracted signal against `schemas/behavior-signal.schema.json`. Discard invalid signals; log validation failures for audit.

### 3. Route to Model Layers

Route validated signals to the relevant model layer(s):

| Signal `model_layer_hint` | Model Layer | Skill |
|---------------------------|-------------|-------|
| `cognitive` | `models/cognitive/` | Reasoning |
| `emotional` | `models/emotional/` | Empathy |
| `behavioral` | `models/behavioral/` | (direct) |
| `social` | `models/social/` | (direct) |
| (none) | All layers | All applicable skills |

### 4. Synthesize Mind-State

Aggregate outputs from all model layers and skill invocations into a unified `mind-state` object:

1. Update each layer's `dominant` value if new evidence is stronger.
2. Recalculate overall `confidence` as the weighted average of layer confidences.
3. Set `low_confidence_flag = true` if overall confidence < 0.4.
4. Append new `evidence` references to each layer.
5. Append skill annotations.

### 5. Validate Output

Validate the synthesized mind-state against `schemas/mind-state.schema.json`. If validation fails:
- Log the error with full context.
- Return the previous valid mind-state with a `validation_error` note.

### 6. Emit Mind-State

Emit the validated mind-state object as the primary output of this inference cycle.

---

## Confidence Lifecycle

| Turns Processed | Expected Confidence Range |
|-----------------|--------------------------|
| 1 | 0.0–0.3 (low confidence) |
| 2–4 | 0.3–0.6 (building) |
| 5–10 | 0.5–0.8 (moderate confidence) |
| 10+ | 0.7–1.0 (high confidence) |

---

## Error Handling

| Error Type | Action |
|------------|--------|
| Schema validation failure | Log, return prior state |
| Skill invocation failure | Log, skip skill, continue |
| Model layer unavailable | Log, emit low-confidence flag |
| Conflicting evidence | Use higher-confidence signal; log conflict |
