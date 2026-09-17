---
type: daily-plan
schema_version: 1
id: task-w10-d05-mysql-indexes-explain-and-benchmarking
week: 10
day: 5
date: null
track: core
skill_ids:
- mysql-indexes
- explain
- query-plans
- benchmarking
mode: HYBRID
estimated_minutes: 105
technology_depth: core
resource_ids:
- mysql-indexes-manual
- mysql-explain-manual
deliverables:
- frozen tuning plan
- agent candidate list
- validation/rejection evidence
review_policy: adaptive
prerequisites:
- week-09
status: planned
---

# Day 05 — Challenge Agent-Generated Index Advice

## Outcome

> Freeze your tuning plan, request agent candidates, independently test each, and reject unsupported/redundant indexes.

## Timebox

| Block | Mode | Minutes |
|---|---|---:|
| SOLO baseline | `SOLO` | 25 |
| Agent challenge | `AI-ASSISTED` | 20 |
| Independent validation | `SOLO` | 20 |
| Project / evidence update | `SOLO` | 20 |
| Daily micro-assessment | `SOLO` | 20 |
| **Total** |  | **105** |

Assessment time is included.

## Resources

- `mysql-indexes-manual`
- `mysql-explain-manual`

Resource IDs resolve through `09 Resources/catalog.yaml`.

## Activities

### SOLO baseline — 25 min — `SOLO`

Freeze your tuning plan, request agent candidates, independently test each, and reject unsupported/redundant indexes. Freeze your plan/findings before agent use.

### Agent challenge — 20 min — `AI-ASSISTED`

Ask for critique/alternatives only; require explicit assumptions and evidence.

### Independent validation — 20 min — `SOLO`

Verify or reject agent claims through primary sources, code, SQL, traces, tests, or measurements.

### Project / evidence update — 20 min — `SOLO`

Apply only validated conclusions to the project/evidence artifact.

### Daily micro-assessment — 20 min — `SOLO`

Complete the scored transfer prompt without assistance.

## Deliverables

- frozen tuning plan
- agent candidate list
- validation/rejection evidence

## Daily assessment

Run `02 Daily Assessments/Week 10/Day 05.md`. Store learner attempts privately.

## Review hook

Create D+1/D+7 reviews from demonstrated errors; add D+30 transfer review when justified. Gate remediation is private and preserves the raw attempt.

## AI integrity

Scored attempts are SOLO. HYBRID activities freeze the SOLO baseline before agent use and require independent validation afterward.

## Completion rule

Reading or agent conversation alone is not completion; required evidence must exist.
