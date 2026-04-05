---
description: The factory's master command. Analyzes the DAG, synchronizes Engram, and dispatches parallel or emergency agents using MCP.
---

# Workflow /factory-orchestrate

This flow activates the Orchestrator to drive project evolution using Parallel DAG execution and Immune System Preemption.

1. **Agent:** `ORCHESTRATOR`
2. **Execution Protocol:** SOP via MCP

3. **Step 1: Engram Sync (Memoria Rápida):** Invoca la herramienta MCP:
   * `agent`: "ORCHESTRATOR"
   * **Tool MCP:** `project-management`
   * `target_project`: "PROJECTS/$TARGET_PROJECT"
   * **Params:** '{"action": "warm_up_engram"}'

4. **Step 2: Security Gate:** Invoca la herramienta MCP **directamente por nombre** con:
   * `agent`: "ORCHESTRATOR"
   * **Tool MCP:** `agentic-thought-secret-scanner`
   * `target_project`: "PROJECTS/$TARGET_PROJECT"
   * **Params:** '{}'

5. **Step 3: DAG Topological Analysis:** Invoca la herramienta MCP:
   * `agent`: "ORCHESTRATOR"
   * **Tool MCP:** `project-management`
   * `target_project`: "PROJECTS/$TARGET_PROJECT"
   * **Params:** '{"action": "analyze_schedule"}'

6. **Step 4: Parallel Dispatch & Auto-Heal:** * Lee el array `ready_to_execute` devuelto por el análisis.
   * **PRIORITY RULE:** Si detectas un ID de tarea que empiece por `EMERGENCY-`, ignora el resto del array de tareas de producción y despacha ÚNICAMENTE la emergencia para curar la factoría.
   * Por **CADA** tarea en el array (o la de emergencia), invoca simultáneamente `delegate-clean-session` para despachar a los agentes de forma paralela.
