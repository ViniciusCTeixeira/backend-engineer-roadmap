# Task 14.1 Validation — Python Cache Regression

**Date:** 2026-09-16  
**Status:** PASS — repository cleanup revalidated

## Root cause

Running Python tests created bytecode cache files locally, and the repository did not initially ignore them.

Two generated artifacts were accidentally tracked:

```text
scripts/__pycache__/validate_repo.cpython-314.pyc
tests/__pycache__/test_validate_repo.cpython-314.pyc
```

## Fix

The repository now ignores generated caches globally:

```gitignore
__pycache__/
*.py[cod]
```

The synthetic negative fixture is explicitly allowlisted so the validator can prove that a tracked cache artifact is rejected.

The validator now emits:

```text
[GENERATED_ARTIFACT]
```

for tracked `__pycache__`, `.pyc`, or `.pyo` content.

## TDD evidence

RED:

```text
18 tests
1 failure
generated-python-cache unexpectedly passed
```

GREEN:

```text
18 tests
0 failures
0 errors
```

## Repository revalidation

Correction commit:

```text
195a915fcf79beb5781fd39c04d4eaad9d3a97ac
fix: keep generated python artifacts out of git
```

The commit removed the two real generated `.pyc` files from the current repository tree.

Current `scripts/` contains only:

```text
README.md
validate_repo.py
```

Current `tests/` contains only the test source and fixtures at its top level; no runtime `__pycache__` remains.

The intentionally invalid fixture remains at:

```text
tests/fixtures/generated-python-cache/
```

Result: **PASS**

## GitHub Actions follow-up

The correction push produced run:

```text
35055576555
```

It again ended with:

```text
conclusion: startup_failure
path: BuildFailed
jobs: 0
```

No workflow job executed. This is tracked as an external GitHub Actions startup condition, not as a failure of the Python-cache correction.

## Conclusion

**Task 14.1 is approved.**
