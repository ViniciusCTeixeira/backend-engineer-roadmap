---
type: daily-plan
schema_version: 1
id: task-w02-d04-oop-composer-and-boundaries
week: 2
day: 4
date: null
track: core
skill_ids:
- psr4
- autoloading
- namespaces
mode: SOLO
estimated_minutes: 105
technology_depth: core
resource_ids:
- composer-schema
deliverables:
- working/broken PSR-4 examples
- Project A autoload map
- private assessment attempt
review_policy: adaptive
prerequisites:
- week-01
status: planned
---

# Day 04 — PSR-4 Autoloading as a Mapping, Not Magic

## Outcome

Advance Week 2's primary outcome with observable evidence, not reading-only completion.

> Use OOP deliberately, reason about composition vs inheritance, and understand Composer/PSR-4/version constraints well enough to create a testable Project A boundary.

## Timebox

| Block | Mode | Minutes |
|---|---|---:|
| Reference reading | `SOLO` | 20 |
| Autoload lab | `SOLO` | 40 |
| Project A map | `SOLO` | 15 |
| Daily micro-assessment | `SOLO` | 20 |
| Explanation | `SOLO` | 10 |
| **Total** |  | **105** |

Assessment time is included in this total.

## Resources

- `composer-schema`

Resource IDs resolve through `09 Resources/catalog.yaml`.

## Activities

### Reference reading — 20 min — `SOLO`

Review Composer autoload/PSR-4 configuration.

### Autoload lab — 40 min — `SOLO`

Create two mappings, intentionally break one, diagnose it, then restore it.

### Project A map — 15 min — `SOLO`

Document Project A autoload roots/namespaces and one surprising mapping.

### Daily micro-assessment — 20 min — `SOLO`

Complete the autoloading assessment.

### Explanation — 10 min — `SOLO`

Explain namespace → prefix → path from memory.

## Deliverables

- working/broken PSR-4 examples
- Project A autoload map
- private assessment attempt

## Daily assessment

Run `02 Daily Assessments/Week 02/Day 04.md`. Store the learner attempt privately.

## Review hook

Trial-and-error-only diagnosis schedules D+1 mapping reconstruction.

## Completion rule

The day is complete only when required evidence exists. Reading or agent conversation alone is not completion.
