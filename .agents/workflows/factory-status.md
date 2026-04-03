---
description: Generates a visual report of project progress and v5.0-MCP health via MCP.
---

# Workflow /factory-status

This flow generates a consolidated health and status report for the current project context.

1. **Agent:** `DEPLOYMENT_MONITOR`
2. **Execution Protocol:** SOP via MCP

3. **Run Pulse Check:** Invoca la herramienta MCP **directamente por nombre** con:
   * `agent`: "DEPLOYMENT_MONITOR"
   * **Tool MCP:** `project-management`
   * `target_project`: "PROJECTS/$TARGET_PROJECT"
   * **Params:** '{}'

4. **Status Mapping:** Utiliza los datos devueltos por el MCP para generar un reporte visual textual en el chat.
