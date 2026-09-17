---
type: weekly-simulation
schema_version: 1
id: simulation-w40
week: 40
mode: HYBRID
simulation_type: ai-assisted
skill_ids:
- eval-datasets
- graders
- regression
- prompt-injection
- tool-security
estimated_minutes: 75
status: planned
score_total: null
---

# Week 40 — AI Evals, Security, Regression, and Production Quality Simulation

## Rules

- Follow the declared mode exactly.
- Preserve the first SOLO attempt before feedback or agent use.
- Do not search for a model solution during scored SOLO phases.
- Store learner responses privately under `.study/`.
- Grade using `docs/assessments.md` and critical floors where applicable.
- No public answer key is stored beside this simulation.

## Phase A — SOLO baseline — 55 min

Solve/design/diagnose a scenario covering:

- Define measurable success/failure for one AI feature
- Build a small versioned eval dataset with edge cases
- Run grading and inspect disagreements/failures
- Threat-model prompt/tool/retrieval attacks and permission bypasses

Freeze the complete baseline.

## Phase B — agent challenge — 10 min

Ask for one alternative, missing risk, or review. Do not allow unbounded edits.

## Phase C — independent review — 10 min

Accept/reject agent claims using evidence and explain the trade-off.

## Raw attempt — IMMUTABLE AFTER SUBMISSION

_Private learner record only._

## Assistance declaration

_Private learner record only._

## Feedback

Append only after submission.

## Error records created

## Review events created

## Weekly adaptation recommendation

Use `docs/adaptive-learning.md`; never rewrite public curriculum from one learner result.
