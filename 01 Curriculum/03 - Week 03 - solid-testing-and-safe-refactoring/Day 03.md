---
type: daily-plan
schema_version: 1
id: task-w03-d03-solid-testing-and-safe-refactoring
week: 3
day: 3
date: null
track: core
skill_ids:
- phpunit
- arrange-act-assert
- test-failures
mode: SOLO
estimated_minutes: 105
technology_depth: core
resource_ids:
- phpunit-writing-tests
deliverables:
- three PHPUnit tests
- deliberate-failure note
- private assessment attempt
review_policy: adaptive
prerequisites:
- week-02
status: planned
---

# Day 03 — PHPUnit Fundamentals and Failure Feedback

## Outcome

Advance Week 3's primary outcome with observable evidence, not reading-only completion.

> Use SOLID and tests as feedback mechanisms to refactor behavior safely rather than applying patterns mechanically.

## Timebox

| Block | Mode | Minutes |
|---|---|---:|
| Primary-source reading | `SOLO` | 25 |
| Test lab | `SOLO` | 35 |
| Failure-message review | `SOLO` | 15 |
| Daily micro-assessment | `SOLO` | 20 |
| English | `SOLO` | 10 |
| **Total** |  | **105** |

Assessment time is included in this total.

## Resources

- `phpunit-writing-tests`

Resource IDs resolve through `09 Resources/catalog.yaml`.

## Activities

### Primary-source reading — 25 min — `SOLO`

Read PHPUnit guidance on test classes, assertions, exception expectations, and failure behavior.

### Test lab — 35 min — `SOLO`

Write happy-path, invalid-input/exception, and edge-case tests for a tiny object; observe a deliberate failure.

### Failure-message review — 15 min — `SOLO`

Improve one test so its failure better communicates protected behavior.

### Daily micro-assessment — 20 min — `SOLO`

Complete the PHPUnit assessment.

### English — 10 min — `SOLO`

Explain Arrange/Act/Assert and exception expectations in English.

## Deliverables

- three PHPUnit tests
- deliberate-failure note
- private assessment attempt

## Daily assessment

Run `02 Daily Assessments/Week 03/Day 03.md`. Store the learner attempt privately.

## Review hook

Implementation without meaningful assertion creates validation-failure.

## Completion rule

The day is complete only when required evidence exists. Reading or agent conversation alone is not completion.
