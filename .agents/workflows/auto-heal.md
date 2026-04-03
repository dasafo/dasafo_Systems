---
description: Activates the M5 Self-Healing loop via MCP. DEVOPS_SRE triggers an emergency spec for FACTORY_EVOLVER.
---

# Workflow /auto-heal

This flow represents the industrial immune system. When a deployment fails, this workflow triggers the automatic creation of an emergency patch.

1. **Agent:** `DEVOPS_SRE`
2. **Execution Protocol:** SOP via MCP

3. **Emergency Diagnosis:** Identify the specific blocker (e.g., `PORT_CONFLICT:5432`).
4. **Apply Patch (Trigger Evolver):** Invoca la herramienta MCP `execute_industrial_skill` con:
   * `agent`: "FACTORY_EVOLVER"
   * `skill`: "skill-refactor-pro"
   * `target_project`: "PROJECTS/$TARGET_PROJECT"
   * `params_json`: '{"file_path": "WORKSPACE/infra/docker-compose.yml", "rules": ["PORT_CONFLICT:5432"]}'

**Initiating autonomous self-healing protocol...**
