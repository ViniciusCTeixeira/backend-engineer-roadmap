---
type: daily-plan
schema_version: 1
id: task-w32-d03-v1-1
week: 32
day: 3
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
- kubernetes-application-basics
deliverables:
- probe design
- failure experiment
review_policy: adaptive
prerequisites:
- week-31
status: planned
---

# Day 03 — Design Readiness and Liveness for Real Failure Modes

## Outcome

> Implement/plan probes that distinguish startup/readiness from process deadlock without making every dependency a liveness condition.

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

- `kubernetes-application-basics`

## Activities

### Primary-source study — 20 min — `SOLO`

Read only the sections required for the day's reasoning.

### Hands-on lab — 40 min — `SOLO`

Implement/plan probes that distinguish startup/readiness from process deadlock without making every dependency a liveness condition.

### Project/evidence update — 15 min — `SOLO`

Connect the result to Project B or preserve reproducible standalone evidence.

### Technical English — 10 min — `SOLO`

Explain one decision/assumption/failure mode in English.

### Daily assessment — 20 min — `SOLO`

Complete the scored transfer prompt without assistance.

## Deliverables

- probe design
- failure experiment

## Daily assessment

Run `02 Daily Assessments/Week 32/Day 03.md`. Store attempts privately.

## Review hook

Create D+1/D+7 reviews from demonstrated errors and D+30 transfer review where justified.

## AI integrity

Scored attempts are SOLO. HYBRID work preserves independent evidence before agent use.

## Completion rule

Required evidence must exist; reading or agent conversation alone is not completion.
