# Task 15 Batch Validation — Weeks 05–08

**Date:** 2026-09-16  
**Status:** Package structural validation PASS; full repository validation pending application

## Scope

Generate the first C6-authorized Task 15 batch while preserving the validated Weeks 1–4 model.

## Weeks

| Week | Focus | Project milestone | Minutes |
|---|---|---|---:|
| 05 | PHP runtime / FPM / request path | `legacy-runtime-map` | 720 |
| 06 | CakePHP lifecycle / ORM / boundaries | `legacy-runtime-map` | 720 |
| 07 | Linux / network troubleshooting | `legacy-ops-basics` | 720 |
| 08 | Foundations integration / reproducible workflow | `legacy-ops-basics` | 720 |

## Generated content

- 4 week README files
- 28 daily plans
- 28 daily assessments
- 4 weekly simulations
- curated Weeks 5–8 resource page
- catalog append helper
- updated Curriculum README and public Dashboard

## Workload

Each week totals exactly 720 minutes (12 hours): `105 + 105 + 105 + 105 + 105 + 135 + 60`.

## Required tracks

All weeks include core outcome, Project A, daily assessment, weekly simulation, English, AI/agent evidence, review hooks, and private career action.

## Assessment integrity

Public assessments/simulations contain prompts only; learner answers remain private; SOLO/HYBRID boundaries preserve independent evidence.

## Full repository gate

After applying the package and resource helper, run:

```bash
python -m unittest discover -s tests -p "test_*.py" -v
python scripts/validate_repo.py
git diff --check
```

All commands must pass before this batch is approved on `master`.
