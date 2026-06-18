# Workflow: Evaluation

This workflow describes how HMIS evaluates the quality and accuracy of Hermes inference outputs. Evaluation is a periodic process run against labeled or human-reviewed sessions.

---

## Overview

```
Evaluation Dataset (labeled sessions)
        │
        ▼
  [Run Inference Workflow]  ──▶  predicted mind-states
        │
        ▼
  [Compare to Ground Truth]
        │
        ▼
  [Compute Metrics]
        │
        ▼
  [Generate Evaluation Report]
        │
        ▼
  [Update Model Layer Calibration]
```

---

## Evaluation Dimensions

### 1. Schema Conformance

**Metric**: % of outputs that pass JSON schema validation without errors.

**Target**: 100% (hard requirement — non-conformant outputs are a bug).

### 2. Cognitive Style Accuracy

**Metric**: Agreement rate between Hermes-inferred `dominant_style` and human-labeled ground truth.

**Baseline target (v1 rule-based)**: > 65% agreement.

| Label | Method |
|-------|--------|
| Ground truth | Human reviewer labels sessions using cognitive style definitions in `models/cognitive/README.md` |
| Inference | Hermes Reasoning skill output |

### 3. Emotional Pattern Accuracy

**Metric**: Agreement rate between Hermes-inferred `dominant_pattern` and human-labeled ground truth.

**Baseline target (v1)**: > 60% agreement.

### 4. Confidence Calibration

**Metric**: Calibration curve comparing confidence scores to actual accuracy.

A well-calibrated model should produce ~70% accuracy on turns where confidence ≈ 0.7.

### 5. Guardrail Compliance

**Metric**: % of outputs containing zero clinical labels (DSM/ICD codes or clinical diagnoses).

**Target**: 100% — any violation is a critical failure.

**Check**: Automated scan of output for prohibited terms list.

---

## Evaluation Dataset Requirements

| Requirement | Value |
|-------------|-------|
| Minimum sessions | 50 |
| Minimum turns per session | 5 |
| Labeler agreement threshold | ≥ 0.7 Cohen's kappa |
| Data anonymization | Required before evaluation |

---

## Evaluation Report Format

```yaml
evaluation_report:
  date: ISO8601
  dataset_version: string
  session_count: integer
  turn_count: integer
  metrics:
    schema_conformance: float      # 0.0–1.0
    cognitive_style_accuracy: float
    emotional_pattern_accuracy: float
    confidence_calibration_score: float
    guardrail_compliance: float
  failures:
    schema_failures: integer
    guardrail_violations: integer
    notes: string
  recommendations:
    - string
```

---

## Evaluation Cadence

| Phase | Cadence |
|-------|---------|
| v1 (Foundation) | Manual, on-demand |
| v2 (Implementation) | Per release |
| v3 (Adaptive) | Continuous, automated |
