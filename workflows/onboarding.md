# Workflow: Onboarding

This workflow describes how a new user or session is onboarded into the HMIS model layer. Onboarding establishes the initial context that Hermes uses for the first inference cycle.

---

## Overview

```
New Session / New User
        │
        ▼
  [Collect Context]
        │
        ▼
  [Initialize Mind-State]
        │
        ▼
  [Invoke Reasoning Skill]  ──▶  initial cognitive style estimate
        │
        ▼
  [Invoke Empathy Skill]    ──▶  initial emotional register estimate
        │
        ▼
  [Emit Initial Mind-State]
```

---

## Steps

### 1. Collect Context

Gather available input signals at session start:

| Signal | Source | Required |
|--------|--------|----------|
| User locale | System metadata | No |
| Interaction domain | System metadata | No |
| Prior cognitive profile | Profile store | No |
| First turn text | User input | Yes |

### 2. Initialize Mind-State

Create a baseline `mind-state` object with all confidence values set to `0.0` and `low_confidence_flag: true`. This is the starting point before any inference.

```json
{
  "schema_version": "1.0.0",
  "session_id": "<generated>",
  "timestamp": "<now>",
  "confidence": 0.0,
  "low_confidence_flag": true,
  "cognitive": { "dominant_style": null },
  "emotional": { "dominant_pattern": null },
  "behavioral": { "dominant_tendency": null },
  "social": { "relational_pattern": null }
}
```

### 3. First-Turn Inference

After the first user turn, invoke:
1. **Reasoning Skill** → get initial cognitive style estimate
2. **Empathy Skill** → get initial emotional register estimate

Update mind-state with results. Flag remains `low_confidence` until session confidence exceeds 0.4.

### 4. Emit Initial Mind-State

Output the initialized mind-state JSON, validated against `schemas/mind-state.schema.json`.

---

## Exit Conditions

| Condition | Action |
|-----------|--------|
| Valid first turn received | Proceed to Inference workflow |
| No input after 3 prompts | Emit null mind-state, end session |
| Schema validation failure | Log error, retry with default values |
