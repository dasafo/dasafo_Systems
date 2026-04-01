---
description: Activates the M5 Self-Healing loop. DEVOPS_SRE triggers an emergency spec for FACTORY_EVOLVER to patch infrastructure constraints (v4.0-S).
---

# Workflow /auto-heal

This flow represents the industrial immune system. When a deployment fails due to resource or network constraints, this workflow triggers the automatic creation of an emergency patch.

1. **Agent:** `DEVOPS_SRE`
2. **Execution Protocol:** // turbo
3. **Emergency Diagnosis:** Run `deployment-health-check` to identify the specific blocker (e.g., `PORT_CONFLICT:5432`).
4. **Trigger Evolver:** Once the emergency `SPEC_LITE.json` is physically generated in `TASKS/01_PENDING/`, the `FACTORY_EVOLVER` will autonomously wake up via Double-Gating.
5. **Apply Patch:** Execute the following to patch the infrastructure:
   `python3 dasafo_FACTORY/skill_engine.py --agent FACTORY_EVOLVER --skill skill-refactor-pro --target-project $TARGET_PROJECT --input '{"file_path": "WORKSPACE/infra/docker-compose.yml", "rules": ["PORT_CONFLICT:5432"]}'`

**Initiating self-healing protocol...**
