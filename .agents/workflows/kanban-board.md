---
description: Starts the Vibe Kanban visual dashboard for the current project via MCP.
---

# Workflow /kanban-board

This flow starts the local server to visualize `registry.json` and the physical task artifacts.

1. **Agent:** `ORCHESTRATOR`
2. **Execution Protocol:** SOP via MCP

3. **Start Dashboard:** Invoca la herramienta MCP **directamente por nombre** con:
   * `agent`: "ORCHESTRATOR"
   * **Tool MCP:** `kanban-solidity-gate`
   * `target_project`: "PROJECTS/$TARGET_PROJECT"
   * **Params:** '{"action": "start_dashboard", "port": 3001}'
