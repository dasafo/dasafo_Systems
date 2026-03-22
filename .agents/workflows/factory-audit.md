---
description: Triggers the Security Auditor to aggressively scan all completed tasks for vulnerabilities.
---

# Factory Security Audit Workflow

1. Identify the current active `$TARGET_PROJECT` within `PROJECTS/`.
2. Assume the role of the `@security_auditor`.
3. List all JSON files currently residing in `TASKS/03_COMPLETED`.
4. For each task, check the modified source code in the `WORKSPACE/` for security compliance (Hardcoded secrets, unchecked user input, path traversal risks).
5. If an anomaly is found:
   - Move the Task JSON to `TASKS/05_REJECTED`.
   - Open `/home/david/Documents/AI/AGENTES/dasafo_Systems/dasafo_FACTORY/FEEDBACK-LOG.md` and append a new row to the knowledge base regarding the breach.
6. Provide an audit summary table in the chat showing PASS/FAIL for each scanned task.
