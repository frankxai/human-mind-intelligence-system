# HMIS Roadmap

This document tracks the versioned development plan for the Human Mind Intelligence System.

---

## v1 — Foundation (Current)

**Goal**: Establish the structural and conceptual foundation for the HMIS.

### Deliverables
- [x] Repository scaffolding (this PR)
- [x] README with positioning and guardrail
- [x] AGENTS.md — agent roster
- [x] HERMES.md — Hermes agent specification
- [x] `models/` — cognitive, emotional, behavioral, social layers
- [x] `models/tribe-v2.md` — Tribe v2 social model
- [x] `schemas/` — JSON schemas for mind-state, cognitive profile, behavior signal
- [x] `skills/` — empathy, reasoning, memory skill scaffolds
- [x] `workflows/` — onboarding, inference, evaluation workflows
- [x] `.codex/tasks.md` — Codex task board
- [x] `.github/ISSUE_TEMPLATE/hermes-task.md` — issue template

### Success Criteria
- Any engineer can clone the repo and understand the architecture within 15 minutes.
- Hermes agent spec is unambiguous and implementable.
- All schemas are valid JSON Schema draft-07.

---

## v2 — Core Implementation

**Goal**: Implement the first functional versions of Hermes inference and skill execution.

### Planned Deliverables
- [ ] Hermes inference engine (Python or TypeScript)
- [ ] Schema validation pipeline
- [ ] Cognitive profiling algorithm (rule-based v1)
- [ ] Emotional pattern recognizer
- [ ] Memory skill implementation
- [ ] Unit tests for all skills
- [ ] CI/CD pipeline
- [ ] Tribe v2 model integration

### Target
Q3 2026

---

## v3 — Learning & Adaptation

**Goal**: Enable Hermes to improve profiles over time and adapt to individual users.

### Planned Deliverables
- [ ] Session-level profile persistence (privacy-preserving)
- [ ] Feedback loop integration
- [ ] Multi-turn reasoning chains
- [ ] Tribe-level inference (group cognitive models)
- [ ] Evaluation benchmarks and accuracy metrics
- [ ] Developer SDK

### Target
Q1 2027

---

## Guiding Principles

1. **Human-first, not clinical**: Models always stay in the behavioral/cognitive domain.
2. **Privacy by design**: No raw data retention without explicit consent.
3. **Explainability**: Every output must have traceable evidence.
4. **Modularity**: Each model layer, skill, and workflow is independently replaceable.
