# Adaptive Learning Model — C2-B

**Status:** C2-B candidate for review  
**Purpose:** Adjust future private study while preserving the public curriculum and historical learner evidence.

## 1. Adaptation inputs

Before adapting, inspect when available:

1. `.study/profile.md`
2. `.study/state.yaml`
3. `.study/metrics.yaml`
4. `.study/current-plan.md`
5. `.study/reviews/queue.yaml`
6. recent assessment records
7. recent error records
8. current project milestone status
9. career/interview feedback when the campaign is active
10. public curriculum prerequisites

No adaptation may be justified by one aggregate score alone.

## 2. Performance policy

Per skill/topic:

| Demonstrated performance | Action |
|---|---|
| `>= 85%` | maintenance / spaced review |
| `70–84%` | keep planned load |
| `50–69%` | targeted reinforcement |
| `< 50%` | recovery block before dependent advanced content |

## 3. Repeated-error rule

If the same or closely related error appears in **three separate evidence events**, promote the skill to `high` priority.

If that skill is a prerequisite for the next advanced topic and demonstrated score is `< 50`, promote to `recovery`.

Do not count repeated mistakes within one assessment as three independent evidence events.

## 4. Strong-performance rule

Two consecutive strong weekly results may reduce active repetition when:

- score is `>= 85`;
- no critical-dimension floor is violated;
- review backlog is under control.

Mandatory phase-gate coverage remains.

## 5. D+1 / D+7 / D+30 review generation

### Unknown / confused / forgotten concept
- D+1: explain from memory + one small example.
- D+7: reconstruct/apply without notes.
- D+30: diagnose or transfer to a realistic scenario.

### Reasoning / architecture error
- D+1: explain the trade-off/cause.
- D+7: compare two scenarios/designs.
- D+30: perform a new design/diagnosis with different constraints.

### Implementation / SQL / debugging error
- D+1: repair or reproduce a minimal case.
- D+7: recreate from scratch or solve a variant.
- D+30: diagnose an unfamiliar failure/performance case.

### Git error
- D+1: explain the history/state transition.
- D+7: perform the operation in a disposable repository.
- D+30: recover from a realistic history mistake.

### English communication
- D+1: rewrite/re-record the same technical concept more clearly.
- D+7: explain a related concept under timebox.
- D+30: include the skill in an interview/project walkthrough.

### AI-dependence
- D+1: SOLO reconstruction.
- D+7: SOLO variant task.
- D+30: required only when the gap persists or the topic is foundational.

### Validation failure
- D+1: create a verification checklist for the original problem.
- D+7: solve a variant where tests/evidence are mandatory.
- D+30: diagnose a plausible false-positive/silent failure case.

## 6. Review completion rules

A review is successful only when it includes active recall, reconstruction, application, diagnosis, or transfer.

Passive rereading alone:
- may be preparation;
- does not mark the review completed.

If a D+7 review scores `< 70`, create targeted follow-up and consider another D+7-style review before waiting to D+30.

## 7. Weekly workload ceiling

Defaults:

```text
weekly_hours_target = 12
weekly_hours_ceiling = 15
```

A private learner may configure them.

When required work exceeds the target:

### Keep first
1. overdue prerequisite reviews;
2. `recovery` blocks;
3. phase-gate remediation;
4. current core-backend prerequisites;
5. mandatory project evidence tied to the current core topic.

### Protect, but resize if necessary
6. English transversal practice;
7. career actions once the job-search phase is active;
8. AI-assisted-development practice tied to core work.

### Defer first
9. optional enrichment;
10. professional-exposure platforms;
11. nonessential supporting-platform labs;
12. extra challenge problems.

Never solve overload by deleting historical tasks. Record what was deferred.

If required foundational work would exceed `weekly_hours_ceiling`, the agent must propose a schedule extension/sequence change rather than silently overbook the learner.

## 8. Supporting / Industry Platforms adaptation

Depth classes remain:

```text
core
supporting
professional-exposure
market-triggered
```

Rules:

- Personal poor performance may increase private practice for an existing platform.
- A single job posting cannot promote public depth.
- Repeated market evidence may create a public proposal, never an automatic edit.
- Supporting-platform work is deferred before a core prerequisite when hours conflict.
- A platform may be promoted/demoted publicly only through human-reviewed curriculum proposal.

## 9. Career-feedback adaptation

### One job posting
May:
- update private gap analysis;
- suggest company-specific preparation.

May not:
- change public curriculum;
- promote a technology globally.

### Repeated market signal
A public proposal may be created only when:
- multiple relevant roles show the same requirement;
- the sample/time window is recorded;
- the requirement materially relates to the roadmap target role;
- workload/trade-offs are analyzed.

### Interview failure
May immediately create private remediation when the weakness is supported by:
- direct interviewer feedback; or
- a clearly documented learner failure.

Learner speculation alone should be tagged as lower-confidence evidence.

## 10. Adaptation pseudocode

```text
load public prerequisites
load private current state
load recent evidence
load due/overdue reviews

for each active skill:
    compute mode-specific evidence
    compute demonstrated score
    check critical dimension floors
    check recurrence
    check confidence mismatch
    check AI-dependence signal

generate mandatory remediation/reviews

merge with planned public curriculum

if workload > target:
    defer optional/exposure work first

if required foundations > ceiling:
    create proposal to extend/resequence private plan

write only future private plan/state/queue
never rewrite historical evidence
```

## 11. Three synthetic scenarios

### Scenario A — strong learner

Evidence:
- SOLO: 90, 88, 92
- HYBRID: 94
- no recurring errors
- review backlog: 0

Result:
- demonstrated score ~90;
- maintenance status;
- reduce repetition;
- keep D+30 transfer review;
- do not skip mandatory phase gate.

### Scenario B — apparent AI strength, weak independence

Evidence:
- SOLO: 55, 60
- AI-ASSISTED: 92, 94
- confidence: 90

Result:
- demonstrated score ~58;
- overconfidence flag;
- AI-dependence flag;
- targeted SOLO reconstruction;
- D+1/D+7 remediation;
- AI-assisted score remains evidence of supervision/productivity, not conceptual mastery.

### Scenario C — overloaded week after failed gate

Plan:
- 12h target / 15h ceiling
- 5h required recovery
- 10h originally planned curriculum
- 2h professional-exposure labs

Result:
- keep 5h recovery;
- preserve highest-priority core work;
- defer professional-exposure labs first;
- reduce optional enrichment;
- if core + recovery still exceeds 15h, extend/resequence the private schedule instead of creating a 17h week.

## 12. C2-B adaptation acceptance criteria

- Rules are deterministic and explainable.
- Historical evidence is never edited during adaptation.
- Supporting platforms cannot crowd out prerequisites.
- Review type changes with error type and interval.
- AI dependence is explicitly detectable.
- Career feedback affects private planning immediately but public planning only through proposals.
- Weekly workload respects target/ceiling.
