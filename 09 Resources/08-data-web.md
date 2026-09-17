# Data & Web Resources — Weeks 9–16

**Verified:** 2026-09-16

| ID | Resource | Depth | URL |
|---|---|---|---|
| `mysql-indexes-manual` | MySQL 8.4 — Optimization and Indexes | core | https://dev.mysql.com/doc/refman/8.4/en/optimization-indexes.html |
| `mysql-explain-manual` | MySQL 8.4 — EXPLAIN Statement | core | https://dev.mysql.com/doc/refman/8.4/en/explain.html |
| `mysql-innodb-transactions` | MySQL 8.4 — InnoDB Locking and Transaction Model | core | https://dev.mysql.com/doc/refman/8.4/en/innodb-locking-transaction-model.html |
| `redis-transactions` | Redis — Transactions | core | https://redis.io/docs/latest/develop/using-commands/transactions/ |
| `redis-pipelining` | Redis — Pipelining | supporting | https://redis.io/docs/latest/develop/using-commands/pipelining/ |
| `rfc9110-http-semantics` | RFC 9110 — HTTP Semantics | core | https://www.rfc-editor.org/rfc/rfc9110.html |
| `rfc9111-http-caching` | RFC 9111 — HTTP Caching | core | https://www.rfc-editor.org/rfc/rfc9111.html |
| `bruno-openapi` | Bruno — OpenAPI and Import | supporting | https://docs.usebruno.com/open-api/overview |
| `postman-collections` | Postman — Create and Manage Collections | supporting | https://learning.postman.com/docs/use/use-collections/overview |
| `owasp-api-security-2023` | OWASP API Security Top 10 — 2023 | core | https://api-security.owasp.org/editions/2023/en/0x11-t10/ |
| `rfc6749-oauth2` | RFC 6749 — OAuth 2.0 Authorization Framework | core | https://www.rfc-editor.org/rfc/rfc6749.html |
| `rfc9700-oauth-security` | RFC 9700 — OAuth 2.0 Security Best Current Practice | core | https://www.rfc-editor.org/rfc/rfc9700.html |
| `openid-connect-core` | OpenID Connect Core 1.0 | core | https://openid.net/specs/openid-connect-core-1_0-18.html |
| `rfc7519-jwt` | RFC 7519 — JSON Web Token (JWT) | core | https://www.rfc-editor.org/rfc/rfc7519.html |

## Existing catalog resources reused

- `mysql-84-manual`
- `redis-data-types`
- `redis-persistence`
- `redis-eviction`
- `openapi-spec`
- `phpunit-writing-tests`
- `phpstan-getting-started`

## Selection notes

- MySQL 8.4 LTS documentation is primary for indexes, query plans, transactions and locking.
- Redis official docs are selected by data-model/failure semantics, not by generic cache familiarity.
- HTTP uses RFC 9110/9111 as protocol sources.
- OpenAPI is the contract standard; Bruno is the primary Git-friendly hands-on client, with bounded Postman comparison exposure.
- OAuth concepts use RFC 6749 plus RFC 9700 current security BCP; OpenID Connect Core distinguishes authentication/identity from authorization.
- OWASP API Security Top 10 is threat-awareness input, not proof that a vulnerability exists.
- PHPUnit and PHPStan remain core quality tooling.
