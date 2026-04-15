> [ ⬆️ Up: [[../MOC_SKILL_LIBRARY]] | 📂 Skill: **kanban-solidity-gate** ]
---
version: v5.0-MCP (Native)
agent_authorization: [ORCHESTRATOR]
production_category: PLAN
source: https://skills.sh/supercent-io/skills-template/vibe-kanban
protocol: Phase-Gate / DAST
---

# 🛂 Skill | kanban-solidity-gate

## Objective
Enforce the 'Zero-Pending Rule' for phase transitions and orchestrate the **Vibe Kanban** dashboard. Acts as the industrial customs (Aduana) for project solidity.

## 🛠️ Interface (v5.0-MCP Native)
- **agent**: 'ORCHESTRATOR'
- **target_project**: Path to project root.
- **action**: `audit` | `start_dashboard`
- **port**: Default 3001.

## 🛡️ Industrial Constraints
- Registry status is irrelevant without physical JSON artifacts.
- The dashboard must exactly reflect the disk state.
