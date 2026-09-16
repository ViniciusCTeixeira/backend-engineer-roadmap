---
type: question-bank
schema_version: 1
bank: week-0-diagnostic
domain: testing-static-analysis
question_ids:
- diag-testing-001
answer_key_public: false
---

# Testing and Static Analysis — Week 0 Diagnostic

These prompts diagnose entry depth. They are not public teaching examples and contain no answer keys.

## `diag-testing-001`

| Field | Value |
|---|---|
| Domain | `testing-static-analysis` |
| Mode | `HYBRID` |
| Assessment type | `coding-implementation` |
| Difficulty | `diagnostic` |
| Estimated minutes | 35 |

### Prompt

A legacy service has no direct tests and calls a repository plus an external mailer.

**Phase A — SOLO (minimum 20 min):**
- state the behavior you would protect first;
- propose a minimal test boundary;
- identify what should be real vs replaced/faked;
- write one representative test or detailed pseudocode;
- list one likely static-analysis issue worth checking.

Freeze this attempt.

**Phase B — agent critique (remaining time):**
Ask a coding agent to critique the test strategy only. Preserve its suggestions separately, then record which suggestions you accept/reject and why.

The first SOLO attempt remains the primary conceptual evidence.

### Submission rule

Store the raw attempt privately. Do not append a model answer to this public question.
