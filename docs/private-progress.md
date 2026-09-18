# Private Learner State

The roadmap separates reusable public curriculum from personal learner evidence.

## Why `.study/` exists

A study system becomes personal very quickly:

- real scores;
- answers;
- errors;
- weaknesses;
- confidence;
- current priorities;
- project notes;
- job applications;
- interview outcomes;
- market observations.

Committing these values to the public curriculum would turn the repository into one person's diary and can expose sensitive information.

The solution is an independent nested repository:

```text
backend-engineer-roadmap/     public repository
└── .study/                   private independent Git repository
```

The parent `.gitignore` ignores `.study/`.

## Not a submodule

`.study/` is intentionally not a Git submodule.

The public repository should not pin or advertise a learner's private-state repository.

A learner may optionally configure a private remote from inside `.study/`.

## Canonical private state

Important canonical files/locations include:

```text
.study/profile.md
.study/state.yaml
.study/metrics.yaml
.study/current-plan.md
.study/reviews/queue.yaml
.study/progress/
.study/assessments/
.study/errors/
.study/projects/
.study/career/
.study/agent/
.study/archive/
```

`.study/dashboard.md` is a **derived view**.

Never treat dashboard text as a substitute for canonical state.

When source evidence does not exist, render:

```text
Not available yet
```

instead of inventing a value.

## Historical integrity

After submission, keep raw attempts immutable.

Later information belongs in:

- feedback;
- regrades;
- review records;
- error records;
- linked later evidence.

Do not rewrite the original attempt to make historical performance look better.

The same principle applies to interview notes and job outcomes.

## Git workflow

The private repository can be versioned independently:

```bash
git -C .study status
git -C .study add .
git -C .study commit -m "study: record week progress"
```

A remote is optional.

If used, it should be private and configured from inside `.study/`.

## Parent-repository safety

Useful checks:

```bash
git check-ignore .study
git status
git ls-files .study
```

Expected:

- `.study` is ignored;
- public `git status` does not list learner state;
- `git ls-files .study` returns nothing.

## Private agent writes

Agent rules allow more adaptation inside `.study/` than in public curriculum.

Examples of future private state that may be updated when evidence supports it:

- review priorities;
- future study plan;
- active gaps;
- current aggregates;
- remediation;
- interview preparation.

Agents still must not silently rewrite historical evidence.

## Backup and recovery

The strongest backup is a private remote plus normal Git history.

Do not solve backup by adding `.study/` to the public repository.

If `.study/` is lost and no private backup exists, reconstruct only what can be supported by real evidence. Do not invent past scores or completed work.

## Starting point

Use:

```text
11 Agent/prompts/initialize-study.md
```

Then open:

```text
.study/dashboard.md
```
