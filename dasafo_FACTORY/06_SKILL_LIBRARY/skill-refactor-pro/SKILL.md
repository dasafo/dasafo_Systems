---
version: v5.0-MCP (Native)
agent_authorization: [FACTORY_EVOLVER]
source: https://skills.sh/github/awesome-copilot/refactor
protocol: Surgical-Evolution / DAST
---

# 🧬 Skill | skill-refactor-pro

## Objective

Provide surgical code refactoring to improve maintainability and apply "Golden Rules" from Neo4j without changing external behavior. Treats refactoring as gradual evolution.

## 🛠️ Interface (v5.0-MCP Native)

**MANDATORY:** Use direct typed arguments. `params_json` is **DEPRECATED**.

### Typed Parameters

- `agent` (string): Your Agent ID (must be 'FACTORY_EVOLVER').
- `target_project` (string): Absolute path to the project root.
- `file_path` (string): Specific file within `WORKSPACE/` to evolve (e.g., `backend/main.py`).
- `action` (enum): `apply_refactor` (default), `analyze_smells`.
- `rules` (list): (Optional) List of Golden Rules to apply (e.g., `["SI_UNITS", "PORT_CONFLICT:5432"]`).
- `target_smell` (string): (Optional) Specific smell to target.
- `isolate` (boolean): Execution in Clean Session.

## 🛡️ Industrial Constraints

- **Physical Sandboxing:** Refactored code MUST be output to a new file with `_refactored` suffix. Never overwrite original files directly.
- **SI Mandate:** Execution time in **seconds (s)** and metrics in **bytes (B)**.
- **Test-Driven Policy:** Refactoring is FORBIDDEN on files that lack corresponding physical tests.

---
**ORIGIN:** [refactor by awesome-copilot](https://skills.sh/github/awesome-copilot/refactor)
