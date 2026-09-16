---
type: question-bank
schema_version: 1
bank: week-0-diagnostic
domain: redis-core
question_ids:
- diag-redis-001
- diag-redis-002
answer_key_public: false
---

# Redis Core — Week 0 Diagnostic

These prompts diagnose entry depth. They are not public teaching examples and contain no answer keys.

## `diag-redis-001`

| Field | Value |
|---|---|
| Domain | `redis-core` |
| Mode | `SOLO` |
| Assessment type | `conceptual` |
| Difficulty | `diagnostic` |
| Estimated minutes | 20 |

### Prompt

Choose an appropriate Redis structure/approach for each scenario and justify it:
1. per-user rate-limit counters with expiry;
2. a leaderboard ordered by score;
3. a short-lived session/cache entry;
4. a deduplication marker for a recently processed message.

For each, state TTL/cleanup considerations and one failure mode.

### Submission rule

Store the raw attempt privately. Do not append a model answer to this public question.

## `diag-redis-002`

| Field | Value |
|---|---|
| Domain | `redis-core` |
| Mode | `SOLO` |
| Assessment type | `system-design` |
| Difficulty | `diagnostic` |
| Estimated minutes | 20 |

### Prompt

An API caches product details in Redis for 10 minutes. Product updates must become visible quickly, but the cache may be unavailable.

Propose a caching strategy covering:
- cache-aside/read behavior;
- invalidation/update behavior;
- stale data trade-offs;
- what happens when Redis is down;
- how you avoid a thundering-herd problem for a hot key.

Do not assume Redis is the source of truth.

### Submission rule

Store the raw attempt privately. Do not append a model answer to this public question.
