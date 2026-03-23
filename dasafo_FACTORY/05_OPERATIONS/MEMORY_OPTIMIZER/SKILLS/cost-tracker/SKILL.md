---
description: Lightweight token usage estimation and budget enforcement.
---

# 💰 SKILL: cost-tracker

1. **Token Ingestion:** Extract "input_tokens" and "output_tokens" from every agent interaction.
2. **Price Calculation:** Apply current model pricing (e.g., $xxx / 1M tokens) to the usage.
3. **Project Accumulator:** Update the `PROJECT_COSTS.json` or equivalent in the project root.
4. **Budget Guard:** Compare current accumulated cost against the `max_budget` defined in `GLOBAL_USER.md`.
5. **Threshold Alert:** If cost > 80% or 100% of budget:
   - Flag the project as "BUDGET_EXCEEDED".
   - Block further execution until a `Human Approval Gate` is cleared.
