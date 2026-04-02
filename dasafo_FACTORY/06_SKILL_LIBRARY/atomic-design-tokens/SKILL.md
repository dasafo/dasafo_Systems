---
version: v4.0-S
agent: FRONTEND_DEV / UI_ARCHITECT
source: https://skills.sh/wshobson/agents/design-system-patterns
---

# 💎 Skill | Atomic Design Tokens & DS Patterns

## Objective

Synchronize the UI implementation with the ARCHITECT's global design system using a structured three-tier token hierarchy (Primitive, Semantic, Component). This skill ensures visual consistency, theme scalability, and automated UI synchronization across the project.

## 🛠️ Interface (v4.0-S)

### Input Schema (SkillInput.params)

- `action` (string, optional): "init" (default) | "add_token" | "generate".
  - `init`: Create the base token structure (Primitive, Semantic).
  - `add_token`: Assign a raw value to a primitive or a primitive to a semantic/component token.
  - `generate`: Export the design system to physical CSS/JSON artifacts.
- `layer` (string, optional): "primitive" | "semantic" | "component".
- `name` (string): The name of the token (e.g., `primary`, `button-bg`).
- `value` (string): The value or reference (e.g., `#3b82f6` or `var(--blue-500)`).
- `theme` (string, optional): "light" | "dark" | "all". Defaults to "all".
- `target_project` (string, optional): Absolute path to the UI project.

### Output Schema (SkillOutput.result)

- `status`: (string) "SYSTEM_INITIALIZED" | "TOKEN_LINKED" | "STYLE_GENERATED"
- `artifacts`: (list) Paths to the generated `tokens.css` or `tokens.json`.
- `hierarchy_report`:
  - `primitive_count`: (integer) Count of raw values.
  - `semantic_count`: (integer) Count of contextual aliases.
- `si_alignment`: (boolean) TRUE if all spacing/sizing follows SI units.

### ⚖️ SI Mandate (International System)

Any dimensional metrics (spacing, radii, widths) must be strictly expressed in the SI (using meters/millimeters, typically converted to relative `rem` units in CSS). Durations must be expressed in seconds (s).

## 🛡️ Industrial Constraints (Zero-Trust)

- **Tier Integrity:** Component tokens MUST refer only to Semantic or Primitive tokens. Direct hardcoding of hex/pixel values in Components is FORBIDDEN.
- **Physical Output:** Style artifacts must be physically written to `ui/styles/`. Mocks are invalid.
- **Naming Protocol:** Enforce consistent naming conventions (e.g., `--color-brand-primary`).

## 🧠 Design Patterns (v4.0-S)

1. **Token Hierarchy:**
   - **Primitive:** Raw colors, scales, and values.
   - **Semantic:** Abstract definitions (e.g., `text-primary`, `surface-elevated`).
   - **Component:** Usage-specific tokens (e.g., `button-primary-bg`).
2. **Theming Infrastructure:** Use CSS custom properties for effortless Light/Dark switching.
3. **Responsive Variants:** Integrate breakpoint tokens into the core system.

---
**ORIGIN:** [design-system-patterns by wshobson](https://skills.sh/wshobson/agents/design-system-patterns)
*Skill v4.0-S | Status: Standardized & Industrialized (Dasafo Edition).*
