---
type: curriculum-week
schema_version: 1
week: 12
phase: Data and Web
estimated_minutes: 720
primary_outcome: "Use Redis by data model and failure mode rather than as a generic fast cache."
project_milestone: "legacy-redis + platform-data-model"
---

# Week 12 — Redis Data Modeling, Caching, Persistence, and Failure Modes

## Primary outcome

Use Redis by data model and failure mode rather than as a generic fast cache.

## Matrix alignment

Core topics:
- Redis data types
- TTL/eviction
- RDB/AOF
- cache-aside
- invalidation
- stampede/hot keys
- transactions/pipelining

Project milestone: `legacy-redis + platform-data-model`

Weekly simulation: `HYBRID` / `coding-lab`

English: Write an English cache-strategy ADR covering stale data and failure behavior.

AI/agent: Review agent cache advice only after defining source of truth, freshness, failure, and invalidation requirements.

Career: Create the first private evidence-based skills inventory against market demand.

## Planned workload

| Day | Minutes |
|---|---:|
| Day 01 | 105 |
| Day 02 | 105 |
| Day 03 | 105 |
| Day 04 | 105 |
| Day 05 | 105 |
| Day 06 | 135 |
| Day 07 | 60 |
| **Total** | **720 (12h)** |

Assessment time is already included.

## Primary resource IDs

- redis-data-types
- redis-persistence
- redis-eviction
- redis-transactions
- redis-pipelining

## Adaptation rule

This is a public baseline. Learner-specific remediation, reviews, scores, and future scheduling belong under `.study/`. A phase-gate failure preserves the original attempt and creates targeted private remediation rather than erasing history.
