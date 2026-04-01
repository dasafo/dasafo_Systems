---
description: Verifica que el andamiaje estructural del framework (Scaffolding) exista físicamente en disco antes de delegar tareas a los peones (v4.0-S).
---

# Workflow /validate-backbone

This flow activates the Orchestrator to act as the "Inspector de Obra", ensuring the structural backbone of the project is solid before any atomic implementation agent is dispatched.

1. **Agent:** `ORCHESTRATOR`

2. **Execution Protocol:** // turbo

3. **Pre-flight Check:** Verify physical SSoT (Single Source of Truth) for the base framework.

4. **Run Validation:** Execute the following command (replace `<FRAMEWORK>` with `nextjs` or `fastapi` as needed):
   `python3 dasafo_FACTORY/skill_engine.py --agent ORCHESTRATOR --skill project-backbone-validator --target-project $TARGET_PROJECT --input '{"framework": "<FRAMEWORK>"}'`

5. **Decision Gate:** - If `scaffolding_ready` is True: Proceed to `/execute-task`.
   - If `scaffolding_ready` is False: Suspend delegation and trigger the framework bootstrapper or alert the ARCHITECT to resolve the `missing_bones`.

**Inspecting industrial backbone...**
