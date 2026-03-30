---
version: 3.4.0-S
agent: BACKEND_DEV / ARCHITECT
source: https://skills.sh/jezweb/claude-skills/fastapi
---

# ⚡ Skill | Async FastAPI & Domain Logic

## Objective

Design, scaffold, and implement high-performance, maintainable asynchronous microservices using FastAPI. This skill enforces Domain-Driven Design (DDD), strict Pydantic validation, and efficient async I/O patterns to ensure production-grade reliability.

## 🛠️ Interface (v3.4.0-S)

### Input Schema (SkillInput.params)

- `action` (string, optional): "scaffold" (default) | "add_domain" | "add_endpoint".
  - `scaffold`: Initialize a full domain-based project structure.
  - `add_domain`: Create a new domain folder with schemas, models, and service logic.
  - `add_endpoint`: Add a specific async route to an existing domain router.
- `domain_name` (string, required for "add_domain"): Name of the domain (e.g., `identity`, `billing`).
- `route_name` (string, required for "add_endpoint"): Name of the endpoint function.
- `method` (string, optional): HTTP Method (GET, POST, etc.). Default "GET".
- `target_project` (string, optional): Absolute path to the active project.

### Output Schema (SkillOutput.result)

- `status`: (string) "SCAFFOLDED" | "DOMAIN_ADDED" | "ENDPOINT_SOLIDIFIED"
- `artifacts_created`: (list) Paths to the generated files.
- `compliance_report`:
  - `async_enforced`: (boolean)
  - `ppp_validation`: (string) "Pydantic-SQLAlchemy-Pattern Verified"
- `summary`: (string) Brief recap of the implementation changes.

### ⚖️ Mandato SI (Sistema Internacional)

Cualquier métrica técnica definida (timeouts, cuotas de almacenamiento, límites de memoria) debe expresarse estrictamente en el Sistema Internacional (segundos, bytes).

## 🛡️ Industrial Constraints (Zero-Trust)

- **Strict SoC:** Pydantic schemas MUST be separated from SQLAlchemy models. Mixing them is FORBIDDEN.
- **Async Only:** All I/O operations (database, external requests) MUST use `async def` and non-blocking libraries (e.g., `httpx`, `asyncpg`).
- **Secret Zero-Leak:** Secrets must never be hardcoded. Use `pydantic-settings` or environment variables exclusively.
- **Redundancy Lock:** Skill fails if it tries to overwrite established domain structures without `overwrite: true`.

## 🧠 Core Patterns (v3.4.0-S)

1. **Scaffold Structure:** Organize by domain (`src/domain/`), not by file type.
2. **Async Database:** Use SQLAlchemy 2.0 with `AsyncSession` for all relational persistence.
3. **Pydantic Validation:** Utilize `Field()` constraints for all DTOs and input validation.
4. **Dependency Injection:** Use `Depends()` for database sessions, authentication, and shared logic.

---
**ORIGIN:** [fastapi by jezweb](https://skills.sh/jezweb/claude-skills/fastapi)
*Skill v3.4.0-S | Status: Standardized & Industrialized (Dasafo Edition).*
