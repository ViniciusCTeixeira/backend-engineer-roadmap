---
type: daily-plan
schema_version: 1
id: task-w06-d03-cakephp-depth-and-boundaries
week: 6
day: 3
date: null
track: core
skill_ids:
- cakephp-tables
- cakephp-entities
- domain-boundaries
- oop-design
mode: SOLO
estimated_minutes: 105
technology_depth: core
resource_ids:
- cakephp-5-orm
deliverables:
- responsibility classification
- minimal boundary sketch
- Project A smell entry
review_policy: adaptive
prerequisites:
- week-05
status: planned
---

# Day 03 — Separate Table, Entity, and Application Responsibilities

## Outcome

> Go beyond CakePHP CRUD by reasoning about request lifecycle, ORM behavior, framework conventions, and where application/domain logic should live.

## Timebox

| Block | Mode | Minutes |
|---|---|---:|
| Responsibility reading | `SOLO` | 20 |
| Boundary classification | `SOLO` | 35 |
| Refactor sketch | `SOLO` | 20 |
| Project smell inventory | `SOLO` | 10 |
| Daily micro-assessment | `SOLO` | 20 |
| **Total** |  | **105** |

Assessment time is included in this total.

## Resources

- `cakephp-5-orm`

Resource IDs resolve through `09 Resources/catalog.yaml`.

## Activities

### Responsibility reading — 20 min — `SOLO`

Review Table/Entity responsibilities and connect them to persistence vs domain behavior.

### Boundary classification — 35 min — `SOLO`

Classify validation, query, orchestration, transformation, and domain rules in a synthetic legacy flow.

### Refactor sketch — 20 min — `SOLO`

Sketch the smallest boundary change that makes one rule testable without inventing a full architecture.

### Project smell inventory — 10 min — `SOLO`

Record one concrete CakePHP-style legacy smell with file evidence.

### Daily micro-assessment — 20 min — `SOLO`

Complete the boundary assessment.

## Deliverables

- responsibility classification
- minimal boundary sketch
- Project A smell entry

## Daily assessment

Run `02 Daily Assessments/Week 06/Day 03.md`. Store learner attempts privately.

## Review hook

Create D+1/D+7 review events from demonstrated errors; add D+30 transfer review when justified.

## AI integrity

SOLO work remains independent evidence. HYBRID/AI-assisted work must preserve pre-agent evidence and independently validate consequential claims.

## Completion rule

Reading or agent conversation alone is not completion; required evidence must exist.
