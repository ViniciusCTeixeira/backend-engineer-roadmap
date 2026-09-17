---
type: weekly-simulation
schema_version: 1
id: simulation-w32
week: 32
mode: SOLO
simulation_type: system-design
skill_ids:
- timeouts-retries
- cloudflare-waf-rate-limiting
- kubernetes-exposure
- helm-exposure
- argo-cd-gitops-exposure
estimated_minutes: 75
status: planned
score_total: null
---

# Week 32 — Resilience, Cloudflare WAF, Kubernetes/Helm, and GitOps Exposure Simulation

## Rules

- Follow the declared mode exactly.
- Preserve the first SOLO attempt before feedback or agent use.
- Do not search for a model solution during scored SOLO phases.
- Store learner responses privately under `.study/`.
- Grade using `docs/assessments.md` and critical floors where applicable.
- No public answer key is stored beside this simulation.

## Closed integrated scenario — 60 min

Solve/design/diagnose a scenario covering:

- Design edge/origin rate-limit and WAF boundaries
- Reason about timeout/retry budgets and failure amplification
- Map Docker Compose concepts to Kubernetes objects
- Inspect Helm values/templates in a bounded lab

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
