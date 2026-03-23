---
description: Triggers the Security Auditor to aggressively scan all completed tasks for vulnerabilities.
---

1. Read the latest `LOGS/` of the completed sprint.
2. Run `snyk test` and `gitleaks detect` on the workspace.
3. Perform a "Least Privilege" audit on all agents in `AGENT_REGISTRY.md`.
4. Produce a `SECURITY_AUDIT_REPORT.md` with:
    - Detected vulnerabilities.
    - Risk status of each agent.
    - Recommended remediation steps.
5. Block any "PROD" deployment until a "SEC_APPROVED" status is reached.
