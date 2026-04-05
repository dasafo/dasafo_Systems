---
version: v5.0-MCP (Native)
agent_authorization: [FRONTEND_DEV]
production_category: BUILD
source: https://skills.sh/wshobson/agents/design-system-patterns
protocol: Atomic-Design / DAST
---

# 💎 Skill | atomic-design-tokens

## Objective

Synchronize the UI implementation with a structured three-tier token hierarchy (Primitive, Semantic, Component).

## 🛠️ Interface (v5.0-MCP Native)

**MANDATORY:** Use direct arguments. Generic `params_json` is **DEPRECATED**.

### Typed Parameters

- `agent` (string): Your Agent ID (FRONTEND_DEV).
- `target_project` (string): Path to project root.
- `action` (enum): `init`, `add_token`, `generate`.
- `layer` (enum): `primitive`, `semantic`, `component`.
- `name` (string): Token name (e.g., 'primary-bg').
- `value` (string): Token value or reference.
- `overwrite` (boolean): Bypass Redundancy Lock.
- `isolate` (boolean): Clean Session execution.

## 🛡️ Industrial Constraints

- **Tier Integrity:** Component tokens MUST refer only to Semantic or Primitive tokens.
- **SI Mandate:** All measurements in **seconds (s)** and **bytes (B)**.
- **DAST Sovereignty:** CSS/JSON artifacts must exist in `ui/styles/`.

---
**ORIGIN:** [design-system-patterns by wshobson](https://skills.sh/wshobson/agents/design-system-patterns)
