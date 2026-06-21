# Attention — research grounding

> Non-clinical. This grounds the attention construct model. It does not profile, score, or diagnose a person.

## The model

Attention is the selective control of what gets processed. In the ontology it is the gate at the front of the pipeline: it gates memory and gates consciousness, deciding what reaches storage and what becomes reportable. Emotion modulates it — affect reweights what the system attends to.

## The prediction frame

Predictive processing recasts attention as precision-weighting: the brain up-weights the prediction errors it expects to be informative and damps the rest. Attention, on this view, is not a spotlight added on top of perception but a parameter inside the inference. The machine echo is JEPA's masked-prediction objective — a system learns by predicting the masked, salient part of its input. We borrow the framing of selective, prediction-driven gating; we do not claim the brain runs the algorithm.

## Anchors

- **Predictive coding / the predictive brain** — Rao & Ballard; Friston; Clark, review (1999). The brain as a prediction engine minimizing prediction error across a cortical hierarchy. The cognitive-science root of the prediction frame. [link](https://en.wikipedia.org/wiki/Predictive_coding)
- **An Introduction to Predictive Processing Models of Perception and Decision-Making** — Sprevak & Smith, Topics in Cognitive Science (2024). Accessible, current synthesis of predictive processing across perception and decision-making. [link](https://onlinelibrary.wiley.com/doi/10.1111/tops.12704)
- **I-JEPA: self-supervised learning by predicting in representation space** — Assran et al. (Meta FAIR), Meta AI (2023). First model on LeCun's vision; predicts abstract latent representations, not pixels. V-JEPA (Bardes et al. 2024) and V-JEPA 2 (Assran et al. 2025) extend the line to video dynamics. [link](https://ai.meta.com/blog/yann-lecun-ai-model-i-jepa/)

## Lens alignment

Schema lenses: `filter-model`, `attenuation`, `resource-model`, `selection-model`, `predictive-processing`. The two predictive-processing anchors inform the `predictive-processing` lens directly; I-JEPA is the engineering parallel for selection-as-prediction, loosely informing `selection-model`.

## Boundary

This grounds a model of selective processing. It does not license inferring a person's attentional capacity, focus, or distractibility from observed behavior.

Built on SIP.
