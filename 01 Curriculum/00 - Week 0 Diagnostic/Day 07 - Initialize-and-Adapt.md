---
type: diagnostic-day
schema_version: 1
day: 7
required: false
estimated_minutes: 90
domains: []
status: planned
---

# Day 07 — Initialize Evidence and Adapt Weeks 1–4

## Purpose

Execute the approved Week 0 diagnostic blocks for this day. This is evidence collection, not a pass/fail gate.

## Timebox

| Block | Mode | Minutes |
|---|---|---:|
| Validate private diagnostic records | `SOLO` | 20 |
| Create review events | `SOLO` | 20 |
| Build skill-state baseline | `SOLO` | 20 |
| Adapt Weeks 1–4 privately | `SOLO` | 20 |
| Sync private dashboard | `AI-ASSISTED` | 10 |
| **Total** |  | **90** |

This day is optional and contains no new graded diagnostic content.

## Question IDs

- No new graded questions; this day consolidates existing evidence.

Resolve each ID under `04 Question Bank/diagnostic/`.

## Assessment integrity

- SOLO means no LLM/coding-agent/search for solutions.
- HYBRID means preserve/freeze the first SOLO evidence before agent assistance.
- If help is needed during a SOLO assessment, mark that attempt `abandoned` before receiving teaching/solution help.
- Raw attempts are immutable after submission.
- Public question files contain no answer keys.

## Blocks

### Validate private diagnostic records — 20 min — `SOLO`

Confirm every submitted attempt exists under `.study/` and raw attempts are preserved.
### Create review events — 20 min — `SOLO`

Generate D+1/D+7 and justified D+30 events from actual errors/gaps.
### Build skill-state baseline — 20 min — `SOLO`

Aggregate demonstrated evidence by mode and confidence without inventing missing scores.
### Adapt Weeks 1–4 privately — 20 min — `SOLO`

Apply approved thresholds within the weekly ceiling; public curriculum remains unchanged.
### Sync private dashboard — 10 min — `AI-ASSISTED`

Use `sync-dashboard` after canonical private state has been updated.

## Private evidence

For each scored evidence event, create a private record from:

`90 Templates/diagnostic-result.md`

Store it under `.study/assessments/diagnostic/` (or the equivalent documented private assessment location).

## Completion

The day is complete when the required raw attempts/evidence are stored privately, assistance is declared accurately, and confidence self-report is recorded for assessed domains.
