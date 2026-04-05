---
version: v5.0-MCP (Native)
agent_authorization: [FRONTEND_DEV]
production_category: BUILD
protocol: Aesthetic-Guard / DAST
---

# 🎨 Skill | frontend-ui-designer

## Objective

Enforce modern UI/UX design patterns (Tailwind, Shadcn) by verifying physical scaffolding before code generation. Ensures aesthetic consistency and industrial quality.

## 🛠️ Interface (v5.0-MCP Native)

**MANDATORY:** Use typed arguments. `params_json` is **DEPRECATED**.

### Typed Parameters

- `agent` (string): Your Agent ID (FRONTEND_DEV).
- `target_project` (string): Path to project root.
- `component_name` (string): Name of the component to design (e.g., 'HeroSection').
- `design_vibe` (string): (Optional) Aesthetic direction (e.g., 'glassmorphism').
- `isolate` (boolean): Execution in Clean Session.

## 🛡️ Industrial Constraints

- **Physical Containment:** Validations target strictly `WORKSPACE/frontend/`.
- **SI Standards:** Timing metrics MUST be in **Seconds (s)**.
- **Non-Hallucination:** If markers like `components.json` are missing, the status must reflect failure.

---
*Standard v5.0-MCP | Dasafo Factory Production Hub.*
