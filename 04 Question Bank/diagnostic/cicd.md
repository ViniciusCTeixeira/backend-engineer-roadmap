---
type: question-bank
schema_version: 1
bank: week-0-diagnostic
domain: cicd
question_ids:
- diag-cicd-001
answer_key_public: false
---

# CI/CD — Week 0 Diagnostic

These prompts diagnose entry depth. They are not public teaching examples and contain no answer keys.

## `diag-cicd-001`

| Field | Value |
|---|---|
| Domain | `cicd` |
| Mode | `SOLO` |
| Assessment type | `conceptual` |
| Difficulty | `diagnostic` |
| Estimated minutes | 25 |

### Prompt

Review this synthetic pipeline:

```text
push to main
  -> build image
  -> deploy production
  -> run unit tests
```

Identify problems and redesign the sequence.

Discuss:
- fast feedback before deployment;
- test/static-analysis placement;
- artifact immutability;
- environment configuration/secrets;
- deployment health verification;
- rollback/recovery.

Do not assume that a green deploy command means the release is healthy.

### Submission rule

Store the raw attempt privately. Do not append a model answer to this public question.
