---
version: 3.2.0-S
agent: PRODUCT_OWNER
---

# 💎 Skill | Stakeholder Value Audit

## Objective
Detect and eliminate strategic biases, logical fallacies, and "Feature Fiction" in mission definitions, ensuring every requirement provides empirical functional value.

## 🛠️ Interface (v3.2.0-S)

### Input Schema (SkillInput.params)
- `input_text` (string): The requirement or request to audit.
- `threshold_si` (float, optional): Rigor level (0.0-1.0). Default 0.9.

### Output Schema (SkillOutput.result)
- `red_flags`: (list) Detected fallacies (Solution Spec, Stakeholder Fiction, etc.).
- `verdict`: (string) "PASS" | "CHALLENGE" | "REJECT".
- `suggested_correction`: (string) Realignment with Physics-Mindset.

### ⚖️ Mandato SI (Sistema Internacional)
Toda justificación de valor debe estar respaldada por métricas del SI o lógica de primer principio. Prohibido el uso de analogías vagas.

## Audit Workflow
1.  **Red Flag Detection:** Identify premature tech selection (Solution Spec) or imaginary needs.
2.  **Challenge Mechanism:** If a bias is detected, PAUSE and request the "Functional Value" (SI).
3.  **Realignment:** Transform vague requests into surgical, empirical requirements.
4.  **Ethics Guardrail:** Zero tolerance for non-vegetarian analogies or non-surgical voice.

---
*Skill v3.2.0-S | Status: Standardized.*
