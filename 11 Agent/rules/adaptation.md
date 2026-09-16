# Agent Rule — Adaptation

This rule governs any agent that changes learner-specific future planning.

## Required read set

When files exist, read:

1. `.study/profile.md`
2. `.study/state.yaml`
3. `.study/metrics.yaml`
4. `.study/current-plan.md`
5. `.study/reviews/queue.yaml`
6. recent `.study/assessments/`
7. recent `.study/errors/`
8. current public curriculum week/prerequisites

## Allowed autonomous writes

Within `.study/`, an agent may:

- update aggregated current state;
- add future review events;
- add future remediation tasks;
- reprioritize future private tasks;
- defer optional future private tasks;
- add private recommendations.

## Forbidden behavior

Never:

- overwrite raw historical attempts;
- delete historical scores;
- rewrite interview outcomes;
- alter public curriculum because one learner struggled;
- exceed the configured weekly ceiling silently;
- treat AI-assisted success as proof of SOLO conceptual mastery;
- promote a supporting/exposure platform publicly without a proposal.

## Performance actions

```text
>=85  -> maintenance
70–84 -> keep load
50–69 -> targeted reinforcement
<50   -> recovery before dependent advanced content
```

Critical dimension floors and repeated-error rules still apply.

## Priority under overload

Keep:
1. overdue prerequisite reviews;
2. recovery;
3. gate remediation;
4. core prerequisites;
5. mandatory core-project evidence.

Defer before core:
- enrichment;
- professional exposure;
- optional supporting-platform labs.

If required work exceeds ceiling, create a human-review proposal for private resequencing.
