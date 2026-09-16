---
type: daily-plan
schema_version: 1
id: task-w03-d02-solid-testing-and-safe-refactoring
week: 3
day: 2
date: null
track: core
skill_ids:
- solid-lsp
- solid-isp
- dependency-inversion
mode: SOLO
estimated_minutes: 105
technology_depth: core
resource_ids:
- php-oop-manual
deliverables:
- dependency-inversion example
- over-abstraction counterexample
- private assessment attempt
review_policy: adaptive
prerequisites:
- week-02
status: planned
---

# Day 02 — LSP, ISP, and Dependency Inversion

## Outcome

Advance Week 3's primary outcome with observable evidence, not reading-only completion.

> Use SOLID and tests as feedback mechanisms to refactor behavior safely rather than applying patterns mechanically.

## Timebox

| Block | Mode | Minutes |
|---|---|---:|
| Concept review | `SOLO` | 20 |
| Design lab | `SOLO` | 40 |
| Counterexample | `SOLO` | 15 |
| Daily micro-assessment | `SOLO` | 20 |
| Project planning | `SOLO` | 10 |
| **Total** |  | **105** |

Assessment time is included in this total.

## Resources

- `php-oop-manual`

Resource IDs resolve through `09 Resources/catalog.yaml`.

## Activities

### Concept review — 20 min — `SOLO`

Define substitutability, client-specific interfaces, and dependency direction.

### Design lab — 40 min — `SOLO`

Identify a concrete dependency and introduce the smallest useful abstraction in a toy example.

### Counterexample — 15 min — `SOLO`

Write one case where abstraction adds needless complexity.

### Daily micro-assessment — 20 min — `SOLO`

Complete the DIP/LSP/ISP assessment.

### Project planning — 10 min — `SOLO`

Relate the concepts to the approved Project A boundary without changing behavior.

## Deliverables

- dependency-inversion example
- over-abstraction counterexample
- private assessment attempt

## Daily assessment

Run `02 Daily Assessments/Week 03/Day 02.md`. Store the learner attempt privately.

## Review hook

Treating every concrete dependency as wrong schedules trade-off review.

## Completion rule

The day is complete only when required evidence exists. Reading or agent conversation alone is not completion.
