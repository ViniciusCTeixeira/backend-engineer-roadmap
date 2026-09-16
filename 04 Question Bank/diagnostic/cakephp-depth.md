---
type: question-bank
schema_version: 1
bank: week-0-diagnostic
domain: cakephp-depth
question_ids:
- diag-cakephp-001
- diag-cakephp-002
answer_key_public: false
---

# CakePHP Depth — Week 0 Diagnostic

These prompts diagnose entry depth. They are not public teaching examples and contain no answer keys.

## `diag-cakephp-001`

| Field | Value |
|---|---|
| Domain | `cakephp-depth` |
| Mode | `SOLO` |
| Assessment type | `conceptual` |
| Difficulty | `diagnostic` |
| Estimated minutes | 20 |

### Prompt

Describe the request-to-response path of a non-trivial CakePHP endpoint as you understand it.

Include the responsibilities of routing/controller/application or middleware layers, ORM/table/entity interaction, and response generation. Mark any lifecycle point you are unsure about instead of guessing.

### Submission rule

Store the raw attempt privately. Do not append a model answer to this public question.

## `diag-cakephp-002`

| Field | Value |
|---|---|
| Domain | `cakephp-depth` |
| Mode | `SOLO` |
| Assessment type | `sql-debugging` |
| Difficulty | `diagnostic` |
| Estimated minutes | 20 |

### Prompt

A CakePHP page became slow after a feature added associated data.

Describe how you would determine whether the issue is:
- N+1 queries;
- an inefficient join/eager-loading shape;
- hydration/application overhead;
- missing database indexes;
- something else.

List concrete evidence you would collect before changing ORM code.

### Submission rule

Store the raw attempt privately. Do not append a model answer to this public question.
