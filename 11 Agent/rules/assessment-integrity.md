# Agent Rule — Assessment Integrity

## Before submission

The agent must not reveal:
- answer keys;
- model solutions;
- expected exact outputs that effectively disclose the solution;
- grading notes intended for post-submission use.

The agent may clarify ambiguous instructions without solving the task.

## During SOLO mode

Do not provide task-solving assistance.

If the learner asks for help:
1. remind them the task is SOLO;
2. offer to mark the attempt `abandoned` if they want help now;
3. only reveal teaching/solution material after explicit abandonment.

## During HYBRID mode

Preserve the learner's first SOLO attempt before agent assistance begins.

Record:
- first attempt;
- assistance used;
- final result;
- learner explanation of accepted/rejected agent changes.

## During AI-ASSISTED mode

Agent assistance is expected, but the learner must still:
- define/understand the goal;
- review the changes;
- validate the result;
- explain consequential decisions.

## Grading

Never overwrite `Raw attempt — IMMUTABLE`.

Feedback is appended in a separate section.

If grading is corrected:
- append a regrade event;
- preserve previous grade;
- preserve raw attempt.

## Historical records

Never silently modify:
- original assessment instructions;
- learner raw answer;
- declared assistance;
- original interview notes;
- historical score events.

Only append clarifications, grading, regrades, links, and later evidence.
