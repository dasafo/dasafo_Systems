# Skill: Shadcn Component Architecture
> **Source:** https://ui.shadcn.com/ (Adapted)
> **Agent:** FRONTEND_DEV

## Objective
Construct a modular, accessible, and themeable UI library based on Radix UI and Tailwind CSS.

## Methodology
- **Copy-Paste Pattern:** Only include components needed for the current task in `/components/ui/`.
- **Atomic Components:** Buttons, Inputs, and Badges must be the base for larger organisms.
- **Accessibility (A11y):** Every component must support keyboard navigation and ARIA labels.
- **Variants:** Use `cva` (Class Variance Authority) to manage component states (e.g., button primary/secondary/ghost).

## Deployment
All UI components MUST respect the factory's **Design Tokens** (Colors, Spacing, Radius).
