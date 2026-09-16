---
type: daily-plan
schema_version: 1
id: task-w05-d04-php-runtime-and-fpm
week: 5
day: 4
date: null
track: core
skill_ids:
- composer-runtime
- environment-config
- agent-supervision
- repository-mapping
mode: HYBRID
estimated_minutes: 105
technology_depth: core
resource_ids:
- composer-basic-usage
- composer-schema
deliverables:
- frozen SOLO repository map
- agent map
- claim verification table
- config-risk note
review_policy: adaptive
prerequisites:
- week-04
status: planned
---

# Day 04 — Map Composer Bootstrap, Scripts, and Environment Configuration

## Outcome

> Understand the PHP web runtime from request arrival through FPM/process execution, configuration, Composer bootstrap, and application response.

## Timebox

| Block | Mode | Minutes |
|---|---|---:|
| SOLO repository map | `SOLO` | 25 |
| Agent repository map | `AI-ASSISTED` | 25 |
| Claim verification | `SOLO` | 20 |
| Config-risk note | `SOLO` | 15 |
| Daily micro-assessment | `SOLO` | 20 |
| **Total** |  | **105** |

Assessment time is included in this total.

## Resources

- `composer-basic-usage`
- `composer-schema`

Resource IDs resolve through `09 Resources/catalog.yaml`.

## Activities

### SOLO repository map — 25 min — `SOLO`

Map composer.json/lock, autoload bootstrap, scripts, environment/config loading, and runtime entry points. Freeze this map.

### Agent repository map — 25 min — `AI-ASSISTED`

Ask an agent to map the same repository read-only. Require file evidence for every claim.

### Claim verification — 20 min — `SOLO`

Check agent claims directly and label each verified, partially supported, or unsupported.

### Config-risk note — 15 min — `SOLO`

Identify one secrets/config boundary and one reproducibility risk.

### Daily micro-assessment — 20 min — `SOLO`

Complete the Composer/runtime transfer assessment.

## Deliverables

- frozen SOLO repository map
- agent map
- claim verification table
- config-risk note

## Daily assessment

Run `02 Daily Assessments/Week 05/Day 04.md`. Store learner attempts privately.

## Review hook

Create D+1/D+7 review events from demonstrated errors; add D+30 transfer review when justified.

## AI integrity

SOLO work remains independent evidence. HYBRID/AI-assisted work must preserve pre-agent evidence and independently validate consequential claims.

## Completion rule

Reading or agent conversation alone is not completion; required evidence must exist.
