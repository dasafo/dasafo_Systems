---
description: Verifies physical scaffolding existence on disk via MCP before delegating tasks.
---

# Workflow /validate-backbone

This flow activates the Orchestrator to act as the "Project Inspector", ensuring the structural backbone is solid.

1. **Agent:** `ORCHESTRATOR`
2. **Execution Protocol:** SOP via MCP

3. **Run Validation:** Invoca la herramienta MCP **directamente por nombre** con:
   * `agent`: "ORCHESTRATOR"
   * **Tool MCP:** `project-backbone-validator`
   * `target_project`: "PROJECTS/$TARGET_PROJECT"
   * **Params:** '{"framework": "<FRAMEWORK>"}' *(Sustituir por fastapi, nextjs, etc.)*

4. **Decision Gate:** - If `scaffolding_ready` is True: Proceed to delegating implementation tasks.
   * If `scaffolding_ready` is False: Suspend delegation and alert the ARCHITECT.
