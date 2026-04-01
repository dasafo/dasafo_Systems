---
description: Triggers context-isolated delegation with predictive Neo4j guardrails (v4.0-S).
---

# Workflow /execute-task

This flow triggers the `delegate-clean-session` skill to prevent Token Decay, enforcing **Context Isolation** and predictive **Neo4j Guardrails**.

1. **Agent:** `ORCHESTRATOR`

2. **Execution Protocol:** // turbo

3. **Pre-Flight Intelligence Check (v4.0-S):** Before delegating to Phase M3, you MUST analyze the target technology (e.g., shadcn, fastapi). If historical data is needed, query Neo4j for `CulturalViolation` nodes related to this technology and inject the retrieved "Golden Rules" into the `03_constraints` of the `SPEC_LITE.json`.

4. **Delegate Action:** Execute the following command (adjusting `agent_type` as needed):
   `python3 dasafo_FACTORY/skill_engine.py --agent ORCHESTRATOR --skill delegate-clean-session --target-project $TARGET_PROJECT --isolate --input '{"agent_type": "BACKEND_DEV", "spec_path": "TASKS/SPEC_LITE.json"}'`

**Spawning isolated sub-agent session...**
