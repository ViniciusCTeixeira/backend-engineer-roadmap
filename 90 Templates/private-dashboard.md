---
type: private-dashboard
schema_version: 1
derived: true
generated_at: "{{generated_at}}"
---

# My Backend Engineer Roadmap

> [!warning] Derived view
> This dashboard is generated from canonical private state. Do not use it as the only place to record evidence or progress.

## Current state

| Field | Value | Canonical source |
|---|---|---|
| Current week | {{current_week}} | `state.yaml` |
| Current phase | {{current_phase}} | `state.yaml` |
| Weekly target | {{weekly_hours_target}} h | `state.yaml` |
| Weekly ceiling | {{weekly_hours_ceiling}} h | `state.yaml` |
| Week completion | {{current_week_completion}} | `metrics.yaml` |
| Actual hours this week | {{current_week_hours}} h | `metrics.yaml` |

When a source value does not exist, render `Not available yet`.

## Today's work

Source: `current-plan.md`

{{todays_work}}

## Reviews

Sources: `reviews/queue.yaml`, completed review records

| Metric | Value |
|---|---:|
| Due today | {{reviews_due_today}} |
| Overdue | {{reviews_overdue}} |
| Pending total | {{reviews_pending}} |

### Highest-priority reviews

{{priority_reviews}}

## Active gaps

Source: `state.yaml`

{{active_gaps}}

Priority order should distinguish:

```text
recovery
high
normal
low
```

## Skill evidence

Sources: `state.yaml`, assessment/review aggregates

| Skill | Demonstrated | Evidence confidence | Priority |
|---|---:|---|---|
{{skill_rows}}

Do not infer mastery from AI-assisted evidence alone.

## Study modes

Source: `metrics.yaml`

| Mode | Current evidence |
|---|---:|
| SOLO | {{solo_average}} |
| HYBRID | {{hybrid_average}} |
| AI-ASSISTED | {{ai_assisted_average}} |

### Calibration / AI-dependence flags

{{mode_flags}}

## Assessment trend

Source: `metrics.yaml`

| Metric | Value |
|---|---:|
| Current week average | {{assessment_current_week_average}} |
| Trailing 4-week average | {{assessment_trailing_4_week_average}} |

{{assessment_notes}}

## Project progress

Source: project progress records / `metrics.yaml`

| Project | Progress | Current milestone |
|---|---:|---|
| Project A — CakePHP Modernization | {{project_a_progress}} | {{project_a_milestone}} |
| Project B — Production Backend Platform | {{project_b_progress}} | {{project_b_milestone}} |

## English

Source: private progress/assessment evidence

{{english_progress}}

## Career

Source: private career aggregates

| Metric | Value |
|---|---:|
| Jobs analyzed | {{career_jobs_analyzed}} |
| Applications | {{career_applications}} |
| Interviews | {{career_interviews}} |
| Offers | {{career_offers}} |

{{career_next_action}}

If the career campaign is not active yet, state the current observation/positioning stage instead of showing invented funnel activity.

## Next actions

{{next_actions}}

## Last synchronization

{{generated_at}}

To rebuild this view, use `11 Agent/prompts/sync-dashboard.md`.
