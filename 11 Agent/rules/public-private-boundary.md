# Public / Private Boundary

## Public repository

Public files may contain:
- reusable curriculum;
- templates;
- synthetic examples;
- public resources;
- generic project specifications;
- generic prompt recipes;
- generalized/anonymized curriculum proposals.

Public files must not contain learner-specific progress.

## Private `.study/`

Store learner-specific:
- profile;
- diagnostic results;
- scores;
- raw attempts;
- review queue;
- errors;
- schedule adaptations;
- applications;
- interviews;
- private retrospectives;
- private agent logs/proposals.

`.study/` is an independent Git repository ignored by the public repository.

## Write classes

### AUTO-PRIVATE
Allowed when historical evidence remains intact:
- future schedule changes;
- review queue additions;
- current aggregate metrics;
- skill priorities;
- private gap analysis.

### AUTO-PUBLIC-LOW-RISK
Allowed:
- typo/format correction;
- broken internal link;
- verified URL replacement;
- objectively incorrect metadata;
- nonsemantic cross-reference repair.

### PROPOSAL-REQUIRED
Required for:
- curriculum content/order;
- assessment difficulty/rubric changes;
- adaptation thresholds;
- technology depth changes;
- new platform/technology;
- target role;
- certification strategy;
- public workload model.

### NEVER-SILENTLY-MODIFY
Never silently:
- publish private learner data;
- move private history into public files;
- delete historical evidence;
- reveal secrets/tokens;
- publish NDA/confidential material.

## Generalization rule

Private evidence may motivate a public proposal only after it is generalized. The proposal must describe the curriculum problem without identifying the learner/employer or copying private records.
