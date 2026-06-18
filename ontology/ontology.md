# Ontology

A compact map of how the twelve cognitive constructs relate. The constructs are
the canon modules at
[`mind-intelligence-systems/models/human-mind/`](https://github.com/frankxai/mind-intelligence-systems/tree/main/models/human-mind).
This file names the **edges** between them — the relationships the canon Related
Constructs sections imply — so an agent can reason across modules, not just
within one.

The ontology is deliberately small. It is a working graph, not an attempt to
settle open questions in cognitive science.

## Constructs (nodes)

Each node maps 1:1 to a canon module and to a schema in [`../schemas/`](../schemas).

| Node | One-line role |
|---|---|
| `attention` | Selects what enters processing; gates the rest. |
| `memory` | Encodes, stores, retrieves over time. |
| `emotion` | Affective state: arousal, appraisal, action tendency. |
| `motivation` | Initiates and sustains goal-directed behavior. |
| `identity` | The self-model: roles, traits, narratives, possible selves. |
| `learning` | Durable change in knowledge, skill, behavior from experience. |
| `belief` | Representations held true that shape interpretation. |
| `behavior` | Observable action resulting from internal state × context. |
| `consciousness` | Subjective awareness; access and phenomenal experience. |
| `metacognition` | Monitoring and control of one's own cognition. |
| `decision-making` | Selecting among alternatives, forming intentions. |
| `social-cognition` | Processing information about other people and situations. |

## Relationships (edges)

Edges are typed. The four relationship types:

- **gates** — A controls what B receives.
- **feeds** — A supplies content or signal that B operates on.
- **modulates** — A shifts the parameters of B without supplying its content.
- **reflects-on** — A takes B as its object.

| From | Type | To | Why (grounded in canon Related Constructs) |
|---|---|---|---|
| `attention` | gates | `memory` | Only attended content is reliably encoded. |
| `attention` | gates | `consciousness` | Access consciousness tracks what attention selects. |
| `memory` | feeds | `learning` | Learning is durable change built on encoding and retrieval. |
| `memory` | feeds | `identity` | Autobiographical memory composes narrative identity. |
| `memory` | feeds | `belief` | Stored evidence and episodes back belief formation. |
| `learning` | modulates | `belief` | Epistemic learning updates beliefs (Bayesian-style). |
| `learning` | modulates | `behavior` | Reinforcement reshapes habitual and goal-directed action. |
| `emotion` | modulates | `motivation` | Approach/avoidance affect biases what is pursued. |
| `emotion` | modulates | `attention` | Affect drives attentional bias toward salient cues. |
| `emotion` | modulates | `memory` | Arousal at encoding alters later retrieval strength. |
| `emotion` | modulates | `decision-making` | Somatic markers weight options under uncertainty. |
| `motivation` | feeds | `behavior` | Goals initiate and direct action. |
| `motivation` | feeds | `decision-making` | Value and expectancy enter option evaluation. |
| `belief` | modulates | `decision-making` | Held priors shape how options are weighed. |
| `belief` | modulates | `behavior` | Beliefs about self and world steer action. |
| `decision-making` | feeds | `behavior` | A committed intention is enacted as behavior. |
| `behavior` | feeds | `learning` | Outcomes of action close the feedback loop into learning. |
| `identity` | modulates | `behavior` | Identity-consistent action; the identity–behavior gap. |
| `identity` | modulates | `motivation` | Possible selves set what is worth pursuing. |
| `metacognition` | reflects-on | `attention` | Meta-attention monitors where attention goes. |
| `metacognition` | reflects-on | `memory` | Metamemory tracks feeling-of-knowing and confidence. |
| `metacognition` | reflects-on | `learning` | Monitoring calibrates study and strategy choice. |
| `metacognition` | reflects-on | `decision-making` | Confidence judgments feed and check decisions. |
| `consciousness` | feeds | `metacognition` | Reportable content is the substrate metacognition inspects. |
| `social-cognition` | feeds | `identity` | Social and role identities form via mentalizing others. |
| `social-cognition` | modulates | `belief` | Stereotypes and social inference shape held beliefs. |
| `social-cognition` | modulates | `behavior` | Norms and social influence steer action. |
| `social-cognition` | modulates | `emotion` | Emotional contagion transfers affect between people. |

## Cross-cutting hubs

Three constructs sit at high degree in the graph and are worth watching when
reasoning across an observation set:

- **memory** — feeds learning, identity, and belief; gated by attention. Most
  durable change routes through it.
- **emotion** — modulates motivation, attention, memory, and decision-making. The
  widest modulator; a single affective shift can move four other systems.
- **metacognition** — reflects on attention, memory, learning, and decision-making.
  The system's self-correction layer.

## Reading the graph for an observation

When you hold observations across several constructs, walk the edges to form
cross-module hypotheses — and keep every step labelled per the
[response-prediction primitive](../docs/response-prediction.md):

1. A `memory` retrieval failure + an `emotion` high-arousal observation, joined by
   the `emotion → memory` modulates edge, suggests arousal-linked retrieval
   disruption as one hypothesis (not a conclusion).
2. A `metacognition` miscalibration observation + a `decision-making` observation,
   joined by `metacognition reflects-on decision-making`, suggests overconfidence
   may be entering a choice.

Edges license hypotheses. They never license diagnoses.
