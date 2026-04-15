---
name: delegate-clean-session
description: Spawn a specialized sub-agent (Peon) in a "Clean Slate" environment. Prevents context pollution.
version: v5.1-MCP
---
# 🚀 Skill | delegate-clean-session (Nivel 1)
Orchestrates context-isolated delegation to specialized sub-agents.
<!-- LEVEL_1_END -->

## 🛠️ Interface (Nivel 2)
### Parameters
- `agent` (string): Your assigned role.
- `target_project` (string): Path to project root.
- `spec_path` (string): Path to task spec.
- `agent_type` (string): Target persona (e.g., 'BACKEND_DEV').
- `isolate` (boolean): Default `true`.
<!-- LEVEL_2_END -->

## Internal Mechanics (Nivel 3)
- **Auto-Start Mandate:** Physically moves task to `02_IN_PROGRESS`.
- **Immunization:** Queries Neo4j for JIT "Golden Rules".
- **DAST Sovereignty:** Requires physical `SPEC_LITE.json`.
