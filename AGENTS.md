# Agent Instructions

This repository is a public, reusable adaptive Backend Engineer study system. Read this file before changing the repository.

## Source of truth

Before substantial work, read the relevant approved documents:

- `docs/superpowers/specs/2026-09-15-adaptive-backend-roadmap-design.md`
- `docs/superpowers/specs/2026-09-15-supporting-industry-platforms-amendment.md`
- `docs/superpowers/plans/2026-09-15-roadmap-v1-implementation-plan.md`
- `docs/decision-log.md`
- `docs/checkpoints.md`

Detailed policies live under `11 Agent/rules/` and `docs/`.

## Public vs private

The public repository contains reusable curriculum, resources, templates, projects, assessments, agent rules, and documentation.

Learner-specific state belongs only under `.study/`, which is a separate ignored Git repository.

Never copy learner-specific data into public files unless the information is intentionally anonymized/generalized and a human approves the public change.

Read `11 Agent/rules/public-private-boundary.md`.

## Historical integrity

Never silently rewrite completed assessment attempts, historical scores, original interview notes, job outcomes, or error-history evidence.

Feedback, regrades, links, and later evidence are append-only.

Read `11 Agent/rules/history-integrity.md` and `11 Agent/rules/assessment-integrity.md`.

## Autonomy classes

### AUTO-PRIVATE
Within `.study/`, you may update future plans, current aggregates, review queues, priorities, and private recommendations when rules permit.

### AUTO-PUBLIC-LOW-RISK
You may fix objective low-risk public issues such as typos, broken internal links, formatting, verified stale URLs, and incorrect metadata.

### PROPOSAL-REQUIRED
Create a proposal before changing curriculum order/content, technology depth, phase ordering, scoring thresholds, target role, certification strategy, workload model, or adding/removing a public platform.

### NEVER-SILENTLY-MODIFY
Do not rewrite history, expose secrets/private data, force-push, destructively rewrite Git history, or leak assessment answer keys.

## Before personal adaptation

When present, inspect:

- `.study/profile.md`
- `.study/state.yaml`
- `.study/metrics.yaml`
- `.study/current-plan.md`
- `.study/reviews/queue.yaml`
- recent `.study/assessments/`
- recent `.study/errors/`
- relevant current curriculum/prerequisites

Read `11 Agent/rules/adaptation.md`.

## Study modes

- `SOLO`: do not solve the learner's task.
- `HYBRID`: preserve the first SOLO attempt before assistance.
- `AI-ASSISTED`: assistance is expected, but require learner review and validation.

AI-assisted performance alone does not establish conceptual mastery.

## Sources

Prefer official/primary sources. Fast-moving topics require freshness verification before public changes.

Read `11 Agent/rules/source-quality.md`.

## Scoped instructions

Additional `AGENTS.md` files may exist in:

- `01 Curriculum/`
- `02 Daily Assessments/`
- `05 Projects/`
- `07 Career/`
- `10 AI Engineering/`

For files within those trees, follow both this file and the more specific file. More specific rules win on scoped details without overriding project safety/integrity requirements.

## Git and validation

Before editing:
1. inspect repository status and relevant files;
2. state the bounded task and intended files;
3. avoid unrelated changes.

After editing:
1. run applicable validation/checks;
2. inspect `git diff --check`;
3. inspect the final diff for private data, answer leakage, and scope creep;
4. report files changed and validation results;
5. do not commit unless the user explicitly asked you to commit.

Never force-push or amend/rewrite existing history unless an explicit human instruction authorizes that exact action.
