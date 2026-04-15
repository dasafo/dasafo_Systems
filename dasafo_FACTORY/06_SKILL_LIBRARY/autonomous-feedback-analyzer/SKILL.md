> [ ⬆️ Up: [[../MOC_SKILL_LIBRARY]] | 📂 Skill: **autonomous-feedback-analyzer** ]
---
version: v5.0-MCP (Native)
agent_authorization: [FACTORY_EVOLVER, MEMORY_OPTIMIZER, DATA_SCIENTIST]
production_category: REVIEW
source: https://skills.sh/phuryn/pm-skills/sentiment-analysis
protocol: LTP-Sync / DAST
---

# 🧠 Skill | autonomous-feedback-analyzer

> [ ⬆️ Up: [[../MOC_SKILL_LIBRARY]] | 📂 Index: [[../../_dasafo_FACTORY]] ]

## Objective

Extract actionable "Golden Rules" from feedback logs and synchronize agentic learning with the Long-Term Persistence (LTP) graph in Neo4j.

## 🛠️ Interface (v5.0-MCP Native)

**MANDATORY:** Use direct arguments. Generic `params_json` is **DEPRECATED**.

### Typed Parameters

- `agent` (string): Your authorized Agent ID.
- `target_project` (string): Path to project root.
- `action` (enum): `analyze_file` (default) | `analyze_text`.
- `file_path` (string): Relative path to feedback source (default: `LOGS/FEEDBACK-LOG.md`).
- `raw_text` (string): Direct text to analyze if using `analyze_text`.
- `isolate` (boolean): Execution in Clean Session.

## 🛡️ Industrial Constraints

- **SI Standards:** Report processed data in **Bytes (B)** and execution in **Seconds (s)**.
- **DAST Sovereignty:** Analysis MUST be persisted in `LOGS/` as a JSON artifact.
- **LTP Integrity:** Direct sync with `dasafo-shared-kg` (Neo4j) is mandatory for rule extraction.

---
**ORIGIN:** [sentiment-analysis by phuryn](https://skills.sh/phuryn/pm-skills/sentiment-analysis)
