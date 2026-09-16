# Data Schemas — C2-A

**Status:** C2-A candidate for review  
**Schema family version:** 1  
**Purpose:** Define stable, human-readable Obsidian/Markdown structures and machine-readable private state without making dashboards the source of truth.

## 1. Schema principles

1. Public templates contain no personal data.
2. Learner-specific records live only under `.study/`.
3. Raw historical evidence is append-only from the learner's perspective: agents may add feedback, but must not replace the original attempt.
4. Every machine-readable private file includes `schema_version`.
5. Stable IDs use lowercase kebab-case.
6. Dates use ISO `YYYY-MM-DD`; timestamps use ISO 8601 with timezone when time matters.
7. Scores are integers from `0` to `100` unless explicitly stated otherwise.
8. Study mode is one of `SOLO`, `HYBRID`, `AI-ASSISTED`.
9. Dashboards are derived views. They never become canonical storage.
10. Public curriculum changes and private learner adaptations use different record types.

## 2. Canonical IDs

Examples:

```text
php-strict-types
mysql-composite-indexes
redis-cache-stampede
http-idempotency
aws-iam-basics
ai-tool-calling

task-w10-d2-mysql-composite-indexes
assessment-2026-11-18-mysql-indexes
review-2026-11-19-mysql-composite-indexes-d1
job-2027-02-10-example-senior-backend
interview-2027-03-04-example-company-round2
proposal-2027-03-15-observability-resource-update
```

IDs must remain stable after creation even if the display title changes.

## 3. Enumerations

### Study mode

```text
SOLO
HYBRID
AI-ASSISTED
```

### Track

```text
core
industry-platforms
english
ai
project
review
career
```

### Technology depth

```text
core
supporting
professional-exposure
market-triggered
```

### Assessment status

```text
planned
in-progress
submitted
graded
abandoned
```

### Review interval

```text
D+1
D+7
D+30
custom
```

### Review status

```text
pending
completed
skipped
rescheduled
```

### Error category

```text
unknown-concept
confused-concepts
forgotten-concept
reasoning-error
implementation-error
sql-error
architecture-error
git-error
debugging-error
english-communication
ai-dependence
validation-failure
time-management
careless-error
```

### Skill priority

```text
low
normal
high
recovery
```

### Entry depth

```text
foundation
standard
accelerated
recovery
```

## 4. Learning-task frontmatter

Canonical public template:

```yaml
---
type: daily-plan
schema_version: 1
id: task-w01-d1-php-types
week: 1
day: 1
date: null
track: core
skill_ids:
  - php-type-system
mode: SOLO
estimated_minutes: 50
technology_depth: core
resource_ids: []
deliverables: []
review_policy: adaptive
prerequisites: []
status: planned
---
```

Rules:

- `date` remains `null` in reusable public curriculum and is resolved privately for a learner.
- `status` in public templates is illustrative; actual completion belongs to `.study/`.
- `resource_ids` reference resource catalog IDs rather than duplicating URLs.
- `deliverables` describe observable evidence.
- `technology_depth` is required when a task centers on a named technology/platform.

## 5. Assessment record schema

A learner assessment is stored privately as a dated Markdown record. Required frontmatter:

```yaml
---
type: assessment
schema_version: 1
id: assessment-2026-11-18-mysql-indexes
date: 2026-11-18
week: 10
assessment_type: sql-debugging
mode: SOLO
skill_ids:
  - mysql-indexes
  - mysql-explain
status: graded
assistance_declared: none
started_at: 2026-11-18T19:10:00-03:00
submitted_at: 2026-11-18T20:00:00-03:00
graded_at: 2026-11-18T20:12:00-03:00
score_total: 78
score_dimensions:
  factual_correctness: 80
  reasoning: 75
  practical_execution: 80
  validation: 70
  communication: 85
  english_quality: null
  ai_supervision: null
confidence_self_report: 85
grader: human-or-agent-id
---
```

The Markdown body must contain immutable/raw and append-only sections:

```markdown
# Assessment

## Instructions snapshot
Exact learner-facing instructions used for this attempt.

## Raw attempt — IMMUTABLE
The original learner answer/code/explanation exactly as submitted.

## Assistance declaration — IMMUTABLE
What tools were used, if any.

## Grading
Scores and rubric evidence.

## Feedback
Corrections and explanation. Never replace the raw attempt.

## Error records created
Links/IDs.

## Review events created
Links/IDs.

## Regrade history
Append-only entries if a grading error is later corrected.
```

### Regrading rule

If grading itself was wrong, do not edit the raw attempt. Append a regrade record:

```yaml
- timestamp: 2026-11-19T08:00:00-03:00
  previous_score: 78
  corrected_score: 82
  reason: "Rubric item X was misapplied."
```

Aggregated metrics may use the corrected grade, but both grade events remain visible.

## 6. Error-entry schema

Each error gets a stable ID and can reference multiple assessments later.

```yaml
---
type: error-entry
schema_version: 1
id: error-2026-11-18-mysql-leftmost-prefix
created_at: 2026-11-18T20:15:00-03:00
skill_ids:
  - mysql-composite-indexes
category: confused-concepts
severity: medium
source_ids:
  - assessment-2026-11-18-mysql-indexes
recurrence_count: 1
status: active
---
```

Body records:

