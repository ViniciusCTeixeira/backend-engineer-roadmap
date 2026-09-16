---
type: question-bank
schema_version: 1
bank: week-0-diagnostic
domain: english-technical
question_ids:
- diag-english-written-001
- diag-english-reading-001
- diag-english-spoken-001
answer_key_public: false
---

# Technical English — Week 0 Diagnostic

These prompts diagnose entry depth. They are not public teaching examples and contain no answer keys.

## `diag-english-written-001`

| Field | Value |
|---|---|
| Domain | `english-technical` |
| Mode | `SOLO` |
| Assessment type | `english-technical` |
| Difficulty | `diagnostic` |
| Estimated minutes | 20 |

### Prompt

Write **180–250 words in English** explaining a production bug you investigated (real but sanitized, or synthetic).

Include:
- symptom;
- initial hypothesis;
- evidence gathered;
- root cause;
- validation of the fix;
- one lesson learned.

Do not use translation/grammar-generation tools during the scored attempt.

### Submission rule

Store the raw attempt privately. Do not append a model answer to this public question.

## `diag-english-reading-001`

| Field | Value |
|---|---|
| Domain | `english-technical` |
| Mode | `SOLO` |
| Assessment type | `english-technical` |
| Difficulty | `diagnostic` |
| Estimated minutes | 20 |

### Prompt

Read the following passage, then answer in English without translation tools.

> A service uses retries for transient failures. The retry policy is effective for occasional network errors, but under sustained downstream failure it can amplify load and increase latency. The team adds exponential backoff, jitter, a retry budget, and metrics that distinguish first-attempt failures from retry outcomes. They also define which operations are safe to retry.

Questions:
1. What operational problem can retries create?
2. Why do backoff and jitter help?
3. Why must retry safety depend on the operation?
4. What metric would you want during an incident, and why?

### Submission rule

Store the raw attempt privately. Do not append a model answer to this public question.

## `diag-english-spoken-001`

| Field | Value |
|---|---|
| Domain | `english-technical` |
| Mode | `SOLO` |
| Assessment type | `english-technical` |
| Difficulty | `diagnostic` |
| Estimated minutes | 20 |

### Prompt

Record a **2–4 minute** spoken explanation in English:

> Explain how you would investigate a slow backend endpoint before optimizing it.

Cover evidence gathering, database/application/network possibilities, and how you would verify improvement.

Store the recording or private reference under `.study/`; do not commit personal audio to the public repository. No generated script may be read during the scored attempt.

### Submission rule

Store the raw attempt privately. Do not append a model answer to this public question.
