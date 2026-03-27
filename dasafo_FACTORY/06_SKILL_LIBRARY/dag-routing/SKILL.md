---
version: 3.2.0-S
agent: ORCHESTRATOR
---

# 🕸️ Skill | DAG Routing Engine

## Objective
Decompose user prompts into a Directed Acyclic Graph (DAG) of parallel and sequential tasks for multi-agent execution.

## 🛠️ Interface (v3.2.0-S)

### Input Schema (SkillInput.params)
- `intent` (string): The user prompt or project intent.
- `project_state` (string, optional): Path to `PROJECT_STATE.json`.

### Output Schema (SkillOutput.result)
- `dag_tasks`: (list) List of task objects with dependency mapping.
- `next_node`: (string) The first agent to be triggered.
- `total_tasks`: (integer) Count of decomposed tasks.

### ⚖️ Mandato SI (Sistema Internacional)
La estimación del tiempo de ejecución total del grafo (secuencial vs paralelo) debe reportarse en segundos o minutos (unidades SI).

## 🧠 Protocol
1.  **Ingest:** Read the project intent from `PROJECT_STATE.json`.
2.  **Identify:** Separate parallel vs sequential dependencies.
3.  **Format:** Generate strict task objects for the `01_PENDING` directory.
4.  **Telemetry:** Update `$TARGET_PROJECT/PROJECT_TELEMETRY.md` with the new DAG visualization (Mermaid).
5.  **Publish:** Signal the assigned agents.

---
*Skill v3.2.0-S | Status: Standardized.*
