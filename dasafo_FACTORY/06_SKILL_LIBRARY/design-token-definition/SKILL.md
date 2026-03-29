---
version: 3.3.0-S
agent: Multiple (ARCHITECT / FRONTEND_DEV)
source: https://skills.sh/supercent-io/skills-template/design-token-definition
---

# 🎨 Skill | Design Token Definition

## Objective

Define the project's visual DNA (Tokens) to ensure the "Dasafo Vibe" (Glassmorphism, High-End Aesthetic) is consistent throughout the UI.

## 🛠️ Interface (v3.3.0-S)

### Input Schema (SkillInput.params)

- `action` (string, optional): "validate" | "export". Default "validate".
- `project_name` (string, optional): Name for documentation.

### Output Schema (SkillOutput.result)

- `tokens`: (object) JSON object containing design tokens.
- `status`: (string) "VALID" | "PREMIUM".
- `doc_path`: (string) Path to the `Visual_Standard.md`.

### ⚖️ Mandato SI (Sistema Internacional)

Los valores de espaciado (grid, gap) y tamaños de fuente deben reportarse preferiblemente en unidades relativas (rem, em) o absolutas del SI (mm) si se requiere precisión física.

## 🛡️ Industrial Constraints (Zero-Trust)

- **Immutable Definitions:** Tokens must be physically exported to `design_tokens.json`. Any visual change without an artifact update is a system violation.
- **Visual Standard Lock:** Physical existence of `DOCS/Visual_Standard.md` is mandatory for auditability.

## Workflow

1. **Scan Standards:** Read vibe rules from industrial knowledge.
2. **Produce Tokens:** Generate `design_tokens.json` in `LOCAL_KNOWLEDGE/architecture/`.
3. **Instruct:** Create `Visual_Standard.md` for `FRONTEND_DEV` consumption.

## Constraint

Reject any "plain" styles. Aesthetics must be PREMIUM.

---
**ORIGIN:** [design-token-definition by supercent-io](https://skills.sh/supercent-io/skills-template/design-token-definition)
*Skill v3.3.0-S | Status: Standardized & Industrialized.*
