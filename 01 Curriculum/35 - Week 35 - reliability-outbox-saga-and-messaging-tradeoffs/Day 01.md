---
type: daily-plan
schema_version: 1
id: task-w35-d01-v1-1
week: 35
day: 1
date: null
track: core
skill_ids:
- outbox
- saga
- idempotency
- failure-modes
mode: SOLO
estimated_minutes: 105
technology_depth: core
resource_ids:
- builders-library
deliverables:
- dual-write timeline
- invariant list
review_policy: adaptive
prerequisites:
- week-34
status: planned
---

# Day 01 — Derive the Dual-Write Problem From a Real Workflow

## Outcome

> Model a PostgreSQL state change plus message/publication and show the inconsistent outcomes without an atomic strategy.

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

- `builders-library`

## Activities

### Primary-source study — 20 min — `SOLO`

Read only the sections required for the day's reasoning.

### Hands-on lab — 40 min — `SOLO`

Model a PostgreSQL state change plus message/publication and show the inconsistent outcomes without an atomic strategy.

### Project/evidence update — 15 min — `SOLO`

Connect the result to Project B or preserve reproducible standalone evidence.

### Technical English — 10 min — `SOLO`

Explain one decision/assumption/failure mode in English.

### Daily assessment — 20 min — `SOLO`

Complete the scored transfer prompt without assistance.

## Deliverables

- dual-write timeline
- invariant list

## Daily assessment

Run `02 Daily Assessments/Week 35/Day 01.md`. Store attempts privately.

## Review hook

Create D+1/D+7 reviews from demonstrated errors and D+30 transfer review where justified.

## AI integrity

Scored attempts are SOLO. HYBRID work preserves independent evidence before agent use.

## Completion rule

Required evidence must exist; reading or agent conversation alone is not completion.
