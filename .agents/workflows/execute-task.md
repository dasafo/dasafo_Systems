---
description: Triggers context-isolated delegation with predictive Neo4j guardrails via MCP (v5.0-MCP).
---

# Workflow /execute-task

This flow triggers the `delegate-clean-session` skill to prevent Token Decay, enforcing **Context Isolation** and predictive **Neo4j Guardrails**.

1. **Agent:** `ORCHESTRATOR`
2. **Execution Protocol:** SOP via MCP

3. **Pre-Flight Intelligence Check:** Before delegating to Phase M3, analyze the target technology. If needed, query Neo4j for `CulturalViolation` nodes and ensure rules are injected.

4. **Delegate Action:** Invoca la herramienta MCP **directamente por nombre** con:
   * `agent`: "ORCHESTRATOR"
   * **Tool MCP:** `delegate-clean-session`
   * `target_project`: "PROJECTS/$TARGET_PROJECT"
   * **Params:** '{"agent_type": "BACKEND_DEV", "spec_path": "TASKS/01_PENDING/M3-001.json"}' *(Ajusta el agent_type y spec_path según corresponda).*

**Spawning isolated sub-agent session via Factory MCP...**
