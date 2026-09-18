---
type: daily-plan
schema_version: 1
id: task-w32-d05-v1-1
week: 32
day: 5
date: null
track: core
skill_ids:
- kubernetes
- resilience
- probes
- rollouts
mode: SOLO
estimated_minutes: 105
technology_depth: supporting
resource_ids:
- cloudflare-waf
- helm-quickstart
- argocd-getting-started
- builders-library
deliverables:
- resilience map
- Helm/Argo exposure note
review_policy: adaptive
prerequisites:
- week-31
status: planned
---

# Day 05 — Connect Edge Resilience and Keep Helm/Argo as Exposure

## Outcome

> Design timeout/retry/WAF boundaries, inspect a Helm values/template path and GitOps reconciliation concept, then state what remains outside Year-1 scope.

## Timebox

| Block | Mode | Minutes |
|---|---|---:|
| Primary-source study | `SOLO` | 20 |
| Hands-on lab | `SOLO` | 40 |
| Project/evidence update | `SOLO` | 15 |
| Technical English | `SOLO` | 10 |
| Daily assessment | `SOLO` | 20 |
| **Total** |  | **105** |

## Resources

- `cloudflare-waf`
- `helm-quickstart`
- `argocd-getting-started`
- `builders-library`

## Activities

### Primary-source study — 20 min — `SOLO`

Read only the sections required for the day's reasoning.

### Hands-on lab — 40 min — `SOLO`

Design timeout/retry/WAF boundaries, inspect a Helm values/template path and GitOps reconciliation concept, then state what remains outside Year-1 scope.

### Project/evidence update — 15 min — `SOLO`

Connect the result to Project B or preserve reproducible standalone evidence.

### Technical English — 10 min — `SOLO`

Explain one decision/assumption/failure mode in English.

### Daily assessment — 20 min — `SOLO`

Complete the scored transfer prompt without assistance.

## Deliverables

- resilience map
- Helm/Argo exposure note

## Daily assessment

Run `02 Daily Assessments/Week 32/Day 05.md`. Store attempts privately.

## Review hook

Create D+1/D+7 reviews from demonstrated errors and D+30 transfer review where justified.

## AI integrity

Scored attempts are SOLO. HYBRID work preserves independent evidence before agent use.

## Completion rule

Required evidence must exist; reading or agent conversation alone is not completion.
