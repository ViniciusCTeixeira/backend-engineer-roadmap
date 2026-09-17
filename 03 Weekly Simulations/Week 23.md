---
type: weekly-simulation
schema_version: 1
id: simulation-w23
week: 23
mode: SOLO
simulation_type: sql-debugging
skill_ids:
- nginx
- php-fpm
- fastcgi
- reverse-proxy
- health-checks
estimated_minutes: 75
status: planned
score_total: null
---

# Week 23 — Nginx, PHP-FPM, Reverse Proxy, and Production Request Path Simulation

## Rules

- Follow the declared mode exactly.
- Preserve the first SOLO attempt before feedback or agent use.
- Do not search for a model solution during scored SOLO phases.
- Store learner responses privately under `.study/`.
- Grade using `docs/assessments.md` and critical floors where applicable.
- No public answer key is stored beside this simulation.

## Closed integrated scenario — 60 min

Solve/design/diagnose a scenario covering:

- Build the Nginx→FPM request path
- Configure document root/front controller/FastCGI safely
- Reason about timeouts/body limits and upstream failure
- Correlate access/error/FPM logs

State assumptions and produce evidence or falsifiable validation steps.

## Transfer explanation — 15 min

Explain the key trade-off and one failure mode without notes or agent assistance.

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
