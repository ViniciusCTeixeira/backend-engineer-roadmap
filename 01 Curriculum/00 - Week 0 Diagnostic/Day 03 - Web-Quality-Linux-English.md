---
type: diagnostic-day
schema_version: 1
day: 3
required: true
estimated_minutes: 140
domains:
- http-api-security
- testing-static-analysis
- linux-networking
- english-technical
status: planned
---

# Day 03 — Web Engineering, Quality, Linux, and Written English

## Purpose

Execute the approved Week 0 diagnostic blocks for this day. This is evidence collection, not a pass/fail gate.

## Timebox

| Block | Mode | Minutes |
|---|---|---:|
| HTTP request/response analysis | `SOLO` | 30 |
| API/security scenario | `SOLO` | 30 |
| Testing/static analysis | `HYBRID` | 35 |
| Linux/network troubleshooting | `SOLO` | 25 |
| Technical English — written | `SOLO` | 20 |
| **Total** |  | **140** |

This day is required. Stop when the timebox expires rather than expanding the task indefinitely.

## Question IDs

- `diag-http-001`
- `diag-api-security-001`
- `diag-testing-001`
- `diag-linux-001`
- `diag-english-written-001`

Resolve each ID under `04 Question Bank/diagnostic/`.

## Assessment integrity

- SOLO means no LLM/coding-agent/search for solutions.
- HYBRID means preserve/freeze the first SOLO evidence before agent assistance.
- If help is needed during a SOLO assessment, mark that attempt `abandoned` before receiving teaching/solution help.
- Raw attempts are immutable after submission.
- Public question files contain no answer keys.

## Blocks

### HTTP request/response analysis — 30 min — `SOLO`

Analyze protocol semantics from a concrete request/response scenario.

Question IDs:
- `diag-http-001`
### API/security scenario — 30 min — `SOLO`

Identify design/security risks and mitigations without framework-specific shortcuts.

Question IDs:
- `diag-api-security-001`
### Testing/static analysis — 35 min — `HYBRID`

Phase A is SOLO and must be frozen before Phase B agent critique.

Question IDs:
- `diag-testing-001`
### Linux/network troubleshooting — 25 min — `SOLO`

Use a hypothesis/evidence command sequence rather than a command dump.

Question IDs:
- `diag-linux-001`
### Technical English — written — 20 min — `SOLO`

Write the requested engineering explanation in English without translation tools.

Question IDs:
- `diag-english-written-001`

## Private evidence

For each scored evidence event, create a private record from:

`90 Templates/diagnostic-result.md`

Store it under `.study/assessments/diagnostic/` (or the equivalent documented private assessment location).

## Completion

The day is complete when the required raw attempts/evidence are stored privately, assistance is declared accurately, and confidence self-report is recorded for assessed domains.
