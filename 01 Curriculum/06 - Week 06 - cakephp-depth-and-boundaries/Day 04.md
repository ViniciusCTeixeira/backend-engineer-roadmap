---
type: daily-plan
schema_version: 1
id: task-w06-d04-cakephp-depth-and-boundaries
week: 6
day: 4
date: null
track: core
skill_ids:
- framework-conventions
- application-services
- design-tradeoffs
- testability
mode: SOLO
estimated_minutes: 105
technology_depth: core
resource_ids:
- cakephp-5-controllers
- cakephp-5-testing
deliverables:
- minimal redesign
- test plan
- do-not-abstract decision note
review_policy: adaptive
prerequisites:
- week-05
status: planned
---

# Day 04 — Use Framework Conventions Without Hiding Domain Logic

## Outcome

> Go beyond CakePHP CRUD by reasoning about request lifecycle, ORM behavior, framework conventions, and where application/domain logic should live.

## Timebox

| Block | Mode | Minutes |
|---|---|---:|
| Convention analysis | `SOLO` | 20 |
| Synthetic flow redesign | `SOLO` | 35 |
| Testability check | `SOLO` | 20 |
| Decision note | `SOLO` | 10 |
| Daily micro-assessment | `SOLO` | 20 |
| **Total** |  | **105** |

Assessment time is included in this total.

## Resources

- `cakephp-5-controllers`
- `cakephp-5-testing`

Resource IDs resolve through `09 Resources/catalog.yaml`.

## Activities

### Convention analysis — 20 min — `SOLO`

List what conventions buy you and where convention-heavy code can hide boundaries or coupling.

### Synthetic flow redesign — 35 min — `SOLO`

Redesign one fat-controller/fat-table scenario with the minimum additional application boundary.

### Testability check — 20 min — `SOLO`

Design characterization and focused tests that prove behavior before the boundary change.

### Decision note — 10 min — `SOLO`

Write a trade-off note: what you deliberately do not abstract.

### Daily micro-assessment — 20 min — `SOLO`

Complete the conventions/boundaries assessment.

## Deliverables

- minimal redesign
- test plan
- do-not-abstract decision note

## Daily assessment

Run `02 Daily Assessments/Week 06/Day 04.md`. Store learner attempts privately.

## Review hook

Create D+1/D+7 review events from demonstrated errors; add D+30 transfer review when justified.

## AI integrity

SOLO work remains independent evidence. HYBRID/AI-assisted work must preserve pre-agent evidence and independently validate consequential claims.

## Completion rule

Reading or agent conversation alone is not completion; required evidence must exist.
