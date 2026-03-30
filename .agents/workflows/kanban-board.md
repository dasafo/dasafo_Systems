---
description: Starts the Vibe Kanban visual dashboard for the current project (v3.4.0-S).
---

# Workflow /kanban-board

This flow starts the local server to visualize `registry.json` and the physical task artifacts.

1. **Agent:** `ORCHESTRATOR`
2. **Execution Protocol:** // turbo
3. **Start Dashboard:** `python3 dasafo_FACTORY/skill_engine.py --agent ORCHESTRATOR --skill kanban-solidity-gate --target-project $TARGET_PROJECT --input '{"action": "start_dashboard", "port": 3001}'`

**Initializing Industrial Dashboard on Port 3001...**
