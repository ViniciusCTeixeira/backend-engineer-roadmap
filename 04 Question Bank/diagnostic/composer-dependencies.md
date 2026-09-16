---
type: question-bank
schema_version: 1
bank: week-0-diagnostic
domain: composer-dependencies
question_ids:
- diag-composer-001
- diag-composer-002
answer_key_public: false
---

# Composer and Dependencies — Week 0 Diagnostic

These prompts diagnose entry depth. They are not public teaching examples and contain no answer keys.

## `diag-composer-001`

| Field | Value |
|---|---|
| Domain | `composer-dependencies` |
| Mode | `SOLO` |
| Assessment type | `conceptual` |
| Difficulty | `diagnostic` |
| Estimated minutes | 10 |

### Prompt

A repository commits `composer.lock`. A teammate runs `composer update` before every deployment, while another insists deployments should normally run `composer install`.

Explain the behavioral/reproducibility difference between the two commands and what evidence you would inspect in a dependency-change PR.

### Submission rule

Store the raw attempt privately. Do not append a model answer to this public question.

## `diag-composer-002`

| Field | Value |
|---|---|
| Domain | `composer-dependencies` |
| Mode | `SOLO` |
| Assessment type | `sql-debugging` |
| Difficulty | `diagnostic` |
| Estimated minutes | 10 |

### Prompt

A class `Acme\Billing\Invoice\Issuer` is expected to autoload through PSR-4, but PHP reports `Class not found`.

Write a diagnosis sequence that starts from `composer.json` and namespace/path mapping. Include the evidence you would gather before moving files or adding manual `require` statements.

### Submission rule

Store the raw attempt privately. Do not append a model answer to this public question.
