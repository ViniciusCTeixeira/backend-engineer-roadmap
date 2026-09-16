# Assessment and Scoring Model — C2-B

**Status:** C2-B candidate for review  
**Purpose:** Make assessment transparent enough that a learner or agent can reproduce why a score and adaptation were produced.

## 1. Scoring dimensions

All dimensions use `0–100`. A task type may give a dimension zero weight.

- **Factual correctness** — technical correctness of claims/answers.
- **Reasoning / explanation** — quality of causal reasoning, trade-offs, and ability to explain why.
- **Practical execution** — implementation/configuration/query/debugging outcome.
- **Validation / testing** — evidence that the learner verified behavior and considered failure/edge cases.
- **Communication** — clarity, structure, precision, and ability to state assumptions.
- **English quality** — comprehensibility and technical communication in English; only scored when explicitly part of the task.
- **AI supervision** — quality of delegation, constraints, review, verification, and rejection/correction of agent output; only for `HYBRID`/`AI-ASSISTED`.

A zero weight means the dimension is not part of that assessment; it is not equivalent to a score of zero.

## 2. Task-type weights

### Conceptual assessment

| Dimension | Weight |
|---|---:|
| Factual correctness | 50% |
| Reasoning / explanation | 30% |
| Practical execution | 0% |
| Validation / testing | 0% |
| Communication | 20% |
| English quality | 0% |
| AI supervision | 0% |

### Coding / implementation lab

| Dimension | Weight |
|---|---:|
| Factual correctness | 10% |
| Reasoning / explanation | 15% |
| Practical execution | 35% |
| Validation / testing | 30% |
| Communication | 10% |
| English quality | 0% |
| AI supervision | 0% |

### SQL / debugging lab

| Dimension | Weight |
|---|---:|
| Factual correctness | 15% |
| Reasoning / explanation | 25% |
| Practical execution | 30% |
| Validation / testing | 20% |
| Communication | 10% |
| English quality | 0% |
| AI supervision | 0% |

### System-design interview

| Dimension | Weight |
|---|---:|
| Factual correctness | 15% |
| Reasoning / explanation | 35% |
| Practical execution | 20% |
| Validation / testing | 15% |
| Communication | 15% |
| English quality | 0% |
| AI supervision | 0% |

Here `practical execution` means producing a coherent design, interfaces/data flow, and capacity/failure strategy; `validation` means challenging the design with bottlenecks/failure modes.

### AI-assisted engineering challenge

| Dimension | Weight |
|---|---:|
| Factual correctness | 10% |
| Reasoning / explanation | 15% |
| Practical execution | 25% |
| Validation / testing | 20% |
| Communication | 10% |
| English quality | 0% |
| AI supervision | 20% |

### English technical explanation

| Dimension | Weight |
|---|---:|
| Factual correctness | 20% |
| Reasoning / explanation | 20% |
| Practical execution | 0% |
| Validation / testing | 0% |
| Communication | 25% |
| English quality | 35% |
| AI supervision | 0% |

## 3. Total-score calculation

For the applicable task type:

```text
score_total = Σ(dimension_score × dimension_weight)
```

Weights are fractions whose sum is exactly `1.00`. Round the final value to the nearest integer only after summing.

Example SQL/debugging:

```text
correctness 80 × .15 = 12.00
reasoning   70 × .25 = 17.50
execution   85 × .30 = 25.50
validation  60 × .20 = 12.00
communication 80 × .10 = 8.00
--------------------------------
total = 75
```

## 4. Performance bands

These bands drive adaptation:

| Score | Default action |
|---|---|
| `>= 85` | reduce active repetition; retain spaced maintenance |
| `70–84` | keep planned load |
| `50–69` | targeted reinforcement + earlier review |
| `< 50` | recovery block before advanced dependent topics |

The total score is not the only signal. A critical prerequisite dimension may trigger remediation even if the weighted total is high.

Example: a coding lab with `validation < 50` creates a validation gap even if strong implementation produces `score_total >= 70`.

## 5. Critical-dimension floors

For tasks where the dimension applies:

- `validation < 50` on production/security/data-integrity tasks creates an active validation gap.
- `reasoning < 50` prevents declaring conceptual mastery.
- `ai_supervision < 50` prevents an AI-assisted task from supporting agentic-engineering mastery.
- `english_quality < 50` creates an English remediation item only when English was an explicit assessment goal.

## 6. Topic mastery evidence

Public curriculum progress and private topic mastery are different concepts.

### Mode-specific evidence

Maintain separate rolling scores:

```text
solo_score
hybrid_score
ai_assisted_score
```

Each is the arithmetic mean of the most recent **up to four qualifying evidence events** for that skill and mode.

### Demonstrated score used for mastery

Use this transparent hierarchy:

1. If at least **two recent SOLO evidence events** exist, `demonstrated_score = solo_score`.
2. Else if at least **one SOLO + one HYBRID** event exist, `demonstrated_score = mean(solo_score, hybrid_score)`.
3. Else if only HYBRID evidence exists, use `hybrid_score` but set `evidence_confidence: low`.
4. AI-ASSISTED evidence **never by itself** establishes conceptual mastery; it contributes to agentic/productivity competency instead.

This prevents an agent from substituting for knowledge.

### Evidence confidence

- `high`: at least 3 qualifying observations including 2 SOLO, across at least 2 different task types or dates.
- `medium`: at least 2 observations including 1 SOLO.
- `low`: less evidence or HYBRID-only evidence.

## 7. Confidence calibration

Learner self-report uses `0–100`.

Default flags:

- **overconfident:** self-report `>= 80` and demonstrated score `< 70`.
- **underconfident:** self-report `<= 50` and demonstrated score `>= 85`.
- **calibrated:** neither condition.

Overconfidence creates a metacognitive note and explanation-first review rather than merely more reading.

## 8. AI-dependence signal

Flag `ai-dependence` when both are true for the same skill:

1. `ai_assisted_score - solo_score >= 20`, and
2. `solo_score < 70`.

When there is insufficient SOLO evidence, create a SOLO reconstruction task rather than concluding dependence immediately.

## 9. Weekly simulations

Rotate among:

1. closed technical assessment;
2. coding/lab challenge;
3. agentic engineering challenge;
4. interview/system-design simulation.

A weekly simulation should sample cumulative material, not only the current week.

## 10. Monthly checkpoints and phase gates

Monthly checkpoints integrate multiple domains and project evidence.

Phase gates occur at Weeks 13, 26, 39, 52.

A failed gate:
- preserves the gate attempt;
- creates remediation;
- does not delete future curriculum;
- may delay dependent advanced private tasks;
- does not reset the learner to Week 1.

## 11. Abandonment and answer-key policy

An assessment is `abandoned` only after the learner explicitly chooses to stop the scored attempt.

After abandonment:
- answer/solution may be revealed;
- raw attempt remains preserved;
- the abandoned attempt does not count as successful mastery evidence;
- it may still create error/review records.

## 12. Regrading

Regrading corrects grading errors, not learner answers.

- Raw attempt never changes.
- Previous grade remains recorded.
- Corrected grade is appended.
- Aggregated metrics use the latest valid grade.
- Repeated regrades require human review of the rubric/process.

## 13. C2-B assessment acceptance criteria

- Every required task type has weights summing to 100%.
- SOLO/HYBRID/AI-ASSISTED evidence stays distinguishable.
- AI-assisted success cannot by itself establish conceptual mastery.
- Critical reasoning/validation failures can create gaps independently of total score.
- Answer keys remain hidden before submission/abandonment.
- Regrading preserves original evidence.
