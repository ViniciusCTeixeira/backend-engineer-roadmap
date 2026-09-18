---
type: daily-plan
schema_version: 1
id: task-w13-d04-v1-1
week: 13
day: 4
date: null
track: core
skill_ids:
- phase-gate-1
- mysql
- postgresql
- redis
mode: SOLO
estimated_minutes: 105
technology_depth: core
resource_ids:
- mysql-explain-manual
- postgresql-explain
- postgresql-mvcc
deliverables:
- plan/concurrency gate evidence
- transfer explanation
review_policy: adaptive
prerequisites:
- week-12
status: planned
---

# Day 04 — Closed Index/Transaction Transfer Case

## Outcome

> Interpret a query-plan/concurrency case and state which reasoning is portable versus engine-specific.

## Timebox

| Block | Mode | Minutes |
|---|---|---:|
| Primary-source study | `SOLO` | 20 |
| Hands-on lab | `SOLO` | 40 |
| Project/evidence update | `SOLO` | 15 |
| Technical English | `SOLO` | 10 |
| Daily assessment | `SOLO` | 20 |
| **Total** |  | **105** |

Assessment time is included.

## Resources

- `mysql-explain-manual`
- `postgresql-explain`
- `postgresql-mvcc`

## Activities

### Primary-source study — 20 min — `SOLO`

Read only the source sections needed to reason about the day's focus.

### Hands-on lab — 40 min — `SOLO`

Interpret a query-plan/concurrency case and state which reasoning is portable versus engine-specific.

### Project/evidence update — 15 min — `SOLO`

Connect the result to Project A/B or preserve a reproducible standalone artifact.

### Technical English — 10 min — `SOLO`

Explain one important decision, assumption, or failure mode in English.

### Daily assessment — 20 min — `SOLO`

Complete the scored transfer prompt without assistance.

## Deliverables

- plan/concurrency gate evidence
- transfer explanation

## Daily assessment

Run `02 Daily Assessments/Week 13/Day 04.md`. Store learner attempts privately.

## Review hook

Create D+1/D+7 reviews from demonstrated errors and D+30 transfer review when justified.

## AI integrity

Scored attempts are SOLO. HYBRID work preserves the first independent attempt before agent use.

## Completion rule

Reading or agent conversation alone is not completion; required evidence must exist.
