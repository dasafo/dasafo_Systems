# 🛡️ 04. Security & Ops
>
> **Standard:** v3.2.0-S "Solidity Guard"

## 1. Secret Management
> [!CAUTION]
> NEVER commit `.env` files, API keys, or JWT tokens. Use the `agentic-thought-secret-scanner` before every commit.

## 2. Docker Proof-of-Build
- Every application must be containerized.
- "Works on my machine" is invalid; "Works in Docker" is the requirement.
- Use multi-stage builds for minimal image size.

## 3. Resource Observability (v3.2.0-S)
- **Monitoring**: Access real-time factory health via **Glances (Port 61208)**.
- **Resource Control**: Mandatory `deploy.resources.limits` in all `docker-compose.yml` files.
- **Structured logging**: Include `correlation_id`, `use_case`, and `entity_id` in every log entry.
- **Anti-Fraud Guardrails**: Mandatory execution of `kanban-solidity-gate` for all phase transitions to verify Audit Signatures and prevent status cheating.

## 4. Zero Hardcoding
All paths must be relative to `$TARGET_PROJECT`. The factory logic is project-agnostic and should never be modified to support a specific project instance.
