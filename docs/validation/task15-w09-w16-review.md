# Task 15 Batch Validation — Weeks 09–16

**Date:** 2026-09-16  
**Status:** Package structural validation PASS; full repository validation pending application

## Scope

Generate the Data & Web batch and Phase Gate 1 under the approved C6 gate.

## Weeks

| Week | Focus | Project evidence | Minutes |
|---|---|---|---:|
| 09 | relational modeling + SQL | `legacy-mysql` / `platform-data-model` | 720 |
| 10 | indexes + EXPLAIN + benchmark | `legacy-mysql` / `platform-data-model` | 720 |
| 11 | transactions + locks + concurrency | `legacy-mysql` / `platform-data-model` | 720 |
| 12 | Redis + caching/failure modes | `legacy-redis` / `platform-data-model` | 720 |
| 13 | Phase Gate 1 | cumulative evidence freeze + remediation | 720 |
| 14 | HTTP + idempotency + OpenAPI/Bruno/Postman | `legacy-api-quality` / `platform-api-contract` | 720 |
| 15 | API design + auth/authz/security | `legacy-api-quality` / `platform-api-contract` | 720 |
| 16 | PHPUnit + PHPStan + quality loop | `legacy-api-quality` / `platform-api-contract` | 720 |

## Generated content

- 8 week README files
- 56 daily plans
- 56 daily assessments
- 8 weekly simulations
- Data & Web resource page
- catalog append helper
- updated public Curriculum/Dashboard
- finalized Weeks 5–8 validation status

## Matrix / project alignment

- Weeks 9–11: Project A `legacy-mysql` + Project B `platform-data-model`
- Week 12: Project A `legacy-redis` + Project B cache rationale
- Week 13: cumulative SOLO Phase Gate 1; agents only after immutable submission
- Weeks 14–16: Project A `legacy-api-quality` + Project B `platform-api-contract`
- Week 14 supporting platforms: OpenAPI + Bruno + bounded Postman comparison
- Week 16 keeps PHPUnit/PHPStan core and does not require hosted CI

## Workload

Every week totals exactly 720 minutes.

Week 13's 90-minute cumulative simulation is included inside Day 6's 135-minute budget.

## Assessment integrity

- scored daily attempts are SOLO;
- HYBRID activities preserve pre-agent evidence;
- Week 13 scored gate sections prohibit agent/search assistance;
- no public model solution/answer key;
- raw attempts stay private and immutable.

## Full repository gate

After application:

```bash
python -m unittest discover -s tests -p "test_*.py" -v
python scripts/validate_repo.py
git diff --check
```

All commands must pass before this batch is approved on `master`.
