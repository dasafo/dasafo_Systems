---
version: 3.2.0-S
agent: FRONTEND_DEV
---

# 💎 Skill | Atomic Design Tokens

## Objective
Synchronize the UI implementation with the ARCHITECT's global design system using semantic tokens to ensure visual consistency.

## 🛠️ Interface (v3.2.0-S)

### Input Schema (SkillInput.params)
- `theme` (string, optional): "dark" | "light". Default "dark".
- `target_project` (string, optional): Absolute path to the UI project.

### Output Schema (SkillOutput.result)
- `tokens`: (object) Map of semantic CSS variables.
- `theme`: (string) The applied theme.
- `path`: (string, optional) Path where tokens were written (if applicable).

### ⚖️ Mandato SI (Sistema Internacional)

Cualquier unidad de medida en el sistema de diseño (espaciado en milímetros/pixels, tiempos de animación en milisegundos) debe estar alineada con el SI para escalabilidad global.

## 🛡️ Industrial Constraints (Zero-Trust)

- **Token Sync:** This skill physically writes `tokens.json` to the UI project. Mocks are detected via missing theme artifacts.
- **Theme Guard:** Requires a valid `TARGET_PROJECT` mapping to verify visual persistence.

## Protocol

1. **Ingest:** Read the latest `DESIGN_TOKENS.json` from the Architecture folder.
2. **Translate:** Map tokens to `tailwind.config.js` or CSS variables.
3. **Implement:** Physically write semantic classes to the stylesheet artifacts.

## Constraints

- **NO HARDCODED COLORS:** Every hex code or spacing unit must be a token.
- **Theme Support:** Native support for Dark/Light modes.

---
*Skill v3.2.0-S | Status: Standardized.*
