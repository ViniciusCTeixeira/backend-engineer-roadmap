---
type: daily-plan
schema_version: 1
id: task-w11-d02-mysql-transactions-locks-and-concurrency
week: 11
day: 2
date: null
track: core
skill_ids:
- mysql-transactions
- isolation
- locking
- deadlocks
mode: SOLO
estimated_minutes: 105
technology_depth: core
resource_ids:
- mysql-innodb-transactions
deliverables:
- isolation prediction matrix
- two-session observations
- assumption note
review_policy: adaptive
prerequisites:
- week-10
status: planned
---

# Day 02 — Reason About Isolation and MVCC

## Outcome

> Predict repeated-read/update behavior under selected isolation levels and verify with two sessions.

## Timebox

| Block | Mode | Minutes |
|---|---|---:|
| Primary-source study | `SOLO` | 20 |
| Hands-on reasoning / lab | `SOLO` | 40 |
| Project / evidence update | `SOLO` | 15 |
| Technical English / explanation | `SOLO` | 10 |
| Daily micro-assessment | `SOLO` | 20 |
| **Total** |  | **105** |

Assessment time is included.

## Resources

- `mysql-innodb-transactions`

Resource IDs resolve through `09 Resources/catalog.yaml`.

## Activities

### Primary-source study — 20 min — `SOLO`

Study the relevant primary source specifically for: Predict repeated-read/update behavior under selected isolation levels and verify with two sessions.

### Hands-on reasoning / lab — 40 min — `SOLO`

Predict repeated-read/update behavior under selected isolation levels and verify with two sessions.

### Project / evidence update — 15 min — `SOLO`

Connect the result to Project A/B or preserve a reproducible standalone artifact.

### Technical English / explanation — 10 min — `SOLO`

Explain one important decision, assumption, or failure mode in English.

### Daily micro-assessment — 20 min — `SOLO`

Complete the scored transfer prompt without assistance.

## Deliverables

- isolation prediction matrix
- two-session observations
- assumption note

## Daily assessment

Run `02 Daily Assessments/Week 11/Day 02.md`. Store learner attempts privately.

## Review hook

Create D+1/D+7 reviews from demonstrated errors; add D+30 transfer review when justified. Gate remediation is private and preserves the raw attempt.

## AI integrity

Scored attempts are SOLO. HYBRID activities freeze the SOLO baseline before agent use and require independent validation afterward.

## Completion rule

Reading or agent conversation alone is not completion; required evidence must exist.
