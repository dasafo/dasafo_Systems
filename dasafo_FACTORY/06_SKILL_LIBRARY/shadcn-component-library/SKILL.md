---
version: 3.2.0-S
agent: FRONTEND_DEV
---

# 🎨 Skill | Shadcn Component Architecture

## Objective
Construct a modular, accessible, and themeable industrial UI library using Radix UI and Tailwind CSS, strictly adhering to the factory's Atomic Design system.

## 🛠️ Interface (v3.2.0-S)

### Input Schema (SkillInput.params)
- `component_name` (string): The shadcn/ui component to scaffold.
- `overrides` (object, optional): Custom Tailwind classes or variants.

### Output Schema (SkillOutput.result)
- `component_path`: (string) Destination in `/components/ui/`.
- `a11y_status`: (string) "VERIFIED".
- `design_token_compliance`: (boolean) True.

### ⚖️ Mandato SI (Sistema Internacional)
Toda dimensión de espaciado (gap, padding, margin) y tamaños de fuente deben definirse mediante tokens que correspondan a valores del SI o escalas rem/px normalizadas.

## Methodology
1.  **Selection:** Only include components strictly required for the current task in `/components/ui/`.
2.  **Atomic Base:** Buttons, Inputs, and Badges serve as the immutable atoms for complex organisms.
3.  **A11y (Accessibility):** Native support for keyboard navigation and ARIA labels.
4.  **Variants:** Use `cva` (Class Variance Authority) to manage industrial states (Primary, Danger, Ghost).

---
*Skill v3.2.0-S | Status: Standardized.*
