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
| [`ontology/ontology.md`](ontology/ontology.md) | How the twelve constructs relate (typed edges) · machine-readable in [`ontology/edges.json`](ontology/edges.json) |
| [`docs/response-prediction.md`](docs/response-prediction.md) | The non-clinical prediction primitive |
| [`docs/explorer/index.html`](docs/explorer/index.html) | Interactive explorer — drill into every construct, schema, edge, and its research grounding (open in a browser) |
| [`docs/research/`](docs/research) | Research grounding — frontier AI-lab + cognitive-science anchors per construct |
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

## Explore and ground it

Two surfaces sit on top of the schemas without changing them:

- **[Visual explorer](docs/explorer/index.html)** — a self-contained, zero-build page
  (open it directly in a browser). Click any of the twelve constructs to see its
  schema indicators, interpretation lenses, the ontology edges that connect it, and
  the research that grounds its model. Its data is generated from the schemas,
  [`ontology/edges.json`](ontology/edges.json), and
  [`docs/research/research.json`](docs/research/research.json):

  ```bash
  node scripts/build-explorer.mjs          # regenerate docs/explorer/explorer-data.js
  node scripts/build-explorer.mjs --check  # fail if stale (CI-friendly)
  ```

- **[Research grounding](docs/research/)** — why this System is, at its core, a
  *non-clinical prediction primitive*, and how that maps to frontier work on world
  foundation models and the predictive brain. Start with
  [`docs/research/frontier-map.md`](docs/research/frontier-map.md). The boundary
  holds: this grounds the construct *models*, never the profiling of a person.

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
