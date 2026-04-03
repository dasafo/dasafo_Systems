---
description: The factory's master command. Analyzes project state and advances phases using MCP.
---

# Workflow /factory-orchestrate

This flow activates the Orchestrator to drive project evolution under the **Aduana Universal** protocol.

1. **Agent:** `ORCHESTRATOR`
2. **Execution Protocol:** SOP via MCP

3. **Run Scan (Security Gate):** Invoca la herramienta MCP `execute_industrial_skill` con:
   * `agent`: "ORCHESTRATOR"
   * `skill`: "agentic-thought-secret-scanner"
   * `target_project`: "PROJECTS/$TARGET_PROJECT"
   * `params_json`: '{}'

4. **Execution (Phase Analysis):**
   * El motor MCP sincronizará automáticamente la carpeta `TASKS/` con `registry.json`.
   * Analiza el estado devuelto y deconstruye las siguientes tareas SOLO si la Aduana lo permite (ej. si el HITL Approval está firmado).
