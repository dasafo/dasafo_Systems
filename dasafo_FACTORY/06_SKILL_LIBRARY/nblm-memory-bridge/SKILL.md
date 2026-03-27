---
version: 3.2.0-S
agent: MEMORY_OPTIMIZER
---

# 🌉 Skill | NotebookLM Memory Bridge

## Objective
Sync the factory's semantic architecture and project history with NotebookLM to provide an interactive, multimedia memory for industrial continuity.

## 🛠️ Interface (v3.2.0-S)

### Input Schema (SkillInput.params)
- `sync_scope` (string, optional): "sprint" | "project" | "full". Default "sprint".
- `project_path` (string, optional): Absolute path to the source project.

### Output Schema (SkillOutput.result)
- `bridge_status`: (string) "SYNCHRONIZED".
- `notebook_id`: (string) The NotebookLM UUID.
- `last_sync`: (string) ISO timestamp.

### ⚖️ Mandato SI (Sistema Internacional)
El volumen de datos sincronizado (en bytes o bits) y el tiempo de latencia de sincronización deben reportarse en el SI.

## Workflow
1.  **Export:** Produce a consolidated `SEMANTIC_INDEX.pdf` or equivalent text artifact.
2.  **Upload:** Feed the export into the "Project Brain" via NotebookLM MCP.
3.  **Governance:** Automatically tag sources with Sprint and Date for chronological retrieval.

---
*Skill v3.2.0-S | Status: Standardized.*
