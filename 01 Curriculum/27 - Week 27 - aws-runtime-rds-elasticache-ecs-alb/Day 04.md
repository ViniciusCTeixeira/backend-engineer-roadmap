---
type: daily-plan
schema_version: 1
id: task-w27-d04-v1-1
week: 27
day: 4
date: null
track: core
skill_ids:
- aws-runtime
- rds-postgresql
- dynamodb
- autoscaling
mode: SOLO
estimated_minutes: 105
technology_depth: core
resource_ids:
- aws-dynamodb-data-modeling
deliverables:
- access-pattern table
- DynamoDB key/GSI design
review_policy: adaptive
prerequisites:
- week-26
status: planned
---

# Day 04 — Design DynamoDB From Access Patterns

## Outcome

> List reads/writes first, then choose partition/sort keys and one GSI; test for high-cardinality distribution and hot-key risk.

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

- `aws-dynamodb-data-modeling`

## Activities

### Primary-source study — 20 min — `SOLO`

Read only the sections required for the day's reasoning.

### Hands-on lab — 40 min — `SOLO`

List reads/writes first, then choose partition/sort keys and one GSI; test for high-cardinality distribution and hot-key risk.

### Project/evidence update — 15 min — `SOLO`

Connect the result to Project B or preserve reproducible standalone evidence.

### Technical English — 10 min — `SOLO`

Explain one decision/assumption/failure mode in English.

### Daily assessment — 20 min — `SOLO`

Complete the scored transfer prompt without assistance.

## Deliverables

- access-pattern table
- DynamoDB key/GSI design

## Daily assessment

Run `02 Daily Assessments/Week 27/Day 04.md`. Store attempts privately.

## Review hook

Create D+1/D+7 reviews from demonstrated errors and D+30 transfer review where justified.

## AI integrity

Scored attempts are SOLO. HYBRID work preserves independent evidence before agent use.

## Completion rule

Required evidence must exist; reading or agent conversation alone is not completion.
