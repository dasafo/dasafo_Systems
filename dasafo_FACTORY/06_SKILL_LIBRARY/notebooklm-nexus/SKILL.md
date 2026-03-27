---
version: 3.2.0-S
agent: DATA_SCIENTIST
---

# 🧠 Skill | NotebookLM Knowledge Nexus

## Objective
Leverage NotebookLM as a decentralized industrial mind for synthesizing research papers, massive datasets, and complex experiment histories into actionable technical insights.

## 🛠️ Interface (v3.2.0-S)

### Input Schema (SkillInput.params)
- `action` (string, optional): "synthesize" | "summarize". Default "synthesize".
- `source_indices` (list, optional): List of sources to query in the Nexus.

### Output Schema (SkillOutput.result)
- `nexus_insights`: (string) Detailed technical summary.
- `audio_summary_url`: (string, optional): Link to generated briefing.
- `vibe_check`: (string) "SCIENTIFIC_RIGOR".

### ⚖️ Mandato SI (Sistema Internacional)
Cualquier métrica técnica consolidada (tiempos de inferencia, volúmenes de datos, precisiones) debe citarse estrictamente bajo el SI.

## Workflow
1.  **Collection:** Import PDFs/Markdown from `RESEARCH_AGENT` and `DB_MASTER`.
2.  **Synthesis:** Identify correlations between theoretical ArXiv findings and local project constraints.
3.  **Governance:** Export findings to `$TARGET_PROJECT/LOCAL_KNOWLEDGE/synthesis/`.

---
*Skill v3.2.0-S | Status: Standardized.*
