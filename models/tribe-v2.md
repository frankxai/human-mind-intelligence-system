# Tribe v2 — Social-Cognitive Group Model

Tribe v2 is the group-level social-cognitive model within HMIS. Where the other model layers (cognitive, emotional, behavioral) focus on the individual, Tribe v2 models how individuals behave and think within social groups and networks.

---

## Purpose

Humans are social animals. Much of cognition and behavior is shaped by group membership, role expectations, and tribal dynamics. Tribe v2 provides the primitives to model:

- An individual's relationship to their social groups (tribes)
- How group norms shape individual behavior
- Inter-group dynamics that affect communication and trust

---

## Core Concepts

### Tribe

A **tribe** is any stable social group an individual belongs to — professional team, family, community, online network. A person may belong to multiple tribes simultaneously.

```yaml
tribe:
  id: string
  label: string           # e.g., "engineering team", "family"
  cohesion_score: float   # 0.0–1.0 (how strongly the person identifies)
  role: string            # e.g., leader, contributor, observer
  size_estimate: string   # small (<10), medium (10–50), large (50+)
```

### Social Role

An individual's **social role** within a tribe shapes their communication style and behavioral expectations.

| Role | Behavioral Signature |
|------|---------------------|
| Leader | Directive, accountable, high context-setting |
| Contributor | Collaborative, task-focused, moderate initiative |
| Observer | Listening, low-initiative, high absorption |
| Connector | Bridge-builder, high social bandwidth |
| Challenger | Questioning, high critical engagement |

### Tribal Norm Alignment

How closely an individual's expressed behavior aligns with their tribe's norms.

```yaml
norm_alignment:
  tribe_id: string
  alignment_score: float   # 0.0 = nonconformist, 1.0 = fully conformist
  tension_signals: []      # list of behavioral signals indicating norm tension
```

---

## Version History

| Version | Changes |
|---------|---------|
| v1 | Initial tribe membership model (roles, cohesion) |
| v2 | Added norm alignment, multi-tribe support, inter-group dynamics |

---

## Integration with Hermes

Hermes uses Tribe v2 to contextualize individual profiles:

1. Identify which tribes are salient in the current interaction context.
2. Apply tribal role primitives to modulate behavioral predictions.
3. Flag norm tension signals when individual behavior deviates from tribal expectations.

---

## Guardrail

Tribe v2 models social dynamics at the behavioral level only. It must not be used to stereotype, discriminate against, or make predictions based on demographic group membership.
