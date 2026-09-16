# Task 14.1 Validation — Python Cache Regression

**Date:** 2026-09-16  
**Status:** Local validation PASS; GitHub Actions platform revalidation pending push

## Root cause

Running the validator tests creates Python bytecode caches locally.

The repository `.gitignore` did not previously exclude:

```text
__pycache__/
*.pyc
*.pyo
```

As a result, two generated cache files were accidentally committed with Task 14.

## Fix

The repository now ignores generated Python caches globally:

```gitignore
__pycache__/
*.py[cod]
```

The single synthetic negative fixture under `tests/fixtures/generated-python-cache/` is explicitly allowlisted so it can remain versioned and prove the validator rejects this condition.

The validator also rejects tracked Python cache artifacts with:

```text
[GENERATED_ARTIFACT]
```

This provides defense in depth:

1. Git normally ignores the artifacts.
2. Static validation still fails if such a file is force-added or otherwise tracked.

## TDD evidence

A failing fixture/test was added first:

```text
tests/fixtures/generated-python-cache/
```

RED result:

```text
18 tests
1 failure
generated-python-cache unexpectedly passed
```

After implementing `GENERATED_ARTIFACT` detection:

```text
18 tests
0 failures
0 errors
```

## Repository cleanup required

The previously committed files must be removed from Git tracking:

```text
scripts/__pycache__/validate_repo.cpython-314.pyc
tests/__pycache__/test_validate_repo.cpython-314.pyc
```

Deleting them from the repository is safe because they are generated artifacts.

## GitHub Actions observation

The Task 14 push produced a GitHub Actions run with:

```text
conclusion: startup_failure
workflow name: empty
workflow path: BuildFailed
jobs: 0
```

No repository job, runner, checkout step, Python setup, test, or validator step started.

Therefore this correction does not change the workflow YAML as a speculative response to a failure that occurred before the job graph existed.

After this patch is pushed, inspect the new Actions run. If it again shows `BuildFailed` + `startup_failure` + zero jobs, record the CI layer as externally blocked while continuing to rely on local validator execution until GitHub Actions registration/dispatch recovers.
