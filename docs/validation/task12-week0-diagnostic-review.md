# Task 12 Validation — Executable Week 0

**Date:** 2026-09-16  
**Status:** Local package validation PASS; repository validation pending commit/push

## Scope

Turn the already-approved C1 Week 0 blueprint into executable public prompts while preserving assessment integrity and private learner state.

## Schedule validation

| Day | Required | Minutes | Blueprint |
|---|---|---:|---|
| 1 | yes | 130 | PASS |
| 2 | yes | 135 | PASS |
| 3 | yes | 140 | PASS |
| 4 | yes | 145 | PASS |
| 5 | yes | 135 | PASS |
| 6 | yes | 140 | PASS |
| 7 | no | 90 max | PASS |

No required day exceeds 150 minutes.

## Domain coverage

All 19 approved diagnostic domains have at least one public prompt:

- php-language-runtime
- oop-design
- composer-dependencies
- cakephp-depth
- laravel-familiarity
- mysql-core
- redis-core
- git-github
- http-api-security
- testing-static-analysis
- linux-networking
- docker
- aws-cloud
- cicd
- system-design
- algorithms
- english-technical
- agentic-development
- llm-ai-engineering

Result: **PASS**

## Mode coverage

- closed SOLO conceptual/practical evidence: PASS
- HYBRID testing/static-analysis exercise: PASS
- HYBRID coding-agent repository exercise: PASS
- post-agent SOLO diff/risk review: PASS
- technical English written evidence: PASS
- technical English reading evidence: PASS
- technical English spoken/self-recorded evidence: PASS

## Framework-depth validation

CakePHP prompts require lifecycle/ORM/debugging reasoning rather than CRUD familiarity only.

Laravel explicitly allows `not used` / shallow familiarity rather than penalizing honest lack of framework-specific exposure.

Result: **PASS**

## Assessment integrity

- public Question Bank contains prompts only: PASS
- no public answer key/model solution section: PASS
- SOLO prompts prohibit agent help before submission/abandonment: PASS
- HYBRID prompts preserve first SOLO evidence: PASS
- raw attempts are stored privately and immutable after submission: PASS
- diagnostic result template uses C2 scoring instead of the obsolete "pending C2" placeholder: PASS

## Agentic diagnostic safety

The coding-agent task:

- uses a synthetic PHP component;
- requires a private diagnostic sandbox;
- prohibits editing public curriculum files;
- requires a SOLO plan/invariants before agent use;
- requires independent diff/test review after agent use;
- records accepted/rejected changes.

Result: **PASS**

## Adaptation

Day 7 uses the existing adaptation model:

```text
>=85  maintenance
70–84 keep load
50–69 targeted reinforcement
<50   recovery before dependent advanced work
```

Critical floors, mode separation, review generation, workload ceiling, and public/private boundary remain authoritative.

Result: **PASS**

## Files added/updated

- Week 0 README
- 7 executable day files
- Question Bank README
- 19 diagnostic domain files
- diagnostic result template
- this validation record

## Repository gate

After commit/push, validate on GitHub:

1. only Task 12 files changed;
2. all 19 diagnostic domain files exist;
3. all day totals match blueprint;
4. no public answer-key/model-solution section exists;
5. diagnostic-result template references current C2 scoring;
6. public curriculum outside Week 0 is unchanged.

Task 12 is approved only after repository revalidation passes.
