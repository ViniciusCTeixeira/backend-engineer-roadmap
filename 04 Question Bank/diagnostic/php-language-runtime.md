---
type: question-bank
schema_version: 1
bank: week-0-diagnostic
domain: php-language-runtime
question_ids:
- diag-php-runtime-001
- diag-php-runtime-002
answer_key_public: false
---

# PHP Language and Runtime — Week 0 Diagnostic

These prompts diagnose entry depth. They are not public teaching examples and contain no answer keys.

## `diag-php-runtime-001`

| Field | Value |
|---|---|
| Domain | `php-language-runtime` |
| Mode | `SOLO` |
| Assessment type | `conceptual` |
| Difficulty | `diagnostic` |
| Estimated minutes | 18 |

### Prompt

Without running code first, analyze the following PHP fragment. For every marked expression, predict the runtime value/type or failure and explain *why*.

```php
<?php
function takesInt(int $value): int {
    return $value;
}

$inputs = ["10", "10abc", 10.8, true, null];

foreach ($inputs as $input) {
    // Analyze the call behavior for each input.
    takesInt($input);
}
```

State assumptions about PHP version/configuration that materially affect your reasoning. After freezing your answer, you may run a local experiment and append observed evidence without editing the original prediction.

### Submission rule

Store the raw attempt privately. Do not append a model answer to this public question.

## `diag-php-runtime-002`

| Field | Value |
|---|---|
| Domain | `php-language-runtime` |
| Mode | `SOLO` |
| Assessment type | `coding-implementation` |
| Difficulty | `diagnostic` |
| Estimated minutes | 17 |

### Prompt

Design a **two-file** PHP experiment that tests what `declare(strict_types=1)` changes for scalar parameter calls.

Requirements:
- make a prediction before execution;
- include one caller/callee boundary;
- include at least two inputs;
- record what is controlled by the caller file;
- preserve prediction and observed result separately.

Do not look up the answer before the prediction is frozen.

### Submission rule

Store the raw attempt privately. Do not append a model answer to this public question.
