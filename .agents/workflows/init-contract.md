---
description: Activates the Product Owner to generate the 12-section PRP_MASTER contract with Financial KPIs (v4.0-S).
---

# Workflow /init-contract

This flow forces the **PRODUCT_OWNER** to define the absolute truth and financial viability of the project before any code is written.

1. **Agent:** `PRODUCT_OWNER`
2. **Execution Protocol:** // turbo
3. **Financial Baseline:** Run `startup-metrics-framework` to establish Target CAC, LTV, and SI constraints.
4. **Run PRP Generator:** Execute the following to formalize the contract:
   `python3 dasafo_FACTORY/skill_engine.py --agent PRODUCT_OWNER --skill prp-generator --target-project $TARGET_PROJECT --input '{"action": "generate_master"}'`

**Solidifying Industrial Contract & ROI...**
