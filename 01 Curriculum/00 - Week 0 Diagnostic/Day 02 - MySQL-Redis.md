---
type: diagnostic-day
schema_version: 1
day: 2
required: true
estimated_minutes: 135
domains:
- mysql-core
- redis-core
status: planned
---

# Day 02 — MySQL and Redis

## Purpose

Execute the approved Week 0 diagnostic blocks for this day. This is evidence collection, not a pass/fail gate.

## Timebox

| Block | Mode | Minutes |
|---|---|---:|
| MySQL modeling / SQL | `SOLO` | 35 |
| Indexes / EXPLAIN | `SOLO` | 35 |
| Transactions / locking | `SOLO` | 25 |
| Redis / caching / structures | `SOLO` | 40 |
| **Total** |  | **135** |

This day is required. Stop when the timebox expires rather than expanding the task indefinitely.

## Question IDs

- `diag-mysql-model-001`
- `diag-mysql-explain-001`
- `diag-mysql-tx-001`
- `diag-redis-001`
- `diag-redis-002`

Resolve each ID under `04 Question Bank/diagnostic/`.

## Assessment integrity

- SOLO means no LLM/coding-agent/search for solutions.
- HYBRID means preserve/freeze the first SOLO evidence before agent assistance.
- If help is needed during a SOLO assessment, mark that attempt `abandoned` before receiving teaching/solution help.
- Raw attempts are immutable after submission.
- Public question files contain no answer keys.

## Blocks

### MySQL modeling / SQL — 35 min — `SOLO`

Produce a schema/query design and explain trade-offs.

Question IDs:
- `diag-mysql-model-001`
### Indexes / EXPLAIN — 35 min — `SOLO`

Reason about access paths before proposing indexes.

Question IDs:
- `diag-mysql-explain-001`
### Transactions / locking — 25 min — `SOLO`

Analyze correctness and concurrency, not only syntax.

Question IDs:
- `diag-mysql-tx-001`
### Redis / caching / structures — 40 min — `SOLO`

Choose structures/caching behavior and discuss failure/invalidation trade-offs.

Question IDs:
- `diag-redis-001`
- `diag-redis-002`

## Private evidence

For each scored evidence event, create a private record from:

`90 Templates/diagnostic-result.md`

Store it under `.study/assessments/diagnostic/` (or the equivalent documented private assessment location).

## Completion

The day is complete when the required raw attempts/evidence are stored privately, assistance is declared accurately, and confidence self-report is recorded for assessed domains.
