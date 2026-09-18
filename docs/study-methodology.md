# Study Methodology

The roadmap is designed to turn familiarity into demonstrated engineering capability.

## Core learning loop

The default sequence is:

```text
theory
→ prediction
→ experiment / implementation
→ evidence
→ explanation
→ assessment
→ review
```

The important distinction is evidence.

Reading documentation, watching content, or receiving a good agent answer does not by itself prove that the learner can reason independently.

## Theory

Start with primary/official material.

The goal is not exhaustive reading. Read enough to form a causal model that can be tested.

## Prediction before execution

Before running a query, changing a configuration, asking an agent, or executing a debugging command, predict the expected behavior where practical.

Prediction exposes hidden assumptions.

## Experiment / practice

Use controlled exercises to falsify or strengthen the model.

Examples:

- PHP runtime experiments;
- SQL query/EXPLAIN experiments;
- two-session concurrency tests;
- failure injection;
- load tests;
- agent/tool permission tests;
- retrieval/eval cases.

## Project evidence

Learning is applied to cumulative projects rather than disconnected tutorial applications.

A useful milestone normally includes:

1. implementation or artifact;
2. validation/measurement;
3. explanation of trade-offs.

## Explanation

If you cannot explain the behavior, assumptions, alternatives, and evidence, the implementation is not yet strong evidence of understanding.

Technical English is integrated here rather than treated as a separate grammar course.

## Study modes

### SOLO

No LLM assistance during the independent/scored task.

Use SOLO for:

- conceptual calibration;
- closed assessments;
- phase gates;
- selected debugging/design tasks;
- algorithm/interview practice.

### HYBRID

1. work independently;
2. freeze the first attempt/plan;
3. use an agent;
4. compare;
5. validate;
6. record what changed in your understanding.

The first attempt is evidence and must not be overwritten.

### AI-ASSISTED

Agent use is expected.

You still own:

- requirements;
- acceptance criteria;
- validation;
- security/permission boundaries;
- final explanation.

AI-assisted evidence alone is not enough to establish conceptual mastery.

## Daily assessments

Daily assessments are intentionally short.

They test transfer/reasoning rather than only recall.

Public files contain prompts and grading structure. Real answers stay private.

## Weekly simulations

Weekly simulations rotate forms such as:

- closed technical assessment;
- coding lab;
- debugging incident;
- AI-supervised review;
- system design.

They integrate the week's concepts and project context.

## Phase gates

Phase gates occur at:

```text
Week 13
Week 26
Week 39
Week 52
```

Scored gate sections are SOLO.

A failed gate does not erase progress.

It creates private prerequisite-focused remediation before dependent advanced work.

## Scoring and adaptation

Default score response:

| Score | Default action |
|---:|---|
| 85–100 | reduce repetition; spaced maintenance |
| 70–84 | keep planned load |
| 50–69 | targeted practice and earlier review |
| below 50 | recovery before advanced dependencies |

Critical-dimension floors still apply.

A high total score does not compensate for a critical reasoning/execution/validation weakness where the rubric defines a floor.

## Reviews

Default spacing:

- **D+1** — explanation or small exercise;
- **D+7** — reconstruction/applied use;
- **D+30** — transfer/diagnosis in a different context.

Overdue important reviews take priority over optional new material.

## Error evidence

Repeated related errors matter more than one isolated mistake.

The adaptive model can raise priority when a pattern appears across separate assessments.

Error records are learning evidence, not something to hide.

## Workload

Default:

```text
12 hours / week
```

Generated weeks use seven days with lighter Day 7 review/career work.

Private adaptation may change future allocation while respecting the learner's configured ceiling.

## English

Technical English is practiced through real engineering outputs:

- design notes;
- incident explanations;
- PR/review comments;
- architecture presentations;
- interview answers;
- documentation reading.

## Career feedback

Market/interview feedback updates private preparation.

One vacancy or one interview does not rewrite the public curriculum.

Recurring signals may justify a formal public proposal.

## Related documents

- `docs/assessments.md`
- `docs/adaptive-learning.md`
- `docs/projects.md`
- `docs/career.md`
