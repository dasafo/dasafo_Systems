---
version: 3.3.0-S
agent: Multiple (FRONTEND / COPYWRITER / DOCS_MASTER)
source: https://skills.sh/supercent-io/skills-template/user-experience-copywriter
---

# ✨ Skill | User Experience Copywriter

## Objective

Apply advanced, persuasive, and premium copywriting to all product interfaces and manuals, ensuring industrial clarity and emotional alignment with the brand.

## 🛠️ Interface (v3.3.0-S)

### Input Schema (SkillInput.params)

- `component_strings` (list): Raw labels or messages to be rewritten.
- `target_tone` (string, optional): "Premium" | "Surgical" | "Empathetic". Default "Premium".

### Output Schema (SkillOutput.result)

- `optimized_copy`: (list) High-conversion industrial strings.
- `premium_vibe_check`: (string) "CONFIRMED".
- `readability_score`: (float) (0.0-1.0).

### ⚖️ Mandato SI (Sistema Internacional)

Toda mención a rendimientos técnicos en el microcopy (ej: "400ms speed") debe seguir estrictamente las magnitudes del SI.

## 🛡️ Industrial Constraints (Zero-Trust)

- **Vibe Lock:** Tone MUST strictly align with the `GLOBAL_USER.md` profile. Using playful or generic software jargon is FORBIDDEN.
- **Unit Compliance:** Documentation Strategist MUST audit all microcopy for SI Mandate before delivery to the UI layer.

## Strategy

1. **Microcopy Optimization:** Refine button labels, tooltips, and success banners for zero friction.
2. **Translate to Benefit:** Convert "Error: ConnectException" into benefit-driven guidance: "Network node re-stabilizing. Execution resuming in 500ms (SI)."
3. **Engagement Hooks:** Use clear industrial CTAs in onboarding flows.
4. **Aesthetic Verification:** Ensure the "look and feel" of the copy matches a high-tier industrial SaaS.

---
**ORIGIN:** [user-experience-copywriter by supercent-io](https://skills.sh/supercent-io/skills-template/user-experience-copywriter)
*Skill v3.3.0-S | Status: Standardized & Industrialized.*
