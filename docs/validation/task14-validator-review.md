# Task 14 Validation — Static Repository Validator

**Date:** 2026-09-16  
**Status:** Local package validation PASS; repository/CI validation pending commit/push

## Scope

Add deterministic static validation before Weeks 5–52 are generated at scale.

## Architecture

```text
tests/fixtures/
      │
      ▼
tests/test_validate_repo.py
      │
      ▼
scripts/validate_repo.py
      │
      ├── local execution
      └── GitHub Actions
```

The validator is standard-library-only and does not mutate the repository.

## TDD evidence

The initial test suite was written before the validator existed.

Initial RED state:

```text
11 tests
11 failures
reason: validator missing
```

During GREEN, the suite exposed two normalization defects involving leading-dot paths (`.study` and `.obsidian`). Those defects were corrected before proceeding.

Additional safety contracts were then introduced with a second RED cycle for:

- tracked `.study` content;
- invalid frontmatter `technology_depth`;
- invalid resource `technology_depth`;
- public `answer_key_public: true`;
- public `## Solution` / `## Answer Key` headings.

A link-scanner regression test was added after final integration exposed an inline-code false positive. The final suite size is:

```text
17 tests
0 failures
0 errors
```

Fresh final verification:

```text
python -m py_compile scripts/validate_repo.py
  PASS

python -m unittest discover -s tests -p 'test_*.py' -v
  Ran 17 tests
  OK

python scripts/validate_repo.py
  Validation passed: 0 errors.
```

## Required invariant coverage

| Invariant | Check |
|---|---|
| public `.study` file | `PRIVATE_TRACKED` |
| public link to `.study` | `PRIVATE_LINK` |
| missing required frontmatter | `MISSING_FRONTMATTER` |
| invalid study mode | `INVALID_MODE` |
| broken internal Markdown/Wikilink | `BROKEN_LINK` |
| duplicate canonical ID | `DUPLICATE_ID` |
| missing resource `last_verified` | `RESOURCE_LAST_VERIFIED` |
| historical raw-attempt/feedback split | `HISTORY_SEPARATION` |
| volatile Obsidian state tracked | `OBSIDIAN_LOCAL_STATE` |
| unknown resource reference | `UNKNOWN_RESOURCE_ID` |
| unknown Week 0 question ID | `UNKNOWN_QUESTION_ID` |
| invalid technology depth | `INVALID_TECHNOLOGY_DEPTH` |
| public answer key | `PUBLIC_ANSWER_KEY` |

## False-positive controls

- `.study` in explanatory prose is allowed.
- Only actual links/paths into `.study` are rejected.
- fenced code blocks are removed before link scanning.
- external URLs and anchor-only links are ignored.
- Obsidian links are resolved with `.md` / `README.md` inference.
- ambiguous basename-only Wikilinks are not guessed.
- intentionally invalid `tests/fixtures/` are excluded from real repository validation.
- local ignored files are excluded via Git's tracked/nonignored file set.

## CI

`.github/workflows/validate.yml` runs on push and pull request:

1. checkout;
2. Python 3.12 setup;
3. unit/fixture tests;
4. `python scripts/validate_repo.py`.

No third-party Python dependency is required.

## Repository gate

After commit/push:

1. confirm only Task 14 + Task 12 status-finalization files changed;
2. inspect GitHub Actions run;
3. require tests PASS;
4. require repository validator PASS;
5. only then treat Task 14 as approved for mass-generation batches.
