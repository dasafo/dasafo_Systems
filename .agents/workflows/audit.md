---
description: description: Requests the QA_Tester to perform a comprehensive review of the current task before completion (v3.4.0-S).
---

# Workflow /audit

This flow activates the quality feedback loop to validate the current task against **Solidity Guard v3.4.0-S** industrial standards.

1. **Agent:** `QA_TESTER`
2. **Execution Protocol (AutoShield v3.4)**:
   - Pre-flight check: Verify task parity with the `PRP_CONTRACT.json`.
   - Post-flight check: Inject failures into `FEEDBACK-LOG.md`.
// turbo
3. **Run Visual Audit**: Execute the following command for an automated UI/UX check:
   `python3 dasafo_Systems/dasafo_FACTORY/skill_engine.py --agent QA_TESTER --skill factory-audit-pro --target-project $TARGET_PROJECT`

4. **Result Reporting**: Verify results against the `PRP_CONTRACT.json` success criteria.

**Initiating industrial quality audit...**
