---
type: daily-plan
schema_version: 1
id: task-w27-d05-v1-1
week: 27
day: 5
date: null
track: core
skill_ids:
- aws-runtime
- rds-postgresql
- dynamodb
- autoscaling
mode: HYBRID
estimated_minutes: 105
technology_depth: core
resource_ids:
- aws-dynamodb-data-modeling
- aws-ec2-autoscaling
deliverables:
- RDS-vs-DynamoDB ADR
- scaling signal plan
- agent critique
review_policy: adaptive
prerequisites:
- week-26
status: planned
---

# Day 05 — Decide RDS vs DynamoDB and Scale Deliberately

## Outcome

> Challenge the DynamoDB candidate against PostgreSQL requirements, then model capacity/autoscaling signals and reject unjustified persistence duplication.

## Timebox

| Block | Mode | Minutes |
|---|---|---:|
| SOLO baseline | `SOLO` | 25 |
| Agent challenge | `AI-ASSISTED` | 20 |
| Independent validation | `SOLO` | 20 |
| Project evidence | `SOLO` | 20 |
| Daily assessment | `SOLO` | 20 |
| **Total** |  | **105** |

## Resources

- `aws-dynamodb-data-modeling`
- `aws-ec2-autoscaling`

## Activities

### SOLO baseline — 25 min — `SOLO`

Challenge the DynamoDB candidate against PostgreSQL requirements, then model capacity/autoscaling signals and reject unjustified persistence duplication. Freeze your first plan/evidence before agent use.

### Agent challenge — 20 min — `AI-ASSISTED`

Ask for critique/alternatives only; require assumptions.

### Independent validation — 20 min — `SOLO`

Verify consequential claims through code/tests/data/traces/primary sources.

### Project evidence — 20 min — `SOLO`

Apply only validated conclusions.

### Daily assessment — 20 min — `SOLO`

Complete the scored transfer prompt without assistance.

## Deliverables

- RDS-vs-DynamoDB ADR
- scaling signal plan
- agent critique

## Daily assessment

Run `02 Daily Assessments/Week 27/Day 05.md`. Store attempts privately.

## Review hook

Create D+1/D+7 reviews from demonstrated errors and D+30 transfer review where justified.

## AI integrity

Scored attempts are SOLO. HYBRID work preserves independent evidence before agent use.

## Completion rule

Required evidence must exist; reading or agent conversation alone is not completion.
