---
version: v5.0-MCP (Native)
agent_authorization: [BACKEND_DEV]
production_category: BUILD
protocol: Layered-Architecture / DAST
---

# ⚙️ Skill | nodejs-backend-patterns

## Objective

Enforce industrial-grade Node.js/TypeScript design patterns (Repository, DTOs, Service Layer) and TDD. Ensures architectural purity and separation of concerns.

## 🛠️ Interface (v5.0-MCP Native)

**MANDATORY:** Use typed arguments. `params_json` is **DEPRECATED**.

### Typed Parameters

- `agent` (string): Your Agent ID (BACKEND_DEV).
- `target_project` (string): Path to project root.
- `module_name` (string): (Optional) The domain module name (default: 'core').
- `isolate` (boolean): Execution in Clean Session.

## 🛡️ Industrial Constraints

- **Physical Verification:** Must confirm the presence of `package.json` in `WORKSPACE/backend/`.
- **TDD Mandate:** Every service MUST have a corresponding test file in `tests/`.
- **SI Standards:** Timing metrics MUST be in **Seconds (s)**.
- **Clean Separation:** Mixing controller logic with repository queries is a **Cultural Violation**.

---
*Standard v5.0-MCP | Dasafo Factory Production Hub.*
