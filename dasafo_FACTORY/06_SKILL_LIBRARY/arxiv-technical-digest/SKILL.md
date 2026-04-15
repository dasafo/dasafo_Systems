> [ ⬆️ Up: [[../MOC_SKILL_LIBRARY]] | 📂 Skill: **arxiv-technical-digest** ]
---
version: v5.0-MCP (Native)
agent_authorization: [RESEARCH_AGENT, DOCS_MASTER]
source: https://skills.sh/jezweb/claude-skills/arxiv-digest
protocol: Fact-First / DAST
---

> [ ⬆️ Up: [[../MOC_SKILL_LIBRARY]] | 📂 Global: [[../../_dasafo_FACTORY]] ]


# 📚 Skill | arxiv-technical-digest

## Objective

Ingest and summarize technical papers from ArXiv to validate architectural decisions or research emerging technologies.

## 🛠️ Interface (v5.0-MCP Native)

**MANDATORY:** Use direct arguments. The `params_json` structure is **DEPRECATED**.

### Typed Parameters

- `agent` (string): Your authorized Agent ID (RESEARCH_AGENT or DOCS_MASTER).
- `target_project` (string): Absolute path to the project root.
- `query` (string): Technical keywords to search (e.g., 'FastAPI async patterns').
- `max_results` (integer): (Optional) Limit of papers to digest (default: 5).
- `overwrite` (boolean): (Optional) Bypass the Redundancy Lock.
- `isolate` (boolean): (Optional) Execute in a Clean Session.

## 🛡️ Industrial Constraints

- **Factual Sovereignty:** Do not hallucinate research; data must originate from a physical disk artifact in `LOCAL_KNOWLEDGE/research/`.
- **SI Standards:** All temporal reporting MUST use **seconds (s)**.
- **Auth Gate:** Only Hub 02 and Hub 04 agents are permitted to invoke this sense.

---

> [ ⬆️ Up: [[../MOC_SKILL_LIBRARY]] | 📂 Global: [[../../_dasafo_FACTORY]] ]

**ORIGIN:** [arxiv-digest by jezweb](https://skills.sh/jezweb/claude-skills/arxiv-digest)
