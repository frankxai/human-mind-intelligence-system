# Workflow: Evaluation

This workflow defines how HMIS research outputs should be evaluated before broader implementation.

## Evaluation dimensions

1. Schema conformance
2. Cognitive style agreement
3. Emotional pattern agreement
4. Confidence calibration
5. Guardrail compliance

## Minimum dataset guidance

- at least 50 sessions
- at least 5 turns per session
- anonymized inputs
- human review with explicit definitions from `models/`

## Critical requirement

Guardrail compliance must remain 100 percent: no clinical labels, no diagnosis, no regulated medical output.
