---
type: daily-plan
schema_version: 1
id: task-w05-d05-php-runtime-and-fpm
week: 5
day: 5
date: null
track: core
skill_ids:
- runtime-observability
- php-fpm
- logging
- systematic-debugging
mode: SOLO
estimated_minutes: 105
technology_depth: core
resource_ids:
- php-fpm-manual
- php-errors-exceptions
deliverables:
- incident evidence plan
- safe runtime experiment
- Project A troubleshooting appendix
review_policy: adaptive
prerequisites:
- week-04
status: planned
---

# Day 05 — Observe Runtime Failures With Logs, Status, and Slow Evidence

## Outcome

> Understand the PHP web runtime from request arrival through FPM/process execution, configuration, Composer bootstrap, and application response.

## Timebox

| Block | Mode | Minutes |
|---|---|---:|
| Runtime observability reading | `SOLO` | 20 |
| Evidence-first incident drill | `SOLO` | 35 |
| Safe local experiment | `SOLO` | 20 |
| Project evidence update | `SOLO` | 10 |
| Daily micro-assessment | `SOLO` | 20 |
| **Total** |  | **105** |

Assessment time is included in this total.

## Resources

- `php-fpm-manual`
- `php-errors-exceptions`

Resource IDs resolve through `09 Resources/catalog.yaml`.

## Activities

### Runtime observability reading — 20 min — `SOLO`

Study FPM logs/status/slowlog concepts and PHP error logging, including status-page exposure risk.

### Evidence-first incident drill — 35 min — `SOLO`

For a synthetic slow request, rank hypotheses and state the exact evidence to gather.

### Safe local experiment — 20 min — `SOLO`

Create a small slow/failing sandbox script and capture available timing/log evidence.

### Project evidence update — 10 min — `SOLO`

Add a runtime troubleshooting appendix to the Project A lifecycle map.

### Daily micro-assessment — 20 min — `SOLO`

Complete the runtime-observability assessment.

## Deliverables

- incident evidence plan
- safe runtime experiment
- Project A troubleshooting appendix

## Daily assessment

Run `02 Daily Assessments/Week 05/Day 05.md`. Store learner attempts privately.

## Review hook

Create D+1/D+7 review events from demonstrated errors; add D+30 transfer review when justified.

## AI integrity

SOLO work remains independent evidence. HYBRID/AI-assisted work must preserve pre-agent evidence and independently validate consequential claims.

## Completion rule

Reading or agent conversation alone is not completion; required evidence must exist.
