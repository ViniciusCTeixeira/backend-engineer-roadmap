---
type: daily-plan
schema_version: 1
id: task-w05-d01-php-runtime-and-fpm
week: 5
day: 1
date: null
track: core
skill_ids:
- php-runtime
- php-sapi
- runtime-state
mode: SOLO
estimated_minutes: 105
technology_depth: core
resource_ids:
- php-supported-versions
- php-fpm-manual
deliverables:
- runtime vocabulary map
- prediction-vs-observation table
- Project A runtime inventory
review_policy: adaptive
prerequisites:
- week-04
status: planned
---

# Day 01 — Distinguish PHP CLI, SAPI, and Long-Lived Runtime Assumptions

## Outcome

> Understand the PHP web runtime from request arrival through FPM/process execution, configuration, Composer bootstrap, and application response.

## Timebox

| Block | Mode | Minutes |
|---|---|---:|
| Primary-source reading | `SOLO` | 20 |
| Prediction-first runtime experiments | `SOLO` | 40 |
| Project runtime inventory | `SOLO` | 15 |
| Technical English | `SOLO` | 10 |
| Daily micro-assessment | `SOLO` | 20 |
| **Total** |  | **105** |

Assessment time is included in this total.

## Resources

- `php-supported-versions`
- `php-fpm-manual`

Resource IDs resolve through `09 Resources/catalog.yaml`.

## Activities

### Primary-source reading — 20 min — `SOLO`

Read the PHP runtime/FPM overview and build a vocabulary map for SAPI, process, request, configuration, and worker.

### Prediction-first runtime experiments — 40 min — `SOLO`

Compare separate CLI invocations with a small script that mutates globals/statics/environment. Predict persistence before running.

### Project runtime inventory — 15 min — `SOLO`

Identify the modernization lab entry point, bootstrap files, environment/config files, and runtime assumptions.

### Technical English — 10 min — `SOLO`

Summarize the observed execution model in English without translation.

### Daily micro-assessment — 20 min — `SOLO`

Complete the closed runtime-model assessment.

## Deliverables

- runtime vocabulary map
- prediction-vs-observation table
- Project A runtime inventory

## Daily assessment

Run `02 Daily Assessments/Week 05/Day 01.md`. Store learner attempts privately.

## Review hook

Create D+1/D+7 review events from demonstrated errors; add D+30 transfer review when justified.

## AI integrity

SOLO work remains independent evidence. HYBRID/AI-assisted work must preserve pre-agent evidence and independently validate consequential claims.

## Completion rule

Reading or agent conversation alone is not completion; required evidence must exist.
