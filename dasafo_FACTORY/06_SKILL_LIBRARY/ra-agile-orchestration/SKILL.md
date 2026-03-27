---
version: 3.2.0-S
agent: ORCHESTRATOR
---

# 🏃 Skill | RA Agile Orchestration

## Objective
Dynamically route and prioritize industrial tasks based on their Requirement Analysis (RA) level, ensuring optimal parallelization and resource allocation.

## 🛠️ Interface (v3.2.0-S)

### Input Schema (SkillInput.params)
- `milestone` (string): Current mission milestone (e.g., "M1", "M2").
- `parallel_factor` (integer, optional): Default 3.

### Output Schema (SkillOutput.result)
- `routing_registry`: (object) Map of agents to RA levels.
- `sprint_status`: (string) "DEPLOYED" | "PLANNING".
- `bottlenecks`: (list) Identified resource conflicts.

### ⚖️ Mandato SI (Sistema Internacional)
Las métricas de carga (throughput de tareas por segundo, latencia de orquestación) deben informarse en el SI.

## Orchestration Logic
- **RA-0 to RA-2 (Ideation):** Assign to `RESEARCH_AGENT` and `ARCHITECT`.
- **RA-3 (Execution):** Dispatch to `PRODUCTION` agents (BE, FE, DS, DB).
- **RA-4 (Quality):** Route to `COMPLIANCE` (QA, SECURITY).
- **RA-5 (Validated):** Move to `DEVOPS_SRE` for deployment and `MEMORY_OPTIMIZER` for archival.

---
*Skill v3.2.0-S | Status: Standardized.*
