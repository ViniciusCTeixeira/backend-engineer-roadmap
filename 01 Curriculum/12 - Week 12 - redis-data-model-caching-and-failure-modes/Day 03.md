---
type: daily-plan
schema_version: 1
id: task-w12-d03-redis-data-model-caching-and-failure-modes
week: 12
day: 3
date: null
track: core
skill_ids:
- redis-data-types
- cache-aside
- ttl-eviction
- persistence
mode: SOLO
estimated_minutes: 105
technology_depth: core
resource_ids:
- redis-persistence
deliverables:
- state classification
- failure drill
- Project Redis recovery assumptions
review_policy: adaptive
prerequisites:
- week-11
status: planned
---

# Day 03 — Reason About RDB/AOF and Redis as Non-Authoritative State

## Outcome

> Classify Redis data by durability/rebuildability and define restart/data-loss/unavailability behavior.

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

- `redis-persistence`

Resource IDs resolve through `09 Resources/catalog.yaml`.

## Activities

### Primary-source study — 20 min — `SOLO`

Study the relevant primary source specifically for: Classify Redis data by durability/rebuildability and define restart/data-loss/unavailability behavior.

### Hands-on reasoning / lab — 40 min — `SOLO`

Classify Redis data by durability/rebuildability and define restart/data-loss/unavailability behavior.

### Project / evidence update — 15 min — `SOLO`

Connect the result to Project A/B or preserve a reproducible standalone artifact.

### Technical English / explanation — 10 min — `SOLO`

Explain one important decision, assumption, or failure mode in English.

### Daily micro-assessment — 20 min — `SOLO`

Complete the scored transfer prompt without assistance.

## Deliverables

- state classification
- failure drill
- Project Redis recovery assumptions

## Daily assessment

Run `02 Daily Assessments/Week 12/Day 03.md`. Store learner attempts privately.

## Review hook

Create D+1/D+7 reviews from demonstrated errors; add D+30 transfer review when justified. Gate remediation is private and preserves the raw attempt.

## AI integrity

Scored attempts are SOLO. HYBRID activities freeze the SOLO baseline before agent use and require independent validation afterward.

## Completion rule

Reading or agent conversation alone is not completion; required evidence must exist.
