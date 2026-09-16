---
type: question-bank
schema_version: 1
bank: week-0-diagnostic
domain: agentic-development
question_ids:
- diag-agentic-001
- diag-agentic-review-001
- diag-agentic-explain-001
answer_key_public: false
---

# Agentic Development — Week 0 Diagnostic

These prompts diagnose entry depth. They are not public teaching examples and contain no answer keys.

## `diag-agentic-001`

| Field | Value |
|---|---|
| Domain | `agentic-development` |
| Mode | `HYBRID` |
| Assessment type | `ai-assisted` |
| Difficulty | `diagnostic` |
| Estimated minutes | 50 |

### Prompt

Perform this task only inside a **private diagnostic sandbox**, never on public roadmap curriculum files.

Create a tiny PHP component with the following baseline:

```php
final class ShippingQuote
{
    public function calculate(int $weightGrams, bool $priority): int
    {
        if ($weightGrams <= 0) {
            return 0;
        }

        $base = 900;
        $weightFee = intdiv($weightGrams, 1000) * 250;

        return $priority
            ? $base + $weightFee + 600
            : $base + $weightFee;
    }
}
```

Change request:

> Reject invalid non-positive weight explicitly, preserve the existing public return type, add boundary tests around kilogram transitions, and keep the change narrowly scoped.

**Before agent use (SOLO):**
1. create the sandbox/baseline;
2. record your own implementation plan;
3. write expected invariants and test cases;
4. commit or otherwise preserve a baseline diff point.

**Then use Codex/Claude Code:**
- give bounded context;
- require tests;
- prohibit unrelated refactors;
- inspect every changed file.

Preserve the initial plan, full agent prompt/instructions, final diff, tests, and declared assistance privately.

### Submission rule

Store the raw attempt privately. Do not append a model answer to this public question.

## `diag-agentic-review-001`

| Field | Value |
|---|---|
| Domain | `agentic-development` |
| Mode | `SOLO` |
| Assessment type | `sql-debugging` |
| Difficulty | `diagnostic` |
| Estimated minutes | 25 |

### Prompt

Without asking the coding agent to explain its own work first, review the Day 6 generated diff.

Record:
- each changed file;
- intended behavior change;
- unrelated/scope-creep changes;
- missing/weak tests;
- edge cases;
- backward-compatibility risk;
- whether the implementation actually satisfies the request.

Run the tests/validation yourself. If there is no meaningful criticism, explain the evidence supporting that conclusion.

### Submission rule

Store the raw attempt privately. Do not append a model answer to this public question.

## `diag-agentic-explain-001`

| Field | Value |
|---|---|
| Domain | `agentic-development` |
| Mode | `SOLO` |
| Assessment type | `conceptual` |
| Difficulty | `diagnostic` |
| Estimated minutes | 20 |

### Prompt

From your own understanding, explain:
1. the two most consequential changes made by the agent;
2. one suggestion/change you accepted and why;
3. one change you rejected or would reject and why (if none occurred, identify a plausible scope-expanding change you would reject);
4. the independent evidence that makes you trust or distrust the final result.

Do not use the agent to compose this explanation.

### Submission rule

Store the raw attempt privately. Do not append a model answer to this public question.
