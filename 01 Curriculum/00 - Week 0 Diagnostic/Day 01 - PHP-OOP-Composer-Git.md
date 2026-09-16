---
type: diagnostic-day
schema_version: 1
day: 1
required: true
estimated_minutes: 130
domains:
- php-language-runtime
- oop-design
- composer-dependencies
- git-github
status: planned
---

# Day 01 — PHP, OOP, Composer, and Git

## Purpose

Execute the approved Week 0 diagnostic blocks for this day. This is evidence collection, not a pass/fail gate.

## Timebox

| Block | Mode | Minutes |
|---|---|---:|
| Profile / confidence baseline | `SOLO` | 15 |
| PHP language/runtime | `SOLO` | 35 |
| OOP/design reasoning | `SOLO` | 30 |
| Composer/dependencies | `SOLO` | 20 |
| Git/GitHub | `SOLO` | 30 |
| **Total** |  | **130** |

This day is required. Stop when the timebox expires rather than expanding the task indefinitely.

## Question IDs

- `diag-php-runtime-001`
- `diag-php-runtime-002`
- `diag-oop-design-001`
- `diag-oop-design-002`
- `diag-composer-001`
- `diag-composer-002`
- `diag-git-001`
- `diag-git-002`

Resolve each ID under `04 Question Bank/diagnostic/`.

## Assessment integrity

- SOLO means no LLM/coding-agent/search for solutions.
- HYBRID means preserve/freeze the first SOLO evidence before agent assistance.
- If help is needed during a SOLO assessment, mark that attempt `abandoned` before receiving teaching/solution help.
- Raw attempts are immutable after submission.
- Public question files contain no answer keys.

## Blocks

### Profile / confidence baseline — 15 min — `SOLO`

Record prior exposure and confidence 0–100 for today's domains. This is self-report, not a score.
### PHP language/runtime — 35 min — `SOLO`

Complete the closed PHP prompts without documentation or agent help.

Question IDs:
- `diag-php-runtime-001`
- `diag-php-runtime-002`
### OOP/design reasoning — 30 min — `SOLO`

Reason from change pressure and substitutability; do not answer with pattern names alone.

Question IDs:
- `diag-oop-design-001`
- `diag-oop-design-002`
### Composer/dependencies — 20 min — `SOLO`

Complete dependency/lock/autoload reasoning.

Question IDs:
- `diag-composer-001`
- `diag-composer-002`
### Git/GitHub — 30 min — `SOLO`

Use only a disposable repository for destructive/recovery experiments.

Question IDs:
- `diag-git-001`
- `diag-git-002`

## Private evidence

For each scored evidence event, create a private record from:

`90 Templates/diagnostic-result.md`

Store it under `.study/assessments/diagnostic/` (or the equivalent documented private assessment location).

## Completion

The day is complete when the required raw attempts/evidence are stored privately, assistance is declared accurately, and confidence self-report is recorded for assessed domains.
