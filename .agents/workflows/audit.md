---
description: Requests the QA_Tester to perform a comprehensive review of the current task using the MCP factory protocol (v5.0-MCP).
---

# Workflow /audit

This flow activates the quality feedback loop to validate the current task against **Solidity Guard v5.0-MCP** industrial standards.

1. **Agent:** `QA_TESTER`
2. **Execution Protocol (AutoShield v3.4):** SOP via MCP
   - Pre-flight check: Verify task parity with the `PRP_CONTRACT.json`.
   - Post-flight check: Inject failures into `FEEDBACK-LOG.md`.

3. **Run Visual Audit:** Invoca la herramienta MCP **directamente por nombre** con:
   - `agent`: "QA_TESTER"
   - **Tool MCP:** `factory-audit-pro`
   - `target_project`: "PROJECTS/$TARGET_PROJECT"
   - **Params:** '{}'

4. **Result Reporting:** Verify results against the `PRP_CONTRACT.json` success criteria (SI Units: seconds/bytes).
