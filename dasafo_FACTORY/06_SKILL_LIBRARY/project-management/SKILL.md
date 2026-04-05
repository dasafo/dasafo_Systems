---
version: v5.0-MCP (Native)
agent_authorization: [ORCHESTRATOR, PRODUCT_OWNER]
production_category: PLAN
source: https://skills.sh/googleworkspace/cli/persona-project-manager
protocol: Project-Coordination / DAST
---

# 📅 Skill | project-management

## Objective

Coordinate industrial projects through task tracking and automated status logging. Integrates directly with `registry.json` and `PROJECT_STATE.json` to ensure 100% factual accuracy.

## 🛠️ Interface (v5.0-MCP Native)

**MANDATORY:** Use typed arguments. `params_json` is **DEPRECATED**.

### Typed Parameters

- `agent` (string): Your Agent ID (authorized: 'ORCHESTRATOR', 'PRODUCT_OWNER').
- `target_project` (string): Path to project root.
- `action` (enum): `standup_report` (default), `analyze_schedule`, `log_status`.
- `report_data` (object): (Optional) Data for log notes (e.g., `{"note": "Transitioning to M2"}`).
- `overwrite` (boolean): (Optional) Bypass Redundancy Lock for reports.
- `isolate` (boolean): Execution in Clean Session.

## 🛡️ Industrial Constraints

- **Physical Grounding:** Reports MUST be derived from disk artifacts. Guessing progress is a **Cultural Violation**.
- **SI Standards:** All timings strictly in **Seconds (s)**.
- **Audit Trail:** Every action must leave a physical trace in `DOCS/MANAGEMENT/`.

---
**ORIGIN:** [persona-project-manager by googleworkspace](https://skills.sh/googleworkspace/cli/persona-project-manager)
