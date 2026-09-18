---
type: daily-plan
schema_version: 1
id: task-w11-d01-v1-1
week: 11
day: 1
date: null
track: core
skill_ids:
- transactions
- mvcc
- locking
- deadlocks
mode: SOLO
estimated_minutes: 105
technology_depth: core
resource_ids:
- mysql-innodb-transactions
- postgresql-mvcc
deliverables:
- transaction-boundary comparison
- two-session evidence
review_policy: adaptive
prerequisites:
- week-10
status: planned
---

# Day 01 — Define the Business Transaction Before Engine Mechanics

## Outcome

> Choose one multi-step invariant and implement explicit commit/rollback boundaries in MySQL and PostgreSQL.

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

- `mysql-innodb-transactions`
- `postgresql-mvcc`

## Activities

### Primary-source study — 20 min — `SOLO`

Read only the source sections needed to reason about the day's focus.

### Hands-on lab — 40 min — `SOLO`

Choose one multi-step invariant and implement explicit commit/rollback boundaries in MySQL and PostgreSQL.

### Project/evidence update — 15 min — `SOLO`

Connect the result to Project A/B or preserve a reproducible standalone artifact.

### Technical English — 10 min — `SOLO`

Explain one important decision, assumption, or failure mode in English.

### Daily assessment — 20 min — `SOLO`

Complete the scored transfer prompt without assistance.

## Deliverables

- transaction-boundary comparison
- two-session evidence

## Daily assessment

Run `02 Daily Assessments/Week 11/Day 01.md`. Store learner attempts privately.

## Review hook

Create D+1/D+7 reviews from demonstrated errors and D+30 transfer review when justified.

## AI integrity

Scored attempts are SOLO. HYBRID work preserves the first independent attempt before agent use.

## Completion rule

Reading or agent conversation alone is not completion; required evidence must exist.
