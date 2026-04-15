---
name: skill-validation-outcome
description: Evaluates a Skill's performance against Golden Datasets to ensure zero-regression and output integrity.
version: v5.2-MCP
---
<!-- LEVEL_1_END -->



# Skill Validation Outcome
This macro-skill automates the CI/CD validation of the factory's skill library.

## Parameters
- `target_project`: Path to the project.
- `target_skill`: The name of the skill to validate.
- `input_payload`: The payload to test.
- `actual_output`: The result returned by the skill.
- `min_similarity`: Minimum cosine similarity or threshold (default 0.95).

## Internal Mechanics
1. Loads the Golden Dataset from `04_COMPLIANCE_AND_QUALITY/VALIDATION/GOLDEN_DATASETS/EXPECTATION_[skill].json`.
2. Performs a structural and semantic comparison.
3. Generates a validation report.
