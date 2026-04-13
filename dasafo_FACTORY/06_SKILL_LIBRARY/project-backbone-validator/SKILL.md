---
version: v5.0-MCP (Native)
agent_authorization: [ORCHESTRATOR]
production_category: VERIFY
source: internal/backbone-validator
protocol: Scaffolding-Guard / DAST
---

> [ ⬆️ Up: [[../MOC_SKILL_LIBRARY]] | 📂 Global: [[../../_dasafo_FACTORY]] ]


# 🏗️ Skill | project-backbone-validator

## Objective

Act as the "Inspector de Obra" for the factory. Ensure that the necessary framework scaffolding physically exists on disk before any atomic implementation agent is dispatched.

## 🛠️ Interface (v5.0-MCP Native)

**MANDATORY:** Use typed arguments. `params_json` is **DEPRECATED**.

### Typed Parameters

- `agent` (string): Your Agent ID (must be 'ORCHESTRATOR').
- `target_project` (string): Absolute path to the project root.
- `action` (enum): `validate_structure` (default). Validates the physical scaffolding.
- `schema_version` (string): (Optional) Schema version to validate against (default: 'v1').
- `isolate` (boolean): Execution in Clean Session.

## 🛡️ Industrial Constraints

- **Physical Truth (DAST):** Always inspect the file system directly. Do not rely on assumed context.
- **SI Standards:** All timing metrics strictly in **Seconds (s)**.
- **Gatekeeper Mandate:** If scaffolding is incomplete, this skill blocks the delegation pipeline.

---

> [ ⬆️ Up: [[../MOC_SKILL_LIBRARY]] | 📂 Global: [[../../_dasafo_FACTORY]] ]

*Standard v5.0-MCP | Dasafo Factory Core DAST.*
