---
type: daily-plan
schema_version: 1
id: task-w04-d04-debugging-and-git-recovery
week: 4
day: 4
date: null
track: core
skill_ids:
- git-revert
- git-reset
- git-reflog
- git-recovery
mode: SOLO
estimated_minutes: 105
technology_depth: core
resource_ids:
- git-pro-book
deliverables:
- recovery transcript
- Git safety checklist
- private assessment attempt
review_policy: adaptive
prerequisites:
- week-03
status: planned
---

# Day 04 — revert, reset, and reflog as Different Recovery Tools

## Outcome

Advance Week 4's primary outcome with observable evidence, not reading-only completion.

> Debug failures through hypotheses and evidence, use Git recovery safely, and demonstrate a reproducible Project A bug/root-cause report.

## Timebox

| Block | Mode | Minutes |
|---|---|---:|
| Recovery model | `SOLO` | 20 |
| Disposable recovery lab | `SOLO` | 40 |
| Safety checklist | `SOLO` | 15 |
| Daily micro-assessment | `SOLO` | 20 |
| Project hygiene | `SOLO` | 10 |
| **Total** |  | **105** |

Assessment time is included in this total.

## Resources

- `git-pro-book`

Resource IDs resolve through `09 Resources/catalog.yaml`.

## Activities

### Recovery model — 20 min — `SOLO`

Write what each tool changes: history, branch pointer, index/working tree, or recovery visibility.

### Disposable recovery lab — 40 min — `SOLO`

Create safe revert/reset/reflog recovery scenarios; narrate before executing.

### Safety checklist — 15 min — `SOLO`

Create a checklist for shared-history risk before destructive commands.

### Daily micro-assessment — 20 min — `SOLO`

Complete the recovery assessment.

### Project hygiene — 10 min — `SOLO`

Verify Project A working tree/branch is clean before debugging work.

## Deliverables

- recovery transcript
- Git safety checklist
- private assessment attempt

## Daily assessment

Run `02 Daily Assessments/Week 04/Day 04.md`. Store the learner attempt privately.

## Review hook

Unsafe command choice becomes a git-error review in a disposable repo.

## Completion rule

The day is complete only when required evidence exists. Reading or agent conversation alone is not completion.
