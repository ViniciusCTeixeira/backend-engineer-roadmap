# Task 14 Validation — Static Repository Validator

**Date:** 2026-09-16  
**Status:** PASS — static validator approved; GitHub Actions execution externally blocked before job creation

## Scope

Add deterministic static validation before Weeks 5–52 are generated at scale.

## Implementation

Task 14 introduced:

```text
scripts/validate_repo.py
scripts/README.md
tests/test_validate_repo.py
tests/fixtures/
.github/workflows/validate.yml
```

The validator is standard-library-only and does not mutate the repository.

Implementation commit:

```text
c9cce5c518b69148e95427552ab0f754242fef4e
ci: validate roadmap repository invariants
```

Python-cache regression fix:

```text
195a915fcf79beb5781fd39c04d4eaad9d3a97ac
fix: keep generated python artifacts out of git
```

## TDD evidence

The validator was implemented test-first.

Initial RED:

```text
11 tests
11 failures
reason: validator missing
```

Additional RED/GREEN cycles covered:

- tracked `.study` data;
- invalid study mode;
- invalid technology depth;
- resource freshness metadata;
- duplicate canonical IDs;
- broken Markdown/Wikilinks;
- public answer-key leakage;
- historical raw-attempt/feedback separation;
- Obsidian local state;
- missing resource/question references;
- inline-code link false positives;
- generated Python cache artifacts.

Final local suite:

```text
18 tests
0 failures
0 errors
```

## Repository invariant coverage

| Invariant | Check |
|---|---|
| public `.study` file | `PRIVATE_TRACKED` |
| public link to `.study` | `PRIVATE_LINK` |
| missing required frontmatter | `MISSING_FRONTMATTER` |
| invalid study mode | `INVALID_MODE` |
| invalid technology depth | `INVALID_TECHNOLOGY_DEPTH` |
| broken internal Markdown/Wikilink | `BROKEN_LINK` |
| duplicate canonical ID | `DUPLICATE_ID` |
| resource missing/invalid `last_verified` | `RESOURCE_LAST_VERIFIED` |
| historical raw-attempt/feedback separation | `HISTORY_SEPARATION` |
| volatile Obsidian state | `OBSIDIAN_LOCAL_STATE` |
| unknown resource reference | `UNKNOWN_RESOURCE_ID` |
| unknown Week 0 question ID | `UNKNOWN_QUESTION_ID` |
| public answer key | `PUBLIC_ANSWER_KEY` |
| generated Python bytecode/cache | `GENERATED_ARTIFACT` |

## Repository cleanup revalidation

After Task 14.1:

```text
scripts/
├── README.md
└── validate_repo.py

tests/
├── fixtures/
└── test_validate_repo.py
```

The accidentally tracked runtime caches were removed:

```text
scripts/__pycache__/validate_repo.cpython-314.pyc
tests/__pycache__/test_validate_repo.cpython-314.pyc
```

The synthetic negative fixture under `tests/fixtures/generated-python-cache/` remains intentionally versioned.

Result: **PASS**

## GitHub Actions

The committed workflow remains:

```text
.github/workflows/validate.yml
```

and is designed to run:

1. checkout;
2. Python 3.12 setup;
3. validator tests;
4. repository validator.

### Run 1

```text
run: 35055206204
head: c9cce5c518b69148e95427552ab0f754242fef4e
conclusion: startup_failure
workflow name: empty
workflow path: BuildFailed
jobs: 0
```

### Run 2

```text
run: 35055576555
head: 195a915fcf79beb5781fd39c04d4eaad9d3a97ac
conclusion: startup_failure
workflow name: empty
workflow path: BuildFailed
jobs: 0
```

Both failures occurred before GitHub created a job graph. Therefore no repository step, runner, checkout, Python setup, unit test, or validator command executed.

The second run reproduced the same platform-layer signature after an unrelated repository correction without changing the workflow definition.

## Decision

Task 14's **static validator and repository invariants are approved**.

The GitHub Actions workflow is present but cannot currently be execution-validated because the hosting platform aborts the run before jobs exist.

This external CI condition does **not** block Task 15 generation. Until GitHub Actions starts creating jobs again:

```bash
python -m unittest discover -s tests -p "test_*.py" -v
python scripts/validate_repo.py
```

must be run locally after every curriculum batch.

The Actions integration remains an open external revalidation item and must be checked again before C7/V1 release.

## Conclusion

**Task 14 is approved for continuation to Task 15, with GitHub Actions execution explicitly marked as externally blocked and deferred for revalidation before C7.**
