---
name: frontend-ui-designer
description: Enforces modern UI/UX design patterns using Tailwind CSS, shadcn/ui, and Lucide icons. Use this skill when generating or refactoring React/Next.js frontend components to ensure aesthetic consistency and industrial quality.
---

# 🎨 Skill | Frontend UI Designer (v4.0-S)

## Objective

Act as the UI/UX standard enforcer for the dasafo_Factory. Ensure that all generated React/Next.js components strictly adhere to modern design principles, utilizing Tailwind CSS for styling, `shadcn/ui` for accessible component foundations, and `lucide-react` for iconography.

## 🛠️ Interface (v4.0-S)

### Input Schema (SkillInput.params)

- `target_project` (string, mandatory): Absolute path to the project root.
- `component_name` (string, mandatory): Name of the component to be designed (e.g., `HeroSection`, `LoginForm`).
- `design_vibe` (string, optional): Aesthetic direction (e.g., "dark mode, glassmorphism, minimalistic").

### Output Schema (SkillOutput.result)

- `design_system_verified`: (boolean) Confirmation that Tailwind and UI libraries are present physically.
- `scaffold_path`: (string) The physical path where the component should be written.
- `execution_time_s`: (float) Validation time in seconds.

## 🧠 Industrial Constraints & Best Practices

- **Component Anatomy:** Build components using functional React components with standard hooks.
- **Styling Standards:** Rely exclusively on Tailwind CSS utility classes. Avoid custom CSS files unless strictly necessary for animations not supported by Tailwind.
- **Accessibility (a11y):** Prioritize accessible semantic HTML and Radix UI primitives (via shadcn).
- **Physical Containment:** Always resolve paths to `WORKSPACE/frontend/components/` or `WORKSPACE/frontend/app/`. Never write UI logic to the backend.

## 🚀 Execution Guide

1. Receive the target component requirement from the `SPEC_LITE.json`.
2. Run this skill to physically verify the frontend design system (Tailwind/Shadcn) is initialized.
3. Once `design_system_verified` is True, generate the component applying the requested `design_vibe`.
