# Cognitive Model Layer

This layer defines the cognitive primitives used by Hermes to model how an individual thinks, processes information, and reasons.

---

## Cognitive Style Primitives

| Primitive | Description | Observable Signals |
|-----------|-------------|-------------------|
| `analytical` | Preference for systematic, step-by-step reasoning | Uses structured arguments, requests data, asks "why" |
| `intuitive` | Pattern-based, rapid synthesis | Jumps to conclusions, uses metaphors, trusts gut |
| `narrative` | Thinks in stories and examples | Frequent anecdotes, context-heavy responses |
| `abstract` | Prefers conceptual over concrete | Uses theoretical framing, resists specifics |
| `concrete` | Prefers tangible examples | Requests specifics, action-oriented |

## Attention Modes

| Mode | Description |
|------|-------------|
| `focused` | Deep attention on single thread |
| `distributed` | Wide attention across multiple threads |
| `sequential` | One thing at a time, ordered |
| `parallel` | Multiple threads simultaneously |

## Cognitive Load Signals

Hermes monitors for cognitive load markers in interaction signals:
- Increased latency (when measurable)
- Shorter, more fragmented responses
- Requests for clarification or repetition
- Error rate increase

---

## Schema Reference

Cognitive primitives contribute to the `cognitive_profile` output:
`schemas/cognitive-profile.schema.json`
