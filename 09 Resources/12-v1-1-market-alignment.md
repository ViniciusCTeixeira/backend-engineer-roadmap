# V1.1 Market Alignment Resources

**Verified:** 2026-09-18

This page groups resources added or promoted by the V1.1 US-market alignment amendment.

## Core additions

### PostgreSQL

- `postgresql-18-manual`
- `postgresql-explain`
- `postgresql-mvcc`

Project B uses PostgreSQL continuously after the dual-relational Weeks 9–11.

### Python / FastAPI

- `python-314-docs`
- `fastapi-tutorial`
- `fastapi-testing`

Python is a secondary backend core, reinforced again in Weeks 36–40.

## Supporting additions

### gRPC / Protobuf

- `grpc-docs`
- `grpc-python-basics`

REST/OpenAPI remains the default external API path.

### MongoDB

- `mongodb-data-modeling`
- `mongodb-indexes`
- `mongodb-sharding`

MongoDB is taught as document/access-pattern modeling, not as "SQL without joins."

### DynamoDB

- `aws-dynamodb-data-modeling`

The lab starts from required access patterns and partition distribution.

### Kubernetes

- `kubernetes-basics`
- `kubernetes-application-basics`

V1.1 promotes application-level Kubernetes from professional exposure to supporting.

## Professional exposure

- `graphql-learn`
- `go-127-docs`
- `spring-boot-current`
- `nodejs-releases`
- `typescript-handbook`
- `cassandra-data-modeling`

The expected evidence is code reading, architecture mapping, build/run/test discovery, and bounded changes.

## Observability

- `otel-python`

The Week 30 observability path now covers the Laravel/PHP path and the bounded Python service.

## Freshness notes

At verification time:

- PostgreSQL 18.6 is the current supported PostgreSQL line;
- Python documentation is on 3.14.7;
- Go 1.27.1 is the current 1.27 patch line;
- Spring Boot 4.1.1 is current stable;
- Node.js v24 is LTS and v26 is Current;
- Kubernetes 1.37 is the latest active release line.

Curriculum tasks should avoid depending on point-release-only behavior unless explicitly required.
