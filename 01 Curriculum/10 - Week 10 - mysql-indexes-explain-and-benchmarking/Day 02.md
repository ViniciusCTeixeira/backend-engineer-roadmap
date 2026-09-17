---
type: daily-plan
schema_version: 1
id: task-w10-d02-mysql-indexes-explain-and-benchmarking
week: 10
day: 2
date: null
track: core
skill_ids:
- mysql-indexes
- explain
- query-plans
- benchmarking
mode: SOLO
estimated_minutes: 105
technology_depth: core
resource_ids:
- mysql-indexes-manual
deliverables:
- candidate index matrix
- counterexample queries
- Project B index hypotheses
review_policy: adaptive
prerequisites:
- week-09
status: planned
---

# Day 02 — Design Composite Indexes From Query Shape

## Outcome

> Design candidate multi-column indexes for concrete WHERE/ORDER BY shapes and create counterexamples that show mismatches.

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

- `mysql-indexes-manual`

Resource IDs resolve through `09 Resources/catalog.yaml`.

## Activities

### Primary-source study — 20 min — `SOLO`

Study the relevant primary source specifically for: Design candidate multi-column indexes for concrete WHERE/ORDER BY shapes and create counterexamples that show mismatches.

### Hands-on reasoning / lab — 40 min — `SOLO`

Design candidate multi-column indexes for concrete WHERE/ORDER BY shapes and create counterexamples that show mismatches.

### Project / evidence update — 15 min — `SOLO`

Connect the result to Project A/B or preserve a reproducible standalone artifact.

### Technical English / explanation — 10 min — `SOLO`

Explain one important decision, assumption, or failure mode in English.

### Daily micro-assessment — 20 min — `SOLO`

Complete the scored transfer prompt without assistance.

## Deliverables

- candidate index matrix
- counterexample queries
- Project B index hypotheses

## Daily assessment

Run `02 Daily Assessments/Week 10/Day 02.md`. Store learner attempts privately.

## Review hook

Create D+1/D+7 reviews from demonstrated errors; add D+30 transfer review when justified. Gate remediation is private and preserves the raw attempt.

## AI integrity

Scored attempts are SOLO. HYBRID activities freeze the SOLO baseline before agent use and require independent validation afterward.

## Completion rule

Reading or agent conversation alone is not completion; required evidence must exist.
