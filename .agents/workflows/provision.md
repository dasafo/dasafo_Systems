---
description: Activates the DevOps_SRE to provision the physical infrastructure (v3.4.0-S).
---

# Workflow /provision

This flow triggers the infrastructure-as-code layer to prepare the production environment.

1. **Agent:** `DEVOPS_SRE`
2. **Execution Protocol:** // turbo
3. **Run Provisioner:** `python3 dasafo_FACTORY/skill_engine.py --agent DEVOPS_SRE --skill docker-stack-provisioner --target-project $TARGET_PROJECT`

4. **Persistence:** Verify that `docker-compose.yml` or Terraform states are synced in `WORKSPACE/infra/`.

**Provisioning industrial environment...**
