---
version: v5.0-MCP (Native)
agent_authorization: [MEMORY_OPTIMIZER]
production_category: REVIEW
source: https://skills.sh/sickn33/antigravity-awesome-skills/context-optimization
protocol: Context-Hygiene / DAST
---

> [ ⬆️ Up: [[../MOC_SKILL_LIBRARY]] | 📂 Global: [[../../_dasafo_FACTORY]] ]


# 🧠 Skill | context-pruning-sieve

## Objective

Extend agent context windows by pruning verbose tool outputs, social fluff, and redundant session data. Prevents Token Decay and reduces operational costs.

## 🛠️ Interface (v5.0-MCP Native)

**MANDATORY:** Use direct typed arguments. `params_json` is **DEPRECATED**.

### Typed Parameters

- `agent` (string): Your Agent ID (MEMORY_OPTIMIZER).
- `target_project` (string): Path to project root.
- `target_file` (string): Relative path to context file (e.g., `LOGS/sessions/current.json`).
- `action` (enum): `compact_context`, `mask_observations`.
- `budget_threshold` (float): (Optional) Trigger threshold (default: 0.8).
- `isolate` (boolean): Execution in Clean Session.

## 🛡️ Industrial Constraints

- **Non-Destructive:** Never overwrite the original source; always generate an `*_optimized` version.
- **SI Standards:** All metrics strictly in **Bytes (B)** and **Seconds (s)**.
- **No-Trash Policy:** Automatic removal of social-loop phrases ("thank you", "perfect").

---

> [ ⬆️ Up: [[../MOC_SKILL_LIBRARY]] | 📂 Global: [[../../_dasafo_FACTORY]] ]

**ORIGIN:** [context-optimization by sickn33](https://skills.sh/sickn33/antigravity-awesome-skills/context-optimization)
