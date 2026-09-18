---
type: daily-plan
schema_version: 1
id: task-w37-d05-v1-1
week: 37
day: 5
date: null
track: core
skill_ids:
- tool-calling
- python
- authorization
- human-approval
mode: HYBRID
estimated_minutes: 105
technology_depth: core
resource_ids:
- openai-function-calling-guide
deliverables:
- SOLO attack set
- agent adversarial set
- verified rejections
review_policy: adaptive
prerequisites:
- week-36
status: planned
---

# Day 05 — Run Adversarial Tool-Call Tests With Agent Assistance

## Outcome

> Freeze SOLO attack cases first, then use an agent to generate additional malicious/ambiguous prompts and verify the application rejects unsafe actions.

## Timebox

| Block | Mode | Minutes |
|---|---|---:|
| SOLO baseline | `SOLO` | 25 |
| Agent challenge | `AI-ASSISTED` | 20 |
| Independent validation | `SOLO` | 20 |
| Project evidence | `SOLO` | 20 |
| Daily assessment | `SOLO` | 20 |
| **Total** |  | **105** |

## Resources

- `openai-function-calling-guide`

## Activities

### SOLO baseline — 25 min — `SOLO`

Freeze SOLO attack cases first, then use an agent to generate additional malicious/ambiguous prompts and verify the application rejects unsafe actions. Freeze your first plan/evidence before agent use.

### Agent challenge — 20 min — `AI-ASSISTED`

Ask for critique/alternatives only; require assumptions.

### Independent validation — 20 min — `SOLO`

Verify consequential claims through code/tests/data/traces/primary sources.

### Project evidence — 20 min — `SOLO`

Apply only validated conclusions.

### Daily assessment — 20 min — `SOLO`

Complete the scored transfer prompt without assistance.

## Deliverables

- SOLO attack set
- agent adversarial set
- verified rejections

## Daily assessment

Run `02 Daily Assessments/Week 37/Day 05.md`. Store attempts privately.

## Review hook

Create D+1/D+7 reviews from demonstrated errors and D+30 transfer review where justified.

## AI integrity

Scored attempts are SOLO. HYBRID work preserves independent evidence before agent use.

## Completion rule

Required evidence must exist; reading or agent conversation alone is not completion.
