---
type: diagnostic-result
schema_version: 1
id: "{{diagnostic_result_id}}"
date: "{{date}}"
question_ids: []
skill_ids: []
assessment_type: conceptual
mode: SOLO
status: planned
assistance_declared: none
started_at: null
submitted_at: null
graded_at: null
score_total: null
score_dimensions:
  factual_correctness: null
  reasoning: null
  practical_execution: null
  validation: null
  communication: null
  english_quality: null
  ai_supervision: null
confidence_self_report: null
evidence_confidence: null
recommended_entry_depth: null
grader: null
---

# Diagnostic Result — {{date}}

## Domain / skill IDs

## Question IDs

## Mode and assistance declaration

## Raw attempt — IMMUTABLE AFTER SUBMISSION

> Preserve the learner's original attempt exactly as submitted. Do not rewrite it after feedback.

## Scoring

Use `docs/assessments.md` and the rubric for `assessment_type`.

### Dimension scores

- Factual correctness:
- Reasoning / explanation:
- Practical execution:
- Validation / testing:
- Communication:
- English quality:
- AI supervision:

### Total score

## Critical dimension floors

Record any applicable floor violation, including:

- validation `<50` where production/security/data-integrity validation applies;
- reasoning `<50` for conceptual mastery;
- AI supervision `<50` for agentic mastery;
- English quality `<50` when English is explicitly assessed.

## Confidence calibration

- confidence self-report:
- demonstrated evidence:
- calibration flag:

## Evidence by study mode

Do not merge AI-assisted evidence into SOLO evidence.

- SOLO evidence:
- HYBRID evidence:
- AI-ASSISTED evidence:

## Gaps detected

## Recommended entry depth

Choose from:

```text
foundation
standard
accelerated
recovery
```

## Recommended private adaptation

Use approved thresholds and critical floors. Do not change public curriculum from one learner's result.

## Review events to create

- [ ] D+1 when justified
- [ ] D+7 when justified
- [ ] D+30 transfer when justified

## Evidence links

## Feedback

Append feedback after submission. Never replace the raw attempt.

## Regrade history

Append corrections; preserve previous grade events.
