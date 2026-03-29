# 🛡️ 04. Security & Ops
>
> **Standard:** v3.3.1-S "Industrial Core"

## 1. Secret Management

> [!CAUTION]
> NEVER commit `.env` files, API keys, or credentials. Mandatory use of `agentic-thought-secret-scanner` before every phase transition and commit.

## 2. Docker Proof-of-Build

- Every application must be containerized and defined in `docker-compose.yml`.
- "Works on my machine" is an invalid state; "Works in the Central Node" is the requirement.
- Use multi-stage builds for minimal image size.

## 3. Human-in-the-Loop Mutation Gate

> [!CAUTION]
> MODIFICATION OF `06_SKILL_LIBRARY/` IS FORBIDDEN WITHOUT EXPLICIT HUMAN APPROVAL.
> Any skill update must include a solidity audit report before authorization.

## 4. Resource Observability

- **Monitoring**: Access real-time factory health via centralized logs and performance scores.
- **Resource Control**: Mandatory limits in all deployment descriptors.
- **Structured logging**: Include `correlation_id`, `agent_id`, and `task_id` in every log entry.
- **Aduana Universal**: Mandatory execution of `kanban-solidity-gate` for all phase transitions to verify physical proofs and Audit Signatures.

## 5. Zero Hardcoding

All paths must be relative to `$TARGET_PROJECT`. The factory logic is project-agnostic. Use `DOCS/` hierarchy for all documentation artifacts.

---
*Security & Ops v3.3.1-S | dasafo_FACTORY.*
