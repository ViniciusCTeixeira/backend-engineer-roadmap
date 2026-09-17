---
type: weekly-simulation
schema_version: 1
id: simulation-w37
week: 37
mode: HYBRID
simulation_type: coding-lab
skill_ids:
- function-calling
- tool-schemas
- authorization
- side-effects
- approval-boundaries
estimated_minutes: 75
status: planned
score_total: null
---

# Week 37 — LLM Tool Calling, Permissions, and Bounded Actions Simulation

## Rules

- Follow the declared mode exactly.
- Preserve the first SOLO attempt before feedback or agent use.
- Do not search for a model solution during scored SOLO phases.
- Store learner responses privately under `.study/`.
- Grade using `docs/assessments.md` and critical floors where applicable.
- No public answer key is stored beside this simulation.

## Phase A — SOLO baseline — 55 min

Solve/design/diagnose a scenario covering:

- Design narrow tool schemas from allowed business actions
- Validate tool arguments and reject unauthorized resource access
- Separate model proposal from application execution
- Implement human approval for consequential actions

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
