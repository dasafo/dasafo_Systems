---
description: Executes the atomic deployment of the current build to the provisioned infrastructure via MCP.
---

# Workflow /deploy

This flow pushes the verified code artifacts to the operational environment.

1. **Agent:** `DEVOPS_SRE`
2. **Security Gate:** Requires a `PASSED` status in the latest `SECURITY_REPORT.md`.
3. **Run Deployment:** Invoca la herramienta MCP **directamente por nombre** con:
   * `agent`: "DEVOPS_SRE"
   * **Tool MCP:** `deployment-health-check`
   * `target_project`: "PROJECTS/$TARGET_PROJECT"
   * **Params:** '{"action": "deploy"}'

**Executing atomic deployment v5.0-MCP...**
