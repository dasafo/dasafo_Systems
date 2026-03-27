---
version: 3.2.0-S
agent: ORCHESTRATOR
---

# 📚 Skill | NotebookLM Factory Biographer

## Objective
Generate bird-eye view reports of factory health, mission progress, and industrial blockers using NotebookLM to ensure transparency and strategic alignment.

## 🛠️ Interface (v3.2.0-S)

### Input Schema (SkillInput.params)
- `format` (string, optional): "briefing" | "study_guide" | "blog_post". Default "briefing".
- `focus` (string, optional): "blockers" | "achievements" | "all". Default "all".

### Output Schema (SkillOutput.result)
- `biography_url`: (string) Deep-link to the NotebookLM artifact.
- `status`: (string) "COMPLETED" | "GENERATING".
- `vibe`: (string) "CLARITY".

### ⚖️ Mandato SI (Sistema Internacional)
Cualquier métrica de tiempo de ejecución de misiones o volumen de datos procesado en el reporte debe estar en unidades del SI.

## Reporting Protocol
1.  **Sweep:** Collect progress states from all agent departments (`LOGS/`).
2.  **Synthesis:** Use NotebookLM to create "Factory Updates" based on project artifacts.
3.  **Visualization:** Generate infographics for high-level roadmap visualization.

---
*Skill v3.2.0-S | Status: Standardized.*
