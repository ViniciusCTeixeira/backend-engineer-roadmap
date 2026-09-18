# Contributing

Thanks for helping improve the Adaptive Backend Engineer Roadmap.

This repository is a reusable public learning product. Contributions should improve that product without leaking learner-specific state or weakening assessment integrity.

## Before changing anything

Read:

- `AGENTS.md`
- applicable scoped `AGENTS.md` files
- `docs/decision-log.md`
- `docs/resource-policy.md`
- `docs/assessments.md`
- `docs/adaptive-learning.md`

For substantial curriculum changes, also read the approved design/specification documents under `docs/superpowers/`.

## Change classes

### Low-risk public changes

Examples:

- typo or grammar fixes;
- broken internal links;
- formatting;
- clearly stale URL replacement with the same official resource;
- metadata corrections that do not change lesson meaning.

These can be small, focused changes.

### Proposal-required changes

Do not silently change:

- curriculum order or topic scope;
- phase order;
- weekly workload model;
- assessment difficulty or scoring thresholds;
- target role;
- technology depth;
- certifications;
- major project architecture;
- adding/removing a technology track.

Create a reviewable proposal first.

## Public/private boundary

Never commit learner-specific data.

Private data includes, among other things:

```text
.study/
real assessment answers
personal scores
active weaknesses
private project notes
job/application data
interview notes
compensation information
relocation/sponsorship discussions
personal agent analysis
```

Synthetic examples are allowed when they cannot be mistaken for real learner/employer data.

## Assessment integrity

Public assessments may contain prompts, instructions, rubrics, and grading structure.

Do not place a model answer or solution beside an active public assessment.

Do not rewrite historical learner attempts or scores.

## Resource contributions

Prefer:

1. official documentation/specifications;
2. official free tutorials;
3. respected university/open-source educational material;
4. high-quality community material;
5. paid material only as an optional supplement.

When adding or updating a catalog resource, maintain:

```yaml
id:
title:
url:
topic_ids:
type:
source_authority:
language:
cost:
last_verified:
version_scope:
technology_depth:
notes:
```

Fast-moving sources must be freshly verified.

## Writing curriculum content

A useful task should define:

- what to learn;
- why it matters;
- the primary source;
- hands-on work;
- observable deliverable/evidence;
- declared study mode;
- timebox;
- review implications.

Reading alone is not completion.

Keep the default weekly ceiling intact unless an approved design change says otherwise.

## AI-assisted contributions

Coding agents are allowed, but agent output is not evidence that a contribution is correct.

Review the final diff and run the local quality gate.

If a task is marked SOLO in the curriculum, do not use an agent to produce the learner's scored answer.

## Local validation

Run before proposing a public change:

```bash
python -m unittest discover -s tests -p "test_*.py" -v
python scripts/validate_repo.py
git diff --check
git status
```

Do not add hosted GitHub Actions for routine validation unless the repository's explicit governance changes.

## Commit scope

Prefer reviewable commits with one purpose.

Examples:

```text
docs: fix onboarding links
docs: refresh mysql resource metadata
feat: add approved curriculum batch
fix: preserve private-state boundary
```

Do not force-push or rewrite shared history as part of normal contribution flow.

## Licensing

By submitting a contribution, you agree that your contribution may be distributed under this repository's MIT License.

Do not submit third-party material that you do not have the right to contribute.
