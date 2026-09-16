---
type: question-bank
schema_version: 1
bank: week-0-diagnostic
domain: aws-cloud
question_ids:
- diag-aws-001
answer_key_public: false
---

# AWS and Cloud — Week 0 Diagnostic

These prompts diagnose entry depth. They are not public teaching examples and contain no answer keys.

## `diag-aws-001`

| Field | Value |
|---|---|
| Domain | `aws-cloud` |
| Mode | `SOLO` |
| Assessment type | `system-design` |
| Difficulty | `diagnostic` |
| Estimated minutes | 30 |

### Prompt

Design a small highly available AWS deployment for a PHP API with MySQL-compatible storage and Redis-style caching.

You may use managed services you know, but the assessment is about reasoning, not service-name memorization.

Explain:
- public vs private network exposure;
- compute/runtime choice;
- database availability/backups;
- cache role/failure behavior;
- secrets/IAM boundaries;
- logs/metrics;
- one scaling bottleneck.

If you do not know a service name, describe the required capability instead of guessing.

### Submission rule

Store the raw attempt privately. Do not append a model answer to this public question.
