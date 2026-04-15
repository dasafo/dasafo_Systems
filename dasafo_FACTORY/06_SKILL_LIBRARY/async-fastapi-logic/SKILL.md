> [ ⬆️ Up: [[../MOC_SKILL_LIBRARY]] | 📂 Skill: **async-fastapi-logic** ]
---
version: v5.0-MCP (Native)
agent_authorization: [AI_ENGINEER, BACKEND_DEV]
production_category: BUILD
source: https://skills.sh/jezweb/claude-skills/fastapi
protocol: DDD-Async / DAST
---

> [ ⬆️ Up: [[../MOC_SKILL_LIBRARY]] | 📂 Global: [[../../_dasafo_FACTORY]] ]


# ⚡ Skill | async-fastapi-logic

## Objective

Design and implement high-performance async microservices using FastAPI, enforcing strict Pydantic validation and Domain-Driven Design (DDD).

## 🛠️ Interface (v5.0-MCP Native)

**MANDATORY:** Use direct arguments. The `params_json` structure is **DEPRECATED**.

### Typed Parameters

- `agent` (string): Your authorized Agent ID (AI_ENGINEER, BACKEND_DEV).
- `target_project` (string): Path to project root.
- `action` (enum): `scaffold`, `add_domain`, `add_endpoint`.
- `domain_name` (string): Name of the business domain (e.g., 'billing').
- `route_name` (string): Function name for the endpoint.
- `method` (string): HTTP method (default: 'GET').
- `overwrite` (boolean): Bypass Redundancy Lock.
- `isolate` (boolean): Execution in Clean Session.

## 🛡️ Industrial Constraints

- **Async Enforcement:** All I/O operations MUST be non-blocking (`async def`).
- **SI Standards:** Report all technical performance in **seconds (s)**.
- **DAST Sovereignty:** Logic must reside strictly in `WORKSPACE/backend/src/`.
- **Secret Zero-Leak:** No hardcoded secrets; use environment variables.

---

> [ ⬆️ Up: [[../MOC_SKILL_LIBRARY]] | 📂 Global: [[../../_dasafo_FACTORY]] ]

**ORIGIN:** [fastapi by jezweb](https://skills.sh/jezweb/claude-skills/fastapi)
