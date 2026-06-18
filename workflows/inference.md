# Workflow: Inference

This workflow is the main Hermes loop for converting new interaction evidence into a revised `mind-state`.

## Flow

1. Extract behavior signals from the new turn.
2. Validate signals against `schemas/behavior-signal.schema.json`.
3. Route evidence into cognitive, emotional, behavioral, and social layers.
4. Invoke reasoning, empathy, and memory skills when relevant.
5. Synthesize the updated `mind-state`.
6. Validate output against `schemas/mind-state.schema.json`.
7. Emit the resulting research artifact.

## Confidence lifecycle

- 1 turn: low confidence
- 2-4 turns: building confidence
- 5+ turns: moderate or better if evidence is consistent

## Failure policy

If schema validation fails, Hermes should keep the last valid state and annotate the failure for review.
