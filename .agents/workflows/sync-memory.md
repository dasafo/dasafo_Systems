---
description: Activates the MEMORY_OPTIMIZER to extract Golden Rules from logs and sync them to Neo4j via MCP.
---

# Workflow /sync-memory

This flow acts as the factory's "sleep cycle", converting short-term logs into Long-Term Persistence (LTP).

1. **Agent:** `MEMORY_OPTIMIZER`
2. **Execution Protocol:** SOP via MCP

3. **Extract & Sync:** Invoca la herramienta MCP **directamente por nombre** con:
   * `agent`: "MEMORY_OPTIMIZER"
   * **Tool MCP:** `autonomous-feedback-analyzer`
   * `target_project`: "PROJECTS/$TARGET_PROJECT"
   * **Params:** '{}'
