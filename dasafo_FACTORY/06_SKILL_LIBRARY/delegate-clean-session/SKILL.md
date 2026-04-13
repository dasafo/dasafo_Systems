---
version: v5.0-MCP (Native)
agent_authorization: [ORCHESTRATOR]
production_category: BUILD
source: internal/core-orchestration
protocol: Context-Isolation / DAST
---

> [ ⬆️ Up: [[../MOC_SKILL_LIBRARY]] | 📂 Global: [[../../_dasafo_FACTORY]] ]


# 🚀 Skill | delegate-clean-session

## Objective

Spawn a specialized sub-agent (Peon) in a "Clean Slate" environment. Prevents the high-level Orchestrator context from being polluted by implementation noise.

## 🛠️ Interface (v5.0-MCP Native)

**MANDATORY:** Use typed parameters. `params_json` is **DEPRECATED**.

### Typed Parameters

- `agent` (string): Your ID (must be 'ORCHESTRATOR').
- `target_project` (string): Path to project root.
- `spec_path` (string): Relative path to task spec (e.g., `TASKS/01_PENDING/M3-001.json`).
- `agent_type` (string): Target specialized agent (e.g., 'BACKEND_DEV').
- `isolate` (boolean): Always `true` for this skill.

## 🛡️ Industrial Constraints

- **Auto-Start Mandate:** The task file MUST be moved physically to `02_IN_PROGRESS`.
- **Immunization:** Skill MUST query Neo4j for JIT "Golden Rules" injection.
- **DAST Sovereignty:** No delegation is valid without a physical `SPEC_LITE.json` on disk.

---

> [ ⬆️ Up: [[../MOC_SKILL_LIBRARY]] | 📂 Global: [[../../_dasafo_FACTORY]] ]

*Standard v5.0-MCP | Dasafo Factory Core Orchestration.*
