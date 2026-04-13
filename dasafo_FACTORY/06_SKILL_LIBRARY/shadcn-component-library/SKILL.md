---
version: v5.0-MCP (Native)
agent_authorization: [FRONTEND_DEV]
production_category: BUILD
source: https://skills.sh/shadcn/ui/shadcn
protocol: Component-Composition / DAST
---

> [ ⬆️ Up: [[../MOC_SKILL_LIBRARY]] | 📂 Global: [[../../_dasafo_FACTORY]] ]


# 🎨 Skill | shadcn-component-library

## Objective

Systematically implement and manage professional UI components using the Shadcn/UI framework. Enforces the "Compose, Don't Reinvent" principle and a consistent, token-based design system.

## 🛠️ Interface (v5.0-MCP Native)

**MANDATORY:** Use direct typed arguments. `params_json` is **DEPRECATED**.

### Typed Parameters

- `agent` (string): Your Agent ID (must be 'FRONTEND_DEV').
- `target_project` (string): Absolute path to the project root.
- `action` (enum): `init`, `add`, `search`, `info`.
- `component` (string): (Optional) Name of the component (e.g., 'button', 'card').
- `overwrite` (boolean): (Optional) Bypass Redundancy Lock to update existing components.
- `isolate` (boolean): Execution in Clean Session.

## 🛡️ Industrial Constraints

- **Registry First:** Use Shadcn primitives before creating custom markup. Duplicating standard components is a **Cultural Violation**.
- **Token Consistency:** Use only semantic Tailwind tokens (e.g., `bg-primary`). Hex/RGB hardcoding is **FORBIDDEN**.
- **SI Standards:** Timing metrics MUST be in **Seconds (s)**.
- **DAST Sovereignty:** Components MUST be persisted in `WORKSPACE/frontend/components/ui/`.

---

> [ ⬆️ Up: [[../MOC_SKILL_LIBRARY]] | 📂 Global: [[../../_dasafo_FACTORY]] ]

**ORIGIN:** [shadcn by shadcn/ui](https://skills.sh/shadcn/ui/shadcn)
