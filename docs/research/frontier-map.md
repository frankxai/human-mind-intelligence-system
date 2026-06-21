# Frontier map

How the best current research grounds this System. The organizing idea: **intelligence as prediction**. This System predicts likely human responses from cognitive observations; frontier labs predict the next state of a world from a learned model. Same shape, different domain — and that shape is also how cognitive science increasingly describes the brain.

What follows is the honest version: where the parallel is real, and where it stops.

## 1. The prediction frame

The System's [response-prediction primitive](../response-prediction.md) takes labelled observations and emits *predicted responses with confidence and a falsifier* — never a diagnosis. Strip the domain and that is the same move a world model makes: from a current state, predict the next, carry uncertainty, correct on error. The rest of this map traces that move through three research lines.

## 2. World foundation models — predict in latent space

Yann LeCun's **A Path Towards Autonomous Machine Intelligence** (LeCun, 2022) reframes machine intelligence around a *world model* that predicts future **representations** in latent space rather than generating raw output. Meta built on it with **I-JEPA** (Assran et al., 2023) and the **V-JEPA / V-JEPA 2** video line (Bardes et al., 2024; Assran et al., 2025), predicting masked latent dynamics. NVIDIA's **Cosmos World Foundation Model Platform** (NVIDIA, 2025) trains large systems to understand, simulate, and predict physical environments. A 2024 [survey](https://arxiv.org/abs/2411.14499) maps the landscape and the prediction-vs-generation debate.

- LeCun (2022): https://arxiv.org/abs/2306.02572
- I-JEPA (Meta): https://ai.meta.com/blog/yann-lecun-ai-model-i-jepa/
- Cosmos WFM (NVIDIA, 2025): https://arxiv.org/abs/2501.03575
- World models survey (2024): https://arxiv.org/abs/2411.14499

**What we borrow:** predict in an abstract representation, carry uncertainty, learn from prediction error. **What we refuse:** autonomy. A world model acts; this System hands every decision to a human.

## 3. The predictive brain — the cognitive-science root

The same frame predates the AI work. **Predictive coding** (Rao & Ballard; Clark) casts the brain as a hierarchy minimizing prediction error. The **Bayesian brain / active inference** program (Friston) extends it to action: behavior is selected to minimize expected free energy, not to chase reward. Sprevak & Smith's **Introduction to Predictive Processing** (Topics in Cognitive Science, 2024) is a current synthesis across perception and decision-making.

- Predictive coding: https://en.wikipedia.org/wiki/Predictive_coding
- Bayesian brain / active inference: https://en.wikipedia.org/wiki/Bayesian_approaches_to_brain_function
- Sprevak & Smith (2024): https://onlinelibrary.wiley.com/doi/10.1111/tops.12704

This is why the schemas already carry `predictive-processing` as a lens, and why the `emotion → {attention, memory, motivation, decision-making}` edges read as affective modulation of a prediction system.

## 4. Affective computing — predicting emotion from content

The anchor named in the brief: **predicting emotional response to viewed content**. MIT work shows a [computational model](https://news.mit.edu/2023/computational-model-mimics-ability-predict-emotions-0605) that predicts others' emotional reactions from situation appraisal — appraisal theory made computational. Applied work [decodes viewer emotion elicited by video content](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11530461/). These ground the `emotion` construct's `appraisal-theory` and `dimensional-valence-arousal` lenses.

> **Boundary.** This is cited to ground the emotion *model*. It is not a feature, and this repo ships nothing that detects, scores, or profiles a person's emotions. Per [`../../CANON.md`](../../CANON.md), that boundary is non-waivable.

## 5. Theory of mind in models — the social-cognition frontier

Modeling other minds is the construct frontier labs probe most directly. Kosinski's **Evaluating LLMs in Theory of Mind Tasks** (PNAS, 2024) runs a false-belief battery on language models and reports GPT-4-class performance near older-child levels — treated here as a *measurement result with known training-contamination caveats*, not proof of mind. A 2025 [systematic review](https://arxiv.org/abs/2505.08245) surveys how mental-construct measurement is being applied to models, with validity caveats.

- Kosinski (2024): https://www.semanticscholar.org/paper/240001463c167d38766915d882f70ef6573c0454
- LLM psychometrics review (2025): https://arxiv.org/abs/2505.08245

## 6. What we borrow, what we refuse

| Borrowed from the frontier | Refused |
|---|---|
| Predict in a representation; carry confidence | Acting autonomously on the prediction |
| Learn from prediction error | Treating a model's output as ground truth about a person |
| Theory-of-mind as a modelable capacity | Claiming the System (or any model) *has* a mind |
| Appraisal/valence-arousal structure for emotion | Detecting or scoring a real person's emotions |

The through-line is genuine: this System is a small, non-clinical, human-owned cousin of the prediction paradigm. The discipline is the difference — five labelled stages, a falsifier on every reading, and a human at the decision.

Built on SIP.
