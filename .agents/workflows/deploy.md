---
description: Executes the atomic deployment of the current build to the provisioned infrastructure via MCP.
---

# Workflow /deploy

This flow pushes the verified code artifacts to the operational environment.

1. **Agent:** `DEVOPS_SRE`
2. **Security Gate:** Requires a `PASSED` status in the latest `SECURITY_REPORT.md`.
3. **Run Deployment:** Invoca la herramienta MCP `execute_industrial_skill` con:
   * `agent`: "DEVOPS_SRE"
   * `skill`: "deployment-health-check"
   * `target_project`: "PROJECTS/$TARGET_PROJECT"
   * `params_json`: '{"action": "deploy"}'

**Executing atomic deployment v4.0-S...**
