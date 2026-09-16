---
type: question-bank
schema_version: 1
bank: week-0-diagnostic
domain: http-api-security
question_ids:
- diag-http-001
- diag-api-security-001
answer_key_public: false
---

# HTTP, APIs, and Security — Week 0 Diagnostic

These prompts diagnose entry depth. They are not public teaching examples and contain no answer keys.

## `diag-http-001`

| Field | Value |
|---|---|
| Domain | `http-api-security` |
| Mode | `SOLO` |
| Assessment type | `conceptual` |
| Difficulty | `diagnostic` |
| Estimated minutes | 30 |

### Prompt

Analyze this scenario:

A client sends `PUT /users/42/email` twice because the first response times out after the server may already have committed the change.

Explain:
- relevant HTTP semantics/idempotency considerations;
- what the client can and cannot infer from the timeout;
- how you would design the endpoint/response so retries are safe;
- which status/header/body evidence would be useful for diagnosis.

### Submission rule

Store the raw attempt privately. Do not append a model answer to this public question.

## `diag-api-security-001`

| Field | Value |
|---|---|
| Domain | `http-api-security` |
| Mode | `SOLO` |
| Assessment type | `system-design` |
| Difficulty | `diagnostic` |
| Estimated minutes | 30 |

### Prompt

Design a backend endpoint that lets an authenticated user download one of their private invoices.

Identify at least five risks or checks involving authentication, authorization/object ownership, input handling, information leakage, rate/abuse concerns, and transport/security assumptions.

Explain how you would test for an IDOR/BOLA-style authorization failure without relying on framework magic.

### Submission rule

Store the raw attempt privately. Do not append a model answer to this public question.
