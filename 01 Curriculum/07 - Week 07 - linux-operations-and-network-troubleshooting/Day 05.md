---
type: daily-plan
schema_version: 1
id: task-w07-d05-linux-operations-and-network-troubleshooting
week: 7
day: 5
date: null
track: core
skill_ids:
- lsof
- jq
- log-inspection
- systematic-debugging
- agent-supervision
mode: HYBRID
estimated_minutes: 105
technology_depth: core
resource_ids:
- lsof-manpage
- jq-manual
- linux-ss-manpage
deliverables:
- evidence correlation worksheet
- agent alternative hypotheses
- accepted/rejected hypothesis note
review_policy: adaptive
prerequisites:
- week-06
status: planned
---

# Day 05 — Correlate Processes, Open Files, JSON, and Logs

## Outcome

> Operate comfortably in Linux and troubleshoot PHP service failures through processes, files, permissions, ports, DNS, HTTP evidence, and logs.

## Timebox

| Block | Mode | Minutes |
|---|---|---:|
| Tool reading | `SOLO` | 20 |
| Evidence-correlation lab | `SOLO` | 35 |
| Agent challenge | `AI-ASSISTED` | 20 |
| Comparison | `SOLO` | 10 |
| Daily micro-assessment | `SOLO` | 20 |
| **Total** |  | **105** |

Assessment time is included in this total.

## Resources

- `lsof-manpage`
- `jq-manual`
- `linux-ss-manpage`

Resource IDs resolve through `09 Resources/catalog.yaml`.

## Activities

### Tool reading — 20 min — `SOLO`

Learn enough `lsof`, `jq`, and log filtering to answer specific evidence questions.

### Evidence-correlation lab — 35 min — `SOLO`

Use synthetic JSON logs plus process/socket evidence to select the most supported hypothesis.

### Agent challenge — 20 min — `AI-ASSISTED`

After freezing your conclusion, ask an agent for competing hypotheses only; prohibit destructive commands.

### Comparison — 10 min — `SOLO`

Record which agent hypothesis merits testing and which lacks evidence.

### Daily micro-assessment — 20 min — `SOLO`

Complete the correlation/agent-supervision assessment.

## Deliverables

- evidence correlation worksheet
- agent alternative hypotheses
- accepted/rejected hypothesis note

## Daily assessment

Run `02 Daily Assessments/Week 07/Day 05.md`. Store learner attempts privately.

## Review hook

Create D+1/D+7 review events from demonstrated errors; add D+30 transfer review when justified.

## AI integrity

SOLO work remains independent evidence. HYBRID/AI-assisted work must preserve pre-agent evidence and independently validate consequential claims.

## Completion rule

Reading or agent conversation alone is not completion; required evidence must exist.
