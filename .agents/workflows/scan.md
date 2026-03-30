---
description: description: Performs an industrial-grade security scan following Zero-Trust v3.4.0-S standards.
---

# Workflow /scan

This flow activates the **Security Auditor** to perform a deep-dive audit on the current project.

1. **Target Identification**: Identify the project root using the `$TARGET_PROJECT` environment variable.
2. **Execution Protocol**:
// turbo
3. **Run Scan**: Execute the following command:
   `python3 dasafo_Systems/dasafo_FACTORY/skill_engine.py --agent SECURITY_AUDITOR --skill agentic-thought-secret-scanner --target-project $TARGET_PROJECT`

4. **Reporting**: Generate a structured `SECURITY_REPORT.md` within the project's `LOGS/` directory.

**Enforcing Zero-Trust v3.4.0-S Enforcement...**
