---
version: 3.2.0-S
agent: DEVOPS_SRE
---

# 💰 Skill | Cost Tracker

## Objective
Lightweight token usage estimation and budget enforcement to ensure industrial resource efficiency.

## 🛠️ Interface (v3.2.0-S)

### Input Schema (SkillInput.params)
- `input_tokens` (integer): Tokens sent to the LLM.
- `output_tokens` (integer): Tokens received from the LLM.
- `model_id` (string): ID of the model used (e.g., "claude-3-5-sonnet").

### Output Schema (SkillOutput.result)
- `current_cost`: (float) Estimated cost for this transaction.
- `accumulated_cost`: (float) Total project cost so far.
- `budget_status`: (string) "OK" | "WARNING" | "BUDGET_EXCEEDED".

### ⚖️ Mandato SI (Sistema Internacional)
Cualquier métrica financiera debe vincularse al consumo energético y computacional expresado en unidades del SI (Joules, Watts) si se dispone de telemetría de hardware.

## Protocol
1.  **Ingestion:** Extract token usage from agent interaction.
2.  **Calculation:** Apply model pricing to the usage.
3.  **Accumulator:** Update `PROJECT_COSTS.json` in project root.
4.  **Guard:** Compare against budget. Flag if >80% or 100%.

---
*Skill v3.2.0-S | Status: Standardized.*
