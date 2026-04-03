---
description: Performs an industrial-grade security scan following Zero-Trust v4.0-S standards via MCP.
---

# Workflow /scan

This flow activates the **Security Auditor** to perform a deep-dive audit on the current project.

1. **Agent:** `SECURITY_AUDITOR`
2. **Execution Protocol:** SOP via MCP

3. **Run Scan:** Invoca la herramienta MCP `execute_industrial_skill` con:
   * `agent`: "SECURITY_AUDITOR"
   * `skill`: "agentic-thought-secret-scanner"
   * `target_project`: "PROJECTS/$TARGET_PROJECT"
   * `params_json`: '{}'

4. **Reporting:** Generate a structured `SECURITY_REPORT.md` within the project's `LOGS/` directory.
