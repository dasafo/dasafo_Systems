---
description: Executes the atomic deployment of the current build to the provisioned infrastructure (v3.4.0-S).
---

# Workflow /deploy

This flow pushes the verified code artifacts to the operational environment.

1. **Agent:** `DEVOPS_SRE`
2. **Security Gate**: Requires a `PASSED` status in the latest `SECURITY_REPORT.md`.
3. **Run Deployment:** `python3 dasafo_FACTORY/skill_engine.py --agent DEVOPS_SRE --skill deployment-health-check --target-project $TARGET_PROJECT --input '{"action": "deploy"}'`

**Executing atomic deployment v3.4.0-S...**
