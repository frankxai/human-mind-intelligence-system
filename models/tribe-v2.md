# Tribe v2 — Group Context Model

Tribe v2 extends HMIS from individual interaction patterns to the group contexts that shape them.

## Purpose

Tribe v2 helps Hermes reason about:
- which groups are salient in the current interaction
- what role a person seems to occupy in those groups
- how group norms may influence behavior, trust, and expression

## Core objects

```yaml
tribe:
  id: string
  label: string
  cohesion_score: float
  role: leader | contributor | observer | connector | challenger
  size_estimate: small | medium | large
```

```yaml
norm_alignment:
  tribe_id: string
  alignment_score: float
  tension_signals:
    - string
```

## Guardrail

Tribe v2 must not be used for demographic stereotyping, exclusion, or protected-class inference.

## Research stance

This model is for contextual interpretation only. It is not a basis for ranking human worth, entitlement, or opportunity.
