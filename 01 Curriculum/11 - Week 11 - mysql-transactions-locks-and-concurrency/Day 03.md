---
type: daily-plan
schema_version: 1
id: task-w11-d03-v1-1
week: 11
day: 3
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
- locking-read experiment
- index-lock note
review_policy: adaptive
prerequisites:
- week-10
status: planned
---

# Day 03 — Compare Locking Reads and Lock Scope

## Outcome

> Use indexed/non-indexed predicates to observe blocking/lock impact and separate SQL intent from implementation details.

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

Use indexed/non-indexed predicates to observe blocking/lock impact and separate SQL intent from implementation details.

### Project/evidence update — 15 min — `SOLO`

Connect the result to Project A/B or preserve a reproducible standalone artifact.

### Technical English — 10 min — `SOLO`

Explain one important decision, assumption, or failure mode in English.

### Daily assessment — 20 min — `SOLO`

Complete the scored transfer prompt without assistance.

## Deliverables

- locking-read experiment
- index-lock note

## Daily assessment

Run `02 Daily Assessments/Week 11/Day 03.md`. Store learner attempts privately.

## Review hook

Create D+1/D+7 reviews from demonstrated errors and D+30 transfer review when justified.

## AI integrity

Scored attempts are SOLO. HYBRID work preserves the first independent attempt before agent use.

## Completion rule

Reading or agent conversation alone is not completion; required evidence must exist.
