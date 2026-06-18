# Response Prediction

The response-prediction primitive is the System's reasoning move: given an observed
cognitive or affective state, produce **hypotheses about likely responses**, each
with confidence and evidence. It predicts; it never diagnoses.

This is the load-bearing safety boundary of the whole repo. Read it before using
the schemas to drive any agent behavior.

## The five-stage discipline

Every prediction passes through five labelled stages. The labels are not decoration
— they keep description, inference, and action from collapsing into one
unaccountable claim.

| Stage | Question | Schema home |
|---|---|---|
| **1. Observe** | What actually happened? | `observation` + `indicators` |
| **2. Interpret** | What might it mean? | `interpretation.hypothesis` + `lens` |
| **3. Hypothesize** | What response is likely next? | this doc — the prediction object |
| **4. Evidence** | What backs each step? | `interpretation.evidence`, `confidence`, `provenance` |
| **5. Decide** | What, if anything, do we do? | downstream — human-owned |

Stage 1 is fact. Stages 2–4 are explicitly tentative. Stage 5 is a human decision
that the System informs but does not make.

## What a prediction is

A prediction takes one or more **observation documents** (any of the twelve
[schemas](../schemas)) and emits likely responses. A response is a plausible next
state, action, or reaction — for example: "likely to defer the decision",
"likely to re-read rather than self-test", "likely to disengage from the task".

A prediction is always:

- **conditional** — "given this observed state, *if* conditions hold, *then* this
  response is more likely";
- **probabilistic** — every predicted response carries a confidence in `[0,1]`;
- **falsifiable** — phrased so a later observation can confirm or disconfirm it;
- **plural** — it lists alternatives, never a single forced answer;
- **traceable** — it points back to the observations and the ontology edges that
  license it.

## Shape of a prediction object

Not a JSON Schema in this version — a documented convention for agent output:

```json
{
  "from": [
    { "construct": "emotion", "observationRef": "obs-2026-06-18-001" },
    { "construct": "decision-making", "observationRef": "obs-2026-06-18-002" }
  ],
  "edge": "emotion modulates decision-making",
  "predictions": [
    {
      "response": "Likely to choose the certain, smaller option over the uncertain larger one.",
      "confidence": 0.55,
      "evidence": [
        "high-arousal indicator on the emotion observation",
        "risk-handling indicator on the decision observation",
        "prospect-theory lens: losses loom larger under arousal"
      ],
      "horizon": "next-decision",
      "falsifier": "Person chooses the larger uncertain option."
    },
    {
      "response": "Likely to defer the decision rather than choose now.",
      "confidence": 0.30,
      "evidence": ["task-switching observed earlier in session"],
      "horizon": "next-decision",
      "falsifier": "Person commits to an option within the session."
    }
  ],
  "abstainOnLowEvidence": true
}
```

Confidences across the prediction set do not need to sum to 1 — these are
competing hypotheses, not a partition. When evidence is thin, the correct output is
a single low-confidence prediction or an explicit abstention, not a confident guess.

## Hard rules

These are non-negotiable. They mirror the prime directive in
[`../CLAUDE.md`](../CLAUDE.md) and [`../CANON.md`](../CANON.md).

1. **Never diagnose.** No clinical category, disorder name, or treatment
   recommendation, ever — not as a prediction, not as a hypothesis, not as an
   aside. Predict responses, not conditions.
2. **Keep the stages separate.** An observation never carries an interpretation
   inline. A prediction always names which observations it derives from.
3. **Confidence in interpretation ≤ confidence in observation.** You cannot be
   more sure of what something means than that it happened.
4. **Carry at least one alternative** whenever confidence in the top prediction is
   below 0.7. A single confident reading of a person is a red flag.
5. **Abstain on thin evidence.** "Not enough signal to predict" is a valid and
   often correct output.
6. **The decision is human.** Stage 5 belongs to a person. The System surfaces
   predictions with their evidence; a human decides what to do.

## Worked example

**Observations**

- `attention`: "Re-read the same paragraph four times in five minutes." (confidence 0.85)
- `metacognition`: "Predicted full understanding, then could not summarize it." (confidence 0.8)

**Edge** — `metacognition reflects-on learning`, and attention gates memory/learning.

**Prediction**

> Likely to continue re-reading rather than switch to self-testing (confidence 0.5),
> because the metacognition observation shows a fluency illusion (predicted
> understanding exceeding demonstrated understanding) and the attention observation
> shows passive re-exposure. Alternative (confidence 0.3): likely to abandon the
> material entirely. Falsifier: person switches to active recall unprompted.

**Decision** — left to the human: e.g., a study-support agent might *offer* a recall
prompt, but the choice to act stays with the person. No claim is made about the
person's capacity, condition, or worth — only about a likely next move under stated
conditions.
