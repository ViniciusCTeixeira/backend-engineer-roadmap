# Historical Integrity

Historical evidence is append-only in meaning.

## Immutable after submission/recording

Never replace:
- learner raw assessment attempt;
- assistance declaration;
- original assessment instructions snapshot;
- original interview notes/recollection;
- recorded application outcome;
- original error occurrence;
- previous grade event.

## Allowed append-only additions

You may append:
- grading;
- feedback;
- links;
- recurrence events;
- regrade events;
- later evidence;
- resolution evidence.

## Current-state files

`state.yaml`, `metrics.yaml`, `current-plan.md`, and pending review queues are current/derived state and may be updated according to the adaptation policy.

They do not replace the underlying historical records.

## Correction model

When a historical metadata/grade error is discovered:
1. preserve original evidence;
2. append a correction/regrade event;
3. state why;
4. let current aggregates use the latest valid corrected value.
