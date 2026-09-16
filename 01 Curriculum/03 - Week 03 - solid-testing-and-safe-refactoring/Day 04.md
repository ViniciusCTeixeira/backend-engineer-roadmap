---
type: daily-plan
schema_version: 1
id: task-w03-d04-solid-testing-and-safe-refactoring
week: 3
day: 4
date: null
track: core
skill_ids:
- characterization-testing
- legacy-safety
- test-boundaries
mode: SOLO
estimated_minutes: 105
technology_depth: core
resource_ids:
- cakephp-5-testing
- phpunit-writing-tests
deliverables:
- Project A characterization test
- behavior inventory
- untested-risk note
review_policy: adaptive
prerequisites:
- week-02
status: planned
---

# Day 04 — Characterization Tests Before Legacy Refactoring

## Outcome

Advance Week 3's primary outcome with observable evidence, not reading-only completion.

> Use SOLID and tests as feedback mechanisms to refactor behavior safely rather than applying patterns mechanically.

## Timebox

| Block | Mode | Minutes |
|---|---|---:|
| Testing reference | `SOLO` | 20 |
| Behavior inventory | `SOLO` | 25 |
| Characterization test | `SOLO` | 30 |
| Daily micro-assessment | `SOLO` | 20 |
| Evidence note | `SOLO` | 10 |
| **Total** |  | **105** |

Assessment time is included in this total.

## Resources

- `cakephp-5-testing`
- `phpunit-writing-tests`

Resource IDs resolve through `09 Resources/catalog.yaml`.

## Activities

### Testing reference — 20 min — `SOLO`

Review CakePHP/PHPUnit testing mechanisms relevant to the selected behavior.

### Behavior inventory — 25 min — `SOLO`

State current observable behavior, including one awkward behavior to preserve initially.

### Characterization test — 30 min — `SOLO`

Add a minimal test capturing current behavior before refactoring.

### Daily micro-assessment — 20 min — `SOLO`

Complete the characterization-test assessment.

### Evidence note — 10 min — `SOLO`

Record what the test proves and what remains untested.

## Deliverables

- Project A characterization test
- behavior inventory
- untested-risk note

## Daily assessment

Run `02 Daily Assessments/Week 03/Day 04.md`. Store the learner attempt privately.

## Review hook

Changing behavior while characterizing it is an implementation/validation error.

## Completion rule

The day is complete only when required evidence exists. Reading or agent conversation alone is not completion.
