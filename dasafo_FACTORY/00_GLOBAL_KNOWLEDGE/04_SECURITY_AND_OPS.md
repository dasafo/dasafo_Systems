# 🛡️ 04_SECURITY_AND_OPS

## 1. Secret Management
> [!CAUTION]
> NEVER commit `.env` files, API keys, or JWT tokens. Use the `agentic-thought-secret-scanner` before every commit.

## 2. Docker Proof-of-Build
- Every application must be containerized.
- "Works on my machine" is invalid; "Works in Docker" is the requirement.
- Use multi-stage builds for minimal image size.

## 3. Resource Observability
- Monitor CPU/Memory usage via `DEPLOYMENT_MONITOR`.
- Structured logging: Include `correlation_id`, `use_case`, and `entity_id` in every log entry.

## 4. Zero Hardcoding
All paths must be relative to `$TARGET_PROJECT`. The factory logic is project-agnostic and should never be modified to support a specific project instance.
