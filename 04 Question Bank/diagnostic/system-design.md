---
type: question-bank
schema_version: 1
bank: week-0-diagnostic
domain: system-design
question_ids:
- diag-system-design-001
answer_key_public: false
---

# System Design — Week 0 Diagnostic

These prompts diagnose entry depth. They are not public teaching examples and contain no answer keys.

## `diag-system-design-001`

| Field | Value |
|---|---|
| Domain | `system-design` |
| Mode | `SOLO` |
| Assessment type | `system-design` |
| Difficulty | `diagnostic` |
| Estimated minutes | 45 |

### Prompt

Design a backend for a webhook ingestion service.

Assume:
- external providers can send duplicate events;
- bursts can reach 500 requests/second;
- processing can take several seconds;
- providers retry on timeout/failure;
- users need to inspect processing status.

Cover:
- API boundary;
- persistence;
- idempotency/deduplication;
- asynchronous processing;
- retry/dead-letter behavior;
- observability;
- basic capacity assumptions;
- one consistency trade-off;
- at least three failure modes and how the system responds.

Use technology names only when they support the reasoning.

### Submission rule

Store the raw attempt privately. Do not append a model answer to this public question.
