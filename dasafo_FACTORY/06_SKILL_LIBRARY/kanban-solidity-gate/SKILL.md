---
version: v5.0-MCP (Native)
agent_authorization: [ORCHESTRATOR]
production_category: PLAN
source: https://skills.sh/supercent-io/skills-template/vibe-kanban
protocol: Phase-Gate / DAST
---

> [ ⬆️ Up: [[../MOC_SKILL_LIBRARY]] | 📂 Global: [[../../_dasafo_FACTORY]] ]


# 🛂 Skill | kanban-solidity-gate

## Objective

Enforce the "Zero-Pending Rule" for phase transitions and orchestrate the **Vibe Kanban** dashboard. Acts as the industrial customs (Aduana) for project solidity.

## 🛠️ Interface (v5.0-MCP Native)

**MANDATORY:** Use direct arguments. Generic `params_json` is **DEPRECATED**.

### Typed Parameters

- `agent` (string): Your ID (must be 'ORCHESTRATOR').
- `target_project` (string): Path to project root.
- `action` (enum): `audit` (default) | `start_dashboard`.
- `port` (integer): (Optional) Dashboard port (default: 3001).
- `isolate` (boolean): Always `false` as it needs project persistence.

## 🛡️ Industrial Constraints

- **Physical SSoT:** Registry status is irrelevant without the physical `.json` artifact in `03_COMPLETED/`.
- **SI Standards:** All metrics strictly in **Seconds (s)**.
- **Zero-Ghost Tasks:** The dashboard must exactly reflect the disk state.

---

> [ ⬆️ Up: [[../MOC_SKILL_LIBRARY]] | 📂 Global: [[../../_dasafo_FACTORY]] ]

**ORIGIN:** [vibe-kanban by supercent-io](https://skills.sh/supercent-io/skills-template/vibe-kanban)
