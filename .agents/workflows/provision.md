---
description: Activates the DevOps_SRE to provision the physical infrastructure via MCP.
---

# Workflow /provision

This flow triggers the infrastructure-as-code layer to prepare the production environment.

1. **Agent:** `DEVOPS_SRE`
2. **Execution Protocol:** SOP via MCP

3. **Run Provisioner:** Invoca la herramienta MCP `execute_industrial_skill` con:
   * `agent`: "DEVOPS_SRE"
   * `skill`: "docker-stack-provisioner"
   * `target_project`: "PROJECTS/$TARGET_PROJECT"
   * `params_json`: '{}'

4. **Persistence:** Verify that `docker-compose.yml` or Terraform states are synced in `WORKSPACE/infra/`.
