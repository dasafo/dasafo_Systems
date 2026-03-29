---
version: 3.3.0-S
agent: Multiple (ORCHESTRATOR / PRODUCT_OWNER)
source: https://skills.sh/akillness/oh-my-skills/cost-tracker
---

# 💰 Skill | Cost Tracker

## Objective

Advanced token usage estimation, budget enforcement, and financial ledger management for industrial projects.

## 🛠️ Interface (v3.3.0-S)

### Input Schema (SkillInput.params)

- `input_tokens` (integer): Tokens sent to the LLM.
- `output_tokens` (integer): Tokens received from the LLM.
- `model_id` (string): ID of the model used (e.g., "claude-3-5-sonnet").

### Output Schema (SkillOutput.result)

- `current_cost`: (float) Estimated cost for this transaction.
- `total_accumulated`: (float) Total project cost so far.
- `budget_limit`: (float) Current budget limit defined in ledger.
- `status`: (string) "OK" | "WARNING" | "BUDGET_EXCEEDED".
- `ledger`: (string) Path to the physical `PROJECT_COSTS.json`.

### ⚖️ Mandato SI (Sistema Internacional)

Cualquier métrica financiera debe vincularse al consumo energético y computacional expresado en unidades del SI (Joules, Watts) si se dispone de telemetría de hardware. El tiempo se registra en formato ISO-8601 (segundos).

## 🛡️ Industrial Constraints (Zero-Trust)

- **Physical Ledger:** Must physically update `PROJECT_COSTS.json`. Simulations without file modification are strictly prohibited.
- **Budget Lock:** Automatically flags cost violations based on the physical JSON ledger.
- **Traceability:** Every transaction is logged with a correlation ID (CID) and timestamp.

## Protocol

1. **Ingestion:** Extract token counts and model mapping.
2. **Calculation:** Apply industrial pricing matrix.
3. **Accumulator:** Increment the persistent ledger in the project root.
4. **Guard:** Compare against budget limits and return status.

---
**ORIGIN:** [cost-tracker by akillness/oh-my-skills](https://skills.sh/akillness/oh-my-skills/cost-tracker)
*Skill v3.3.0-S | Status: Standardized & Industrialized.*
