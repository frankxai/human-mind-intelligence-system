# Workflow: Onboarding

This workflow defines how HMIS starts a new research session.

## Flow

1. Collect context metadata.
2. Create a baseline low-confidence `mind-state` object.
3. Run early reasoning and empathy passes on the first turn.
4. Emit a valid initial state for downstream use.

## Guardrail

Onboarding may initialize inference, but it must not infer diagnosis or regulated medical status.
