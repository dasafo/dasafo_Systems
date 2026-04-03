---
description: Activates the Deployment_Monitor to verify real-time health and SI metrics via MCP (v5.0-MCP).
---

# Workflow /health-check

This flow validates that the deployment is reachable and performing under industrial standards.

1. **Agent:** `DEPLOYMENT_MONITOR`
2. **Execution Protocol:** SOP via MCP

3. **Run Health Check:** Invoca la herramienta MCP **directamente por nombre** con:
   * `agent`: "DEPLOYMENT_MONITOR"
   * **Tool MCP:** `deployment-health-check`
   * `target_project`: "PROJECTS/$TARGET_PROJECT"
   * **Params:** '{}'

4. **SI Verification:** Ensure latency is reported in **seconds (s)** and response size in **bytes (B)**.
