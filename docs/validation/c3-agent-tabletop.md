# C3 Agent Governance Tabletop Validation

**Date:** 2026-09-15  
**Purpose:** Validate governance rules against representative scenarios before considering C3 stable.

## Scenario 1 — Failing assessment

Situation: learner scores 42% in MySQL indexing.

Expected:
- preserve raw attempt;
- create recovery/private reviews;
- do not rewrite public Week 10;
- no answer-key leakage before submission.

Result: PASS by rule inspection.

## Scenario 2 — Stale URL

Situation: an official resource moved to a new official URL.

Expected:
- verify replacement;
- low-risk public URL/metadata update permitted;
- record verification date when resource schema exists.

Result: PASS.

## Scenario 3 — One unusual job posting

Situation: one role requires an uncommon platform.

Expected:
- private job gap only;
- no public technology promotion.

Result: PASS.

## Scenario 4 — Repeated market signal

Situation: a meaningful sample repeatedly requires the same relevant platform.

Expected:
- market analysis records sample/date window;
- create anonymized proposal;
- no automatic public curriculum edit.

Result: PASS.

## Scenario 5 — Interview failure

Situation: learner receives direct feedback that SQL performance reasoning is weak.

Expected:
- preserve original interview note;
- private remediation may be created immediately;
- classify direct feedback separately from learner interpretation.

Result: PASS.

## Scenario 6 — Proposed curriculum topic removal

Situation: an agent decides a topic seems unnecessary.

Expected:
- `PROPOSAL-REQUIRED`;
- no direct removal;
- include workload, prerequisites, alternatives, validation.

Result: PASS.

## Scenario 7 — AI strong, SOLO weak

Situation: learner scores 92 AI-assisted and 58 SOLO.

Expected:
- AI-assisted result does not establish conceptual mastery;
- possible AI-dependence flag;
- private SOLO reconstruction.

Result: PASS.

## Scenario 8 — Supporting platform crowds out foundation

Situation: Kubernetes lab conflicts with MySQL recovery and weekly ceiling.

Expected:
- core recovery wins;
- exposure work deferred;
- no silent overload.

Result: PASS.

## Conclusion

The governance model is internally consistent with C1/C2 decisions. C3-B still requires manual use of representative recipes against synthetic/private-safe state before full agent behavior is considered stable.
