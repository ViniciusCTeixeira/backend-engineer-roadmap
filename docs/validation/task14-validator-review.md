# Task 14 Validation — Static Repository Validator

**Date:** 2026-09-16  
**Status:** PASS — static validator approved; hosted GitHub Actions intentionally removed

## Scope

Add deterministic static validation before Weeks 5–52 are generated at scale.

## Implementation

Task 14 introduced:

```text
scripts/validate_repo.py
scripts/README.md
tests/test_validate_repo.py
tests/fixtures/
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

Hosted workflow removal:

```text
5ef36e7059bb7b7c07f07e713273f8211ac0b67f
chore: remove hosted github actions workflow
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

The accidentally tracked runtime caches were removed. The synthetic negative fixture under `tests/fixtures/generated-python-cache/` remains intentionally versioned.

Result: **PASS**

## Hosted CI history

A GitHub Actions workflow was initially added, but repeated runs failed at the platform startup layer before jobs were created:

```text
run: 35055206204 → startup_failure, jobs: 0
run: 35055576555 → startup_failure, jobs: 0
run: 35055883687 → startup_failure, jobs: 0
```

The user then explicitly chose to remove hosted GitHub Actions from this repository to avoid hosted CI charges.

This is a repository-operation decision, not a curriculum change: GitHub Actions remains part of the Year 1 learning plan and should be practiced in bounded learning/project exercises.

## Validation policy from now on

After every curriculum-generation batch and before release gates, run locally:

```bash
python -m unittest discover -s tests -p "test_*.py" -v
python scripts/validate_repo.py
```

Both commands must pass before the batch is approved.

No hosted GitHub Actions run is required for C7/V1 unless this decision is explicitly revisited.

## Conclusion

**Task 14 is approved. Repository validation for V1 is local-only, deterministic, and mandatory after every Task 15 batch.**
