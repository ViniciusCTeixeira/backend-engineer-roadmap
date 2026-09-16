---
type: question-bank
schema_version: 1
bank: week-0-diagnostic
domain: git-github
question_ids:
- diag-git-001
- diag-git-002
answer_key_public: false
---

# Git and GitHub — Week 0 Diagnostic

These prompts diagnose entry depth. They are not public teaching examples and contain no answer keys.

## `diag-git-001`

| Field | Value |
|---|---|
| Domain | `git-github` |
| Mode | `SOLO` |
| Assessment type | `conceptual` |
| Difficulty | `diagnostic` |
| Estimated minutes | 15 |

### Prompt

In a disposable repository, create:
1. one modified but unstaged file;
2. one staged change;
3. one committed change.

Capture the relevant status/diff/log evidence and explain the difference among working tree, index, and commit history.

### Submission rule

Store the raw attempt privately. Do not append a model answer to this public question.

## `diag-git-002`

| Field | Value |
|---|---|
| Domain | `git-github` |
| Mode | `SOLO` |
| Assessment type | `sql-debugging` |
| Difficulty | `diagnostic` |
| Estimated minutes | 15 |

### Prompt

Consider two recovery cases:

**A.** A bad commit is already pushed to a shared branch.  
**B.** You accidentally moved the pointer of an unshared local branch and want to recover the previous commit.

For each case, explain which Git recovery mechanism you would investigate first (`revert`, `reset`, `reflog`, or another specific mechanism), why, and what you would verify before executing it. Use a disposable repository for any command experiment.

### Submission rule

Store the raw attempt privately. Do not append a model answer to this public question.
