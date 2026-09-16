---
type: question-bank
schema_version: 1
bank: week-0-diagnostic
domain: mysql-core
question_ids:
- diag-mysql-model-001
- diag-mysql-explain-001
- diag-mysql-tx-001
answer_key_public: false
---

# MySQL Core — Week 0 Diagnostic

These prompts diagnose entry depth. They are not public teaching examples and contain no answer keys.

## `diag-mysql-model-001`

| Field | Value |
|---|---|
| Domain | `mysql-core` |
| Mode | `SOLO` |
| Assessment type | `coding-implementation` |
| Difficulty | `diagnostic` |
| Estimated minutes | 35 |

### Prompt

Design a relational model for a small order system with customers, orders, order items, and products.

Requirements:
- identify primary/foreign keys;
- represent quantity and price-at-purchase safely;
- state at least two integrity constraints;
- write one query that returns a customer's last 20 orders with total value;
- explain one denormalization you would *not* introduce yet.

Focus on correctness and modeling trade-offs rather than framework ORM syntax.

### Submission rule

Store the raw attempt privately. Do not append a model answer to this public question.

## `diag-mysql-explain-001`

| Field | Value |
|---|---|
| Domain | `mysql-core` |
| Mode | `SOLO` |
| Assessment type | `sql-debugging` |
| Difficulty | `diagnostic` |
| Estimated minutes | 35 |

### Prompt

A table `events` has tens of millions of rows:

```sql
CREATE TABLE events (
  id BIGINT PRIMARY KEY,
  account_id BIGINT NOT NULL,
  kind VARCHAR(50) NOT NULL,
  occurred_at DATETIME NOT NULL,
  payload JSON NOT NULL
);
```

A frequent query is:

```sql
SELECT id, kind, occurred_at
FROM events
WHERE account_id = ?
  AND occurred_at >= ?
ORDER BY occurred_at DESC
LIMIT 100;
```

Describe how you would use `EXPLAIN`/execution evidence to reason about the access path. Propose an index only after stating what you expect it to improve, and discuss one index cost/trade-off.

### Submission rule

Store the raw attempt privately. Do not append a model answer to this public question.

## `diag-mysql-tx-001`

| Field | Value |
|---|---|
| Domain | `mysql-core` |
| Mode | `SOLO` |
| Assessment type | `conceptual` |
| Difficulty | `diagnostic` |
| Estimated minutes | 25 |

### Prompt

Two workers can reserve the last unit of stock concurrently.

Describe a transaction-safe approach that prevents overselling. Explain:
- what data is read/updated;
- what concurrency anomaly you are preventing;
- what locking/isolation behavior you rely on;
- how you would test the race rather than assuming the transaction is correct.

### Submission rule

Store the raw attempt privately. Do not append a model answer to this public question.