- what happened;
- learner's original reasoning;
- correct concept;
- why the mistake occurred;
- one learner-created example;
- linked review events;
- later recurrence references;
- resolution evidence.

Historical description is not rewritten when the same error recurs; append a recurrence event.

## 7. Review-event schema

Canonical machine-friendly shape:

```yaml
schema_version: 1
id: review-2026-11-19-mysql-composite-indexes-d1
topic: mysql-composite-indexes
skill_ids:
  - mysql-composite-indexes
source_ids:
  - assessment-2026-11-18-mysql-indexes
reason: confused-concepts
due_date: 2026-11-19
interval: D+1
mode: SOLO
review_style: explain-and-small-exercise
status: pending
estimated_minutes: 20
priority: high
reschedule_count: 0
```

Completed reviews move to a completed record/archive or are marked completed without deleting the original queue evidence.

## 8. Private `state.yaml`

`state.yaml` represents the current state only. It may change over time because raw historical evidence lives elsewhere.

```yaml
schema_version: 1
current_week: 10
current_phase: data-and-web
start_date: 2026-09-21
target_role: senior-backend-engineer
weekly_hours_target: 12
weekly_hours_ceiling: 15
study_modes:
  solo: true
  hybrid: true
  ai_assisted: true
skill_state:
  mysql-composite-indexes:
    demonstrated_score: 64
    evidence_confidence: medium
    solo_score: 61
    hybrid_score: 72
    ai_assisted_score: null
    confidence_self_report: 85
    calibration_flag: overconfident
    study_priority: high
    recommended_entry_depth: foundation
    last_evidence_date: 2026-11-18
active_gaps:
  - mysql-composite-indexes
current_milestones:
  - modern-backend-data-model
```

## 9. `metrics.yaml`

Aggregates only. Raw records remain canonical.

```yaml
schema_version: 1
as_of: 2026-11-18
completion:
  current_week_percent: 75
  trailing_4_week_percent: 82
study_time:
  current_week_hours: 8.5
  trailing_4_week_average_hours: 11.2
assessments:
  current_week_average: 74
  trailing_4_week_average: 77
modes:
  solo_average: 69
  hybrid_average: 79
  ai_assisted_average: 88
reviews:
  pending: 6
  overdue: 2
projects:
  modernization_lab_percent: 65
  laravel_backend_percent: 20
career:
  jobs_analyzed: 15
  applications: 0
  interviews: 0
  offers: 0
```

## 10. Daily progress record

Private daily records may reference public tasks:

```yaml
---
type: daily-progress
schema_version: 1
date: 2026-11-18
week: 10
planned_minutes: 120
actual_minutes: 135
task_ids:
  - task-w10-d2-mysql-composite-indexes
completed_task_ids:
  - task-w10-d2-mysql-composite-indexes
energy_self_report: 3
notes_private: true
---
```

No public file is edited merely to mark a learner's completion.

## 11. Job-analysis schema

Job analyses are private and evidence-oriented.

Required fields:

```yaml
---
type: job-analysis
schema_version: 1
id: job-2027-02-10-example-senior-backend
captured_at: 2027-02-10T12:00:00-03:00
source_type: job-posting
company_alias: ExampleCo
role_title: Senior Backend Engineer
location_model: remote
application_status: analyzed
technology_signals:
  php: required
  laravel: required
  aws: required
  kubernetes: preferred
  kafka: preferred
fit:
  demonstrated: []
  in_progress: []
  missing: []
  risks: []
public_curriculum_change_allowed: false
---
```

A single job never directly changes public curriculum.

## 12. Interview-retrospective schema

```yaml
---
type: interview-retrospective
schema_version: 1
id: interview-2027-03-04-example-company-round2
date: 2027-03-04
company_alias: ExampleCo
round: technical
outcome: pending
skill_signals:
  php: strong
  mysql: weak
  system-design: medium
  english: medium
source_confidence: learner-recall
---
```

Body must separate:

- factual questions/tasks remembered;
- learner response summary;
- known external feedback;
- learner interpretation;
- gap classification;
- remediation created.

Do not store confidential or NDA-restricted interview content.

## 13. Curriculum-proposal schema

Public proposal:

```yaml
---
type: curriculum-proposal
schema_version: 1
id: proposal-2027-03-15-observability-resource-update
status: proposed
created_at: 2027-03-15
proposal_type: resource-update
affected_skill_ids:
  - observability-tracing
evidence_scope: generalized
breaking_change: false
---
```

Proposal body requires:

1. problem;
2. evidence;
3. why the issue is generic rather than learner-specific;
4. proposed change;
5. affected files;
6. workload impact;
7. alternatives considered;
8. validation plan.

## 14. Schema versioning

- New optional field: may retain the same schema version if old readers remain correct.
- Rename/remove/change meaning of a field: increment `schema_version`.
- Never migrate by overwriting historical raw attempts.
- A migration may add derived metadata or create a new transformed file while preserving the original evidence.
- Public examples must always use synthetic data.

## 15. C2-A acceptance criteria

- All canonical note types have explicit schemas.
- Raw assessment attempt is structurally separated from feedback.
- Public task completion is never stored in the public curriculum.
- Every machine-readable private file includes `schema_version`.
- Stable IDs are defined.
- `.study/` remains the only canonical home for learner state.
- Examples contain synthetic data only.
