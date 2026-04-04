---
description: The factory's master command. Analyzes the DAG and dispatches parallel agents using MCP.
---

# Workflow /factory-orchestrate

This flow activates the Orchestrator to drive project evolution using Parallel DAG execution.

1. **Agent:** `ORCHESTRATOR`
2. **Execution Protocol:** SOP via MCP

3. **Step 1: Security Gate:** Invoca la herramienta MCP **directamente por nombre** con:
   * `agent`: "ORCHESTRATOR"
   * **Tool MCP:** `agentic-thought-secret-scanner`
   * `target_project`: "PROJECTS/$TARGET_PROJECT"
   * **Params:** '{}'

4. **Step 2: DAG Topological Analysis:** Invoca la herramienta MCP:
   * `agent`: "ORCHESTRATOR"
   * **Tool MCP:** `project-management`
   * `target_project`: "PROJECTS/$TARGET_PROJECT"
   * **Params:** '{"action": "analyze_schedule"}'

5. **Step 3: Parallel Dispatch:** * Lee el array `ready_to_execute` devuelto por el análisis.
   * Por **CADA** tarea en ese array, invoca simultáneamente `delegate-clean-session` para despachar a los agentes correspondientes de forma paralela.
