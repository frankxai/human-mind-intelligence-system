# Human Mind Intelligence System

[![Built on SIP](https://img.shields.io/badge/Built%20on-SIP-c9b6ff.svg)](https://github.com/frankxai/Starlight-Intelligence-System)
[![License: MIT](https://img.shields.io/badge/License-MIT-f4c97a.svg)](LICENSE)
[![Layer: Cognitive System](https://img.shields.io/badge/layer-cognitive%20system-blue.svg)](https://github.com/frankxai/mind-intelligence-systems)

The engineered System that turns the canonical human-mind model into installable
JSON schemas, ontology, and response-prediction primitives.

It observes and predicts. It never diagnoses.

## Where this sits

The shared human-mind model — twelve cognitive modules, their definitions, key
processes, and research grounding — is **canon**, and it lives upstream in
[mind-intelligence-systems](https://github.com/frankxai/mind-intelligence-systems).
This repo does not own that model; it **operationalizes** it. Each canon module
becomes an installable schema, the relationships between modules become an
ontology, and the whole thing drives a non-clinical response-prediction primitive.

Naming doctrine (from the canon): **OS** = lived daily · **System** = engineered,
installable product · **Systems** = the portfolio. This repo is a **System** — the
cognitive one.

## Quick map

| Path | What it is |
|---|---|
| [`schemas/`](schemas) | 12 JSON Schemas (draft 2020-12), one per construct — each models an *observation* |
| [`schemas/README.md`](schemas/README.md) | Index of all twelve schemas + the shared shape |
| [`ontology/ontology.md`](ontology/ontology.md) | How the twelve constructs relate (typed edges) |
| [`docs/response-prediction.md`](docs/response-prediction.md) | The non-clinical prediction primitive |
| [`CANON.md`](CANON.md) | Composes SIP + the human-mind canon; declines its own |
| [`CLAUDE.md`](CLAUDE.md) / [`AGENTS.md`](AGENTS.md) | Operating doctrine for agents |
| [`MEMORY.md`](MEMORY.md) | Version, commitments, anti-scope |

The twelve constructs: attention, memory, emotion, motivation, identity, learning,
belief, behavior, consciousness, metacognition, decision-making, social-cognition.

## Quick start — load a schema

Each schema validates one *observation* of a construct. Load it like any draft
2020-12 JSON Schema.

```python
import json
from jsonschema import Draft202012Validator

with open("schemas/attention.schema.json") as f:
    schema = json.load(f)

observation = {
    "construct": "attention",
    "observation": "Switched browser tabs 14 times in 10 minutes while drafting.",
    "indicators": ["task-switching", "mind-wandering"],
    "confidence": 0.9,
}

Draft202012Validator(schema).validate(observation)  # raises on invalid
```

The `observation` field holds only what was seen. Any reading of *what it means*
goes in the separate `interpretation` object, with its own confidence and evidence.
That separation is the point — see
[`docs/response-prediction.md`](docs/response-prediction.md).

## Safety principle

Non-clinical by construction. This System models cognition, forms labelled
hypotheses, and predicts likely responses with confidence. It does **not** diagnose,
name disorders, or recommend treatment. Five stages stay labelled and separate:
**observe → interpret → hypothesize → evidence → decide**. The decision is always
human-owned. This principle is non-waivable.

## The Mind Intelligence ecosystem

| Repo | Family | Role |
|---|---|---|
| [mind-intelligence-systems](https://github.com/frankxai/mind-intelligence-systems) | canon | naming · models · mesh |
| [human-mind-intelligence-system](https://github.com/frankxai/human-mind-intelligence-system) | cognitive | schemas · ontology *(this repo)* |
| [agentic-mind-os](https://github.com/frankxai/agentic-mind-os) | lived OS | personal mind OS |
| [starlight-mind-os-pro](https://github.com/frankxai/starlight-mind-os-pro) | lived OS | premium distribution |
| [awesome-mind-agent-skills](https://github.com/frankxai/awesome-mind-agent-skills) | discovery | the front door |
| [mind-palace-agent-skills](https://github.com/frankxai/mind-palace-agent-skills) | memory palace | Blessing skills |
| [frankx-mind-palace](https://github.com/frankxai/frankx-mind-palace) | memory palace | blessed work as data |

## License & attestation
MIT — see [`LICENSE`](LICENSE).
**Built on SIP.** Composes the [Starlight Intelligence Protocol](https://github.com/frankxai/Starlight-Intelligence-System). Per SIP § Sovereignty clause.
Built by [Frank Riemer](https://frankx.ai). For builders, not consumers.

<!-- STARLIGHT:OPERATING:BEGIN v2 sha=9f8fecc91edc source=794db1e51a55a128816f7aa266eb0ac1dbd452c3 -->

## Agent operating guidance

Repository agents use the shared Starlight operating contract in `AGENTS.md` alongside local instructions.
The contract asks agents to establish a useful outcome, select relevant skills, complete authorized work,
verify current sources, refine the actual artifact, and report evidence and remaining gates.
It covers human agency, privacy, rights, resource stewardship and bounded proactivity.
Repository identity, brand, canon, build commands and release gates remain local.

[Pinned contract](https://github.com/frankxai/Starlight-Intelligence-System/blob/794db1e51a55a128816f7aa266eb0ac1dbd452c3/docs/architecture/agents-md/band-a.md)
· [Projection and verification](https://github.com/frankxai/Starlight-Intelligence-System/blob/794db1e51a55a128816f7aa266eb0ac1dbd452c3/docs/architecture/AGENTS-MD-CONTRACT.md)

These files supply operating guidance. They do not activate an agent, grant tool permissions,
schedule recurring work, certify compliance or prove a live capability.

<!-- STARLIGHT:OPERATING:END -->
