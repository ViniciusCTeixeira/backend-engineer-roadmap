---
type: question-bank
schema_version: 1
bank: week-0-diagnostic
domain: oop-design
question_ids:
- diag-oop-design-001
- diag-oop-design-002
answer_key_public: false
---

# OOP and Design Reasoning — Week 0 Diagnostic

These prompts diagnose entry depth. They are not public teaching examples and contain no answer keys.

## `diag-oop-design-001`

| Field | Value |
|---|---|
| Domain | `oop-design` |
| Mode | `SOLO` |
| Assessment type | `conceptual` |
| Difficulty | `diagnostic` |
| Estimated minutes | 15 |

### Prompt

A checkout service currently validates an order, calculates shipping, applies a promotion, persists the order, and sends a notification.

Identify the distinct reasons this component might change. Propose the **smallest** boundary changes you would make first and explain:
- what remains concrete;
- where an interface would or would not help;
- where composition is useful;
- one abstraction you would *not* introduce yet.

Reason from change pressure and testability, not from SOLID acronyms alone.

### Submission rule

Store the raw attempt privately. Do not append a model answer to this public question.

## `diag-oop-design-002`

| Field | Value |
|---|---|
| Domain | `oop-design` |
| Mode | `SOLO` |
| Assessment type | `conceptual` |
| Difficulty | `diagnostic` |
| Estimated minutes | 15 |

### Prompt

A subtype overrides a base method but rejects an input that the base contract accepts.

Explain why this can break callers. Give a concrete PHP example or pseudocode example, then propose a safer design. Include one case where inheritance would still be a reasonable choice.

### Submission rule

Store the raw attempt privately. Do not append a model answer to this public question.
