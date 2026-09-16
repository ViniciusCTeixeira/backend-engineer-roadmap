---
type: weekly-simulation
schema_version: 1
id: simulation-w05
week: 5
mode: SOLO
simulation_type: closed-technical
skill_ids:
- php-runtime
- php-fpm
- runtime-config
- composer-runtime
estimated_minutes: 75
status: planned
score_total: null
---

# Week 5 — PHP Runtime, FPM, and the Web Request Path Simulation

## Rules

- Follow the declared mode exactly.
- Preserve the first SOLO attempt before feedback or agent use.
- Do not search for a model solution during scored SOLO phases.
- Store responses privately under `.study/`.
- Grade using `docs/assessments.md`.

## Closed section — runtime reconstruction — 45 min
Without notes/search/agents: draw the Nginx → FPM → PHP request path, explain CLI vs FPM lifecycle assumptions, reason about a synthetic FPM pool under load, and explain Composer bootstrap/scripts.

## Evidence diagnosis — 20 min
Map three synthetic symptoms (wrong FastCGI target, pool saturation, application exception) to the next best evidence source.

## Transfer explanation — 10 min
Explain one way a runtime misconception can cause a misleading application-level diagnosis.

## Raw attempt — IMMUTABLE AFTER SUBMISSION

_Private learner record only._

## Assistance declaration

_Private learner record only._

## Grading dimensions

Use the approved assessment model and critical floors.

## Feedback

Append only after submission.

## Error records created

## Review events created

## Weekly adaptation recommendation

Use `docs/adaptive-learning.md`; never rewrite public curriculum from one learner result.

No solution/model answer is stored in the public roadmap.
