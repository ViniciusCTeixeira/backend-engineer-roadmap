---
type: daily-plan
schema_version: 1
id: task-w12-d02-redis-data-model-caching-and-failure-modes
week: 12
day: 2
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
- redis-eviction
- redis-data-types
deliverables:
- TTL decision table
- eviction failure analysis
- metrics note
review_policy: adaptive
prerequisites:
- week-11
status: planned
---

# Day 02 — Use TTL and Eviction Without Confusing Them

## Outcome

> Design TTLs, analyze memory-pressure eviction, and state metrics/signals before blaming cache misses.

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

- `redis-eviction`
- `redis-data-types`

Resource IDs resolve through `09 Resources/catalog.yaml`.

## Activities

### Primary-source study — 20 min — `SOLO`

Study the relevant primary source specifically for: Design TTLs, analyze memory-pressure eviction, and state metrics/signals before blaming cache misses.

### Hands-on reasoning / lab — 40 min — `SOLO`

Design TTLs, analyze memory-pressure eviction, and state metrics/signals before blaming cache misses.

### Project / evidence update — 15 min — `SOLO`

Connect the result to Project A/B or preserve a reproducible standalone artifact.

### Technical English / explanation — 10 min — `SOLO`

Explain one important decision, assumption, or failure mode in English.

### Daily micro-assessment — 20 min — `SOLO`

Complete the scored transfer prompt without assistance.

## Deliverables

- TTL decision table
- eviction failure analysis
- metrics note

## Daily assessment

Run `02 Daily Assessments/Week 12/Day 02.md`. Store learner attempts privately.

## Review hook

Create D+1/D+7 reviews from demonstrated errors; add D+30 transfer review when justified. Gate remediation is private and preserves the raw attempt.

## AI integrity

Scored attempts are SOLO. HYBRID activities freeze the SOLO baseline before agent use and require independent validation afterward.

## Completion rule

Reading or agent conversation alone is not completion; required evidence must exist.
