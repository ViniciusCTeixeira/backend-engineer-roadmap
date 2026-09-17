---
type: weekly-simulation
schema_version: 1
id: simulation-w31
week: 31
mode: HYBRID
simulation_type: coding-lab
skill_ids:
- terraform-workflow
- state
- modules
- aws-provider
- cloudflare-provider
estimated_minutes: 75
status: planned
score_total: null
---

# Week 31 — Terraform: State, Modules, AWS/Cloudflare, and Secret Boundaries Simulation

## Rules

- Follow the declared mode exactly.
- Preserve the first SOLO attempt before feedback or agent use.
- Do not search for a model solution during scored SOLO phases.
- Store learner responses privately under `.study/`.
- Grade using `docs/assessments.md` and critical floors where applicable.
- No public answer key is stored beside this simulation.

## Phase A — SOLO baseline — 55 min

Solve/design/diagnose a scenario covering:

- Model desired state and Terraform plan/apply lifecycle
- Provision a bounded AWS resource set in code or safe sandbox
- Add a Cloudflare DNS/edge resource in Terraform
- Refactor repeated infrastructure into a small module

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
