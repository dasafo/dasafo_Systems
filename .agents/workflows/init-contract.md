---
description: Activates the Product Owner to generate the 12-section PRP_MASTER contract (v3.4.0-S).
---

# Workflow /init-contract

This flow forces the **PRODUCT_OWNER** to define the absolute truth of the project before any code is written.

1. **Agent:** `PRODUCT_OWNER`
2. **Execution Protocol:** // turbo
3. **Run PRP Generator:** `python3 dasafo_Systems/dasafo_FACTORY/skill_engine.py --agent PRODUCT_OWNER --skill prp-generator --target-project $TARGET_PROJECT --input '{"action": "generate_master", "project_name": "Current Project", "problem_description": "Define based on conversation."}'`

**Solidifying Industrial Contract...**
