---
version: v4.0-MCP
agent: FACTORY_EVOLVER / ORCHESTRATOR
source: internal/factory-doctor
---

# 🚑 Skill | Factory Doctor (v4.0-MCP)

## Objective

Realizar una auditoría forense del sistema de archivos para sanar estados corruptos. Regenera el `registry.json` y el `PROJECT_STATE.json` basándose exclusivamente en la presencia física de tareas y artefactos.

## 🛠️ Interface (v4.0-MCP)

### Input Schema (SkillInput.params)

- [cite_start]`target_project` (string, mandatory): Ruta absoluta al proyecto a sanar[cite: 1].
- `sync_neo4j` (boolean, default: true): Si se debe persistir el estado en el Grafo de Conocimiento.

### Output Schema (SkillOutput.result)

- `healing_status`: `SUCCESS` | `PARTIAL` | `FAILED`.
- `reconstructed_tasks`: (int) Número de tareas recuperadas en el registro.
- `detected_phase`: Phase M1-M5 detectada por artefactos.
- `registry_size_bytes`: Tamaño del nuevo registro en bytes (SI Mandate).

## 🛡️ Industrial Constraints

- **Disk Supremacy:** Los archivos en `TASKS/01_PENDING`, `02_IN_PROGRESS` y `03_COMPLETED` sobreescriben cualquier registro previo.
- **SI Traceability:** El tiempo de escaneo se reporta en segundos (s).
