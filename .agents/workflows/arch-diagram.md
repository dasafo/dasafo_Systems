---
description: Requests the Architect to generate updated blueprints and the 4-layer system mapping
---

# Workflow /arch-diagram

This flow activates the Architect to visualize and solidify the technical architecture under the **v4.0-S** standard.

1. **Agent:** `ARCHITECT`

2. **Execution Protocol:** // turbo

3. **Step 1: Run ADR Synthesis:** Execute the following command to record the context of architectural decisions:
`python3 dasafo_FACTORY/skill_engine.py --agent ARCHITECT --skill architecture-decision-records --target-project $TARGET_PROJECT --input '{"action": "init"}'`

4. **Step 2: Finalize Blueprint (v4.0-S Mandate):** Consolidate the ADRs into the physical blueprint artifact:
`python3 dasafo_FACTORY/skill_engine.py --agent ARCHITECT --skill architecture-decision-records --target-project $TARGET_PROJECT --input '{"action": "finalize_blueprint"}'`

5. **Result Reporting:** Verify that `DOCS/ARCH/BLUEPRINT.md` is physically present on disk.

6. **Atomic Task Closure (v4.0-S):** Move the architectural task to COMPLETED to release the agent:
`python3 dasafo_FACTORY/skill_engine.py --agent ARCHITECT --skill registry-manager --target-project $TARGET_PROJECT --input '{"action": "update_status", "task_id": "M2-001", "new_status": "COMPLETED"}'`

7. **Result Reporting:** Verify BLUEPRINT.md is present and task M2-001 is in 03_COMPLETED.

**Drawing technical blueprints and mapping 4 layers...**
