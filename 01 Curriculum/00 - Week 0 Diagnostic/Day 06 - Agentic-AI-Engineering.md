---
type: diagnostic-day
schema_version: 1
day: 6
required: true
estimated_minutes: 140
domains:
- agentic-development
- llm-ai-engineering
status: planned
---

# Day 06 — Agentic Development and AI Engineering

## Purpose

Execute the approved Week 0 diagnostic blocks for this day. This is evidence collection, not a pass/fail gate.

## Timebox

| Block | Mode | Minutes |
|---|---|---:|
| Repository task with coding agent | `HYBRID` | 50 |
| Independent diff/risk review | `SOLO` | 25 |
| Accepted/rejected changes explanation | `SOLO` | 20 |
| LLM/API/tool-calling concepts | `SOLO` | 25 |
| AI system-design mini-scenario | `SOLO` | 20 |
| **Total** |  | **140** |

This day is required. Stop when the timebox expires rather than expanding the task indefinitely.

## Question IDs

- `diag-agentic-001`
- `diag-agentic-review-001`
- `diag-agentic-explain-001`
- `diag-llm-001`
- `diag-ai-design-001`

Resolve each ID under `04 Question Bank/diagnostic/`.

## Assessment integrity

- SOLO means no LLM/coding-agent/search for solutions.
- HYBRID means preserve/freeze the first SOLO evidence before agent assistance.
- If help is needed during a SOLO assessment, mark that attempt `abandoned` before receiving teaching/solution help.
- Raw attempts are immutable after submission.
- Public question files contain no answer keys.

## Blocks

### Repository task with coding agent — 50 min — `HYBRID`

Preserve a SOLO task plan and baseline before using Codex/Claude Code.

Question IDs:
- `diag-agentic-001`
### Independent diff/risk review — 25 min — `SOLO`

Review the generated diff without asking the agent to explain itself first.

Question IDs:
- `diag-agentic-review-001`
### Accepted/rejected changes explanation — 20 min — `SOLO`

Explain consequential changes and rejected suggestions from your own understanding.

Question IDs:
- `diag-agentic-explain-001`
### LLM/API/tool-calling concepts — 25 min — `SOLO`

Answer core integration concepts without an LLM.

Question IDs:
- `diag-llm-001`
### AI system-design mini-scenario — 20 min — `SOLO`

Design a small AI-enabled backend flow and identify evaluation/security/cost risks.

Question IDs:
- `diag-ai-design-001`

## Private evidence

For each scored evidence event, create a private record from:

`90 Templates/diagnostic-result.md`

Store it under `.study/assessments/diagnostic/` (or the equivalent documented private assessment location).

## Completion

The day is complete when the required raw attempts/evidence are stored privately, assistance is declared accurately, and confidence self-report is recorded for assessed domains.
