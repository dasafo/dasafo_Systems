---
version: 3.4.0-S
agent: FRONTEND_DEV
source: https://skills.sh/shadcn/ui/shadcn
---

# 🎨 Skill | Shadcn Component Library (v3.4.0-S)

## Objective

Systematically implement and manage professional, accessible, and premium UI components using the Shadcn/UI framework. This skill enforces the "Compose, Don't Reinvent" principle, utilizing the Shadcn CLI to scaffold components and maintain a consistent, token-based design system.

## 🛠️ Interface (v3.4.0-S)

### Input Schema (SkillInput.params)

- `action` (enum): `init`, `add`, `search`, `info`, `docs`.
- `target_project` (string, mandatory): Absolute path to the frontend project.
- `component` (string, optional): Name of the component to add or search (e.g., `button`, `card`, `tabs`).
- `preset` (string, optional): Preset code for initialization (e.g., `new-york-dark`).

### Output Schema (SkillOutput.result)

- `status`: (string) "SOLIDIFIED - COMPONENT ADDED" | "CONFIG_GENERATED"
- `artifacts_created`: (array) List of paths to the newly created component files.
- `composition_report`: (string) Summary of the component's role in the UI hierarchy.
- `industrial_status`: (string) "VERIFIED - SHADCN COMPLIANT".

### ⚖️ Mandato SI (Sistema Internacional)

Cualquier métrica técnica en el frontend (tiempos de renderizado, latencia de interacción, tamaños de bundle de componentes, cuotas de memoria del navegador) debe expresarse estrictamente en unidades del SI (**segundos**, **bytes**).

## 🛡️ Industrial Constraints (Zero-Trust)

- **Registry First:** Use `npx shadcn@latest search` before creating custom markup. Custom components that replicate Shadcn functionality are FORBIDDEN.
- **Token Consistency:** Use only semantic Tailwind tokens (`bg-primary`, `text-muted-foreground`). Hardcoded hex/rgb values are STRICTLY BANNED.
- **Composition Rule:** Complex UIs must be built by composing atomic components (e.g., `Dashboard = Sidebar + Card + Table`).
- **Icons Policy:** Pass icons as React objects, not string keys. Use `data-icon="inline-start"` for positioning inside buttons.
- **No Custom Pulse:** Use the `Skeleton` component for all loading states. Custom `animate-pulse` divs are disallowed.

## 🧠 Frontend Workflow (v3.4.0-S)

1. **Information Gathering:** Detect the project context using `npx shadcn@latest info`.
2. **Component Retrieval:** Add necessary components using the CLI: `npx shadcn@latest add <component>`.
3. **Styling Integration:** Apply semantic tokens and variants (`variant="outline"`, `size="sm"`) to match the design system.
4. **Composition:** Assemble full pages using the provided components as building blocks.
5. **Validation:** Ensure accessibility standards and visual regression checks pass.

---
**ORIGIN:** [shadcn by shadcn/ui](https://skills.sh/shadcn/ui/shadcn)
*Skill v3.4.0-S | Status: Standardized & Industrialized (Dasafo Edition).*
