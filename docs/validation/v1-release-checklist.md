# V1 Public-Release Checklist — C7

**Date:** 2026-09-17  
**Release-candidate commit:** `e3ea5607be6f28de668e0ca27828803403d6d5ff`  
**Status:** C7 PASS — public release QA approved; annotated `v1.0.0` tag pending

## 1. Task 16 handoff

- [x] `docs: prepare public roadmap release` exists on `master` at `3a24f0e9181cc5d770fbb569172b6d52c6421c74`.
- [x] The 11 Task 16 files match the approved Task 16 package by Git blob SHA.
- [x] Task 16 documentation is treated as approved after repository revalidation.

## 2. Clean-clone QA

A separate clean clone of the C7 candidate was created from an isolated QA repository.

Initial clean-clone testing exposed a real release blocker:

```text
test_tracked_private_study_file_fails ... FAIL
private-tracked unexpectedly passed
```

Root cause:

- `tests/fixtures/private-tracked/.study/state.yaml` is an intentional negative fixture;
- the root `.gitignore` pattern `.study/` also ignored this nested test fixture;
- an existing developer checkout could retain the ignored fixture locally, hiding the issue;
- a true clean clone omitted the fixture and therefore invalidated the regression test.

Fix:

- explicitly allowlist only `tests/fixtures/private-tracked/.study/**`;
- add a regression test requiring the negative fixture to exist and be tracked in Git.

TDD evidence:

```text
RED
AssertionError: False is not true : private-tracked negative fixture is missing from this checkout

GREEN
Ran 19 tests
OK
```

Final clean-clone checks:

- [x] worktree starts clean;
- [x] `.study/` does not exist initially;
- [x] README contains the real clone command;
- [x] getting-started contains the real clone command;
- [x] validator tests: 19/19 pass;
- [x] `python scripts/validate_repo.py`: zero errors;
- [x] `git diff --check`: clean;
- [x] no hosted `.github/workflows/` files.

Canonical clone command:

```bash
git clone https://github.com/ViniciusCTeixeira/backend-engineer-roadmap.git
cd backend-engineer-roadmap
```

## 3. Private-state initialization QA

Using synthetic learner state in the clean clone:

- [x] `.study/.git` initializes as an independent nested repository;
- [x] `git check-ignore .study` succeeds in the public parent;
- [x] parent `git ls-files .study` returns zero files;
- [x] parent `git status` remains clean;
- [x] nested `.study` repository can commit independently;
- [x] missing derived values use `Not available yet` rather than invented data.

GitHub history check at the candidate base found zero commits for:

```text
.study
.study/state.yaml
.study/profile.md
```

## 4. Agent tabletop QA

Representative recipes reviewed/tested with synthetic state:

| Recipe | Expected write boundary | Result |
|---|---|---|
| `initialize-study` | `.study/` only | PASS |
| `start-day` | private current/future planning | PASS |
| `finish-day` | private progress/state/metrics/reviews/errors | PASS |
| `weekly-retrospective` | private future planning/metrics/reviews/agent notes | PASS |
| `analyze-job` | private career/job analysis | PASS |
| `post-interview` | private retrospective/errors/reviews/future plan | PASS |
| `propose-curriculum-improvement` | one generalized file under `docs/proposals/` only | PASS after C7 boundary clarification |

Synthetic write-boundary evidence:

- [x] all private command simulations left the parent public worktree unchanged;
- [x] submitted raw assessment bytes remained unchanged;
- [x] original interview-note bytes remained unchanged;
- [x] public proposal tabletop changed exactly one file;
- [x] proposal contained generalized synthetic evidence only;
- [x] no direct curriculum edit occurred.

Codex/Claude bootstrap:

- [x] `AGENTS.md` remains canonical shared policy;
- [x] `CLAUDE.md` imports `@AGENTS.md`;
- [x] recipes contain both Codex and Claude Code notes.

## 5. Assessment integrity QA

- [x] `prepare-assessment` explicitly prohibits answer key/model-solution disclosure before submission/abandonment;
- [x] public assessments/simulations/question-bank scan found zero `## Solution` / `## Answer Key` headings;
- [x] validator negative tests for public answers remain green;
- [x] raw submitted attempts are explicitly protected by agent rules/recipes.

## 6. Resource freshness audit

Fast-moving or version-sensitive references were rechecked immediately before the candidate release.

Verified against current official sources on 2026-09-17:

- PHP supported versions;
- Laravel current documentation (13.x);
- Docker Get Started;
- GitHub Actions documentation;
- AWS IAM, VPC, RDS, and SQS docs;
- Cloudflare DNS and WAF docs;
- Kubernetes Basics;
- Helm Quickstart (4.3.0);
- OpenAI Structured Outputs, Function Calling, Embeddings, Evals, and developer docs;
- MCP current introduction/spec documentation.

Release correction:

```text
helm-quickstart
old: https://docs.helm.sh/docs/intro/quickstart/
new: https://helm.sh/docs/intro/quickstart/
```

Affected fast-moving catalog entries receive `last_verified: '2026-09-17'`.

## 7. V1 success criteria review

Approved design criterion: an experienced PHP learner can clone the public repository, open it in Obsidian, initialize ignored/private `.study/`, run Week 0, receive private adaptation, use all study modes, preserve immutable assessments, receive D+1/D+7/D+30 reviews, use Codex/Claude recipes, complete project progression, and enter the job-search phase without personal data entering public Git history.

Evidence:

- [x] complete Week 0 exists;
- [x] Weeks 1–52 are generated;
- [x] Dashboard/Obsidian onboarding exists;
- [x] private nested-Git workflow passes synthetic QA;
- [x] SOLO / HYBRID / AI-ASSISTED policies are documented and represented in curriculum;
- [x] immutable assessment/history rules exist and are validator/recipe protected;
- [x] D+1/D+7/D+30 adaptive review system exists;
- [x] Codex and Claude Code workflows are documented;
- [x] Project A and Project B progression exists;
- [x] career campaign and Year 2 transition exist;
- [x] current GitHub history query shows no `.study` commits;
- [x] local static validation passes with zero errors.

## 8. Final C7 verification

- [x] C7 package applied to the real repository.
- [x] local tests/validator/diff checks passed on the release candidate.
- [x] release-candidate fixes committed and pushed to `master` at `e3ea5607be6f28de668e0ca27828803403d6d5ff`.
- [x] pushed `master` revalidated against this checklist.
- [x] GitHub repository visibility changed to **public**.
- [x] GitHub reports canonical clone URL `https://github.com/ViniciusCTeixeira/backend-engineer-roadmap.git`.
- [x] GitHub reports `private: false`, `visibility: public`, and default branch `master`.
- [x] checklist status updated to C7 PASS.

Public-access note:

The assistant execution sandbox could not perform a redundant outbound `git clone` because its environment could not resolve `github.com` through DNS. This is recorded as an execution-environment limitation rather than hidden. The repository itself is confirmed public by GitHub, the canonical HTTPS clone endpoint is exposed, and clean-clone behavior was already validated in the isolated C7 QA repository.

The only remaining release action is the annotated `v1.0.0` tag.

## 9. Final release commands

```bash
git tag -a v1.0.0 -m "Adaptive Backend Engineer Roadmap v1.0.0"
git push origin v1.0.0
```

Do not tag a candidate that has not passed public-visibility and pushed-`master` revalidation.
