---
description: Requests the Architect to generate updated blueprints and the 4-layer system mapping via MCP.
---

# Workflow /arch-diagram

This flow activates the Architect to visualize and solidify the technical architecture under the **v5.0-MCP** standard.

1. **Agent:** `ARCHITECT`
2. **Execution Protocol:** SOP via MCP

3. **Step 1: Run ADR Synthesis:** Invoca la herramienta MCP **directamente por nombre** con:
   * `agent`: "ARCHITECT"
   * **Tool MCP:** `architecture-decision-records`
   * `target_project`: "PROJECTS/$TARGET_PROJECT"
   * **Params:** '{"action": "init"}'

4. **Step 2: Finalize Blueprint (v5.0-MCP Mandate):** Consolida los ADRs en el disco invocando las herramientas MCP **directamente por nombre** (ej. `prp-generator`, `delegate-clean-session`) con:
   * `agent`: "ARCHITECT"
   * **Tool MCP:** `architecture-decision-records`
   * `target_project`: "PROJECTS/$TARGET_PROJECT"
   * **Params:** '{"action": "finalize_blueprint"}'

5. **Result Reporting:** Verify that `DOCS/ARCH/BLUEPRINT.md` is physically present on disk. The system will auto-commit the task upon success.
