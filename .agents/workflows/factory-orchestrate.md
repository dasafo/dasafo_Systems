---
description: The factory's master command. Analyzes project state and advances to the next phase following the Universal Pipeline (v3.4.0-S).
---

# Workflow /factory-orchestrate

This flow activates the Orchestrator to drive project evolution under the **Aduana Universal** protocol.

1. **Agent:** `ORCHESTRATOR`
2. **Security Gate (MANDATORY)**: Run `kanban-solidity-gate` via MCP to verify physical tasks. **Hard Stop** if not SOLIDIFIED.
3. **Run Scan**: Execute the following command:
   `python3 dasafo_FACTORY/skill_engine.py --agent ORCHESTRATOR --skill agentic-thought-secret-scanner --target-project $TARGET_PROJECT`
4. **Execution (v3.4.0-S)**:
   - Synchronize `registry.json` with the physical `TASKS/` folder.
   - Analyze project state and delegate next tasks ONLY if Phase transitions are validated by the Aduana protocol.

**Synchronizing industrial pipeline v3.4.0-S...**
