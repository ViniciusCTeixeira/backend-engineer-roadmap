---
type: question-bank
schema_version: 1
bank: week-0-diagnostic
domain: docker
question_ids:
- diag-docker-001
answer_key_public: false
---

# Docker — Week 0 Diagnostic

These prompts diagnose entry depth. They are not public teaching examples and contain no answer keys.

## `diag-docker-001`

| Field | Value |
|---|---|
| Domain | `docker` |
| Mode | `SOLO` |
| Assessment type | `sql-debugging` |
| Difficulty | `diagnostic` |
| Estimated minutes | 30 |

### Prompt

A PHP container works when built locally, but after a code change the running container still appears to use old application files.

Give a diagnosis plan that distinguishes:
- image/build-cache effects;
- bind mount/volume effects;
- wrong image/tag/container;
- process/runtime caching.

For each hypothesis, name the evidence you would inspect before rebuilding everything blindly.

### Submission rule

Store the raw attempt privately. Do not append a model answer to this public question.
