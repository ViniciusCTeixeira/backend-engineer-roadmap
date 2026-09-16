---
type: diagnostic-day
schema_version: 1
day: 4
required: true
estimated_minutes: 145
domains:
- cakephp-depth
- laravel-familiarity
- docker
- aws-cloud
- cicd
status: planned
---

# Day 04 — Frameworks, Containers, Cloud, and Delivery

## Purpose

Execute the approved Week 0 diagnostic blocks for this day. This is evidence collection, not a pass/fail gate.

## Timebox

| Block | Mode | Minutes |
|---|---|---:|
| CakePHP depth/debugging | `SOLO` | 40 |
| Laravel transfer/familiarity | `SOLO` | 20 |
| Docker troubleshooting | `SOLO` | 30 |
| AWS/cloud architecture | `SOLO` | 30 |
| CI/CD pipeline review | `SOLO` | 25 |
| **Total** |  | **145** |

This day is required. Stop when the timebox expires rather than expanding the task indefinitely.

## Question IDs

- `diag-cakephp-001`
- `diag-cakephp-002`
- `diag-laravel-001`
- `diag-docker-001`
- `diag-aws-001`
- `diag-cicd-001`

Resolve each ID under `04 Question Bank/diagnostic/`.

## Assessment integrity

- SOLO means no LLM/coding-agent/search for solutions.
- HYBRID means preserve/freeze the first SOLO evidence before agent assistance.
- If help is needed during a SOLO assessment, mark that attempt `abandoned` before receiving teaching/solution help.
- Raw attempts are immutable after submission.
- Public question files contain no answer keys.

## Blocks

### CakePHP depth/debugging — 40 min — `SOLO`

Show lifecycle/ORM/debugging reasoning beyond routine CRUD usage.

Question IDs:
- `diag-cakephp-001`
- `diag-cakephp-002`
### Laravel transfer/familiarity — 20 min — `SOLO`

Map transferable concepts and clearly mark unfamiliar Laravel-specific mechanisms.

Question IDs:
- `diag-laravel-001`
### Docker troubleshooting — 30 min — `SOLO`

Diagnose layers/runtime/network/volume behavior from evidence.

Question IDs:
- `diag-docker-001`
### AWS/cloud architecture — 30 min — `SOLO`

Choose managed building blocks and explain reliability/security trade-offs.

Question IDs:
- `diag-aws-001`
### CI/CD pipeline review — 25 min — `SOLO`

Review a synthetic pipeline for correctness, feedback speed, deployment safety, and rollback.

Question IDs:
- `diag-cicd-001`

## Private evidence

For each scored evidence event, create a private record from:

`90 Templates/diagnostic-result.md`

Store it under `.study/assessments/diagnostic/` (or the equivalent documented private assessment location).

## Completion

The day is complete when the required raw attempts/evidence are stored privately, assistance is declared accurately, and confidence self-report is recorded for assessed domains.
