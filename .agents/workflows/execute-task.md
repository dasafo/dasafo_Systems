---
description: Spawns a Clean Session to execute a specific task isolated from the main context (v3.4.0-S).
---

# Workflow /execute-task

This flow triggers the `delegate-clean-session` skill to prevent Token Decay and enforce **Context Isolation**.

1. **Agent:** `ORCHESTRATOR`
2. **Execution Protocol:** // turbo
3. **Delegate Action:** `python3 dasafo_FACTORY/skill_engine.py --agent ORCHESTRATOR --skill delegate-clean-session --target-project $TARGET_PROJECT --isolate --input '{"agent_type": "BACKEND_DEV", "spec_path": "TASKS/SPEC_LITE.json"}'`

**Spawning isolated sub-agent session...**
