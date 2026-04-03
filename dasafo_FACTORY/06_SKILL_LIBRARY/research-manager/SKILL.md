---
version: v5.0-MCP (Native)
agent_authorization: [RESEARCH_AGENT]
source: custom_dasafo_factory
protocol: Research-Persistence / DAST
---

# 🔬 Skill | research-manager

## Objective

Safely manage and persist deep-research artifacts, architectural investigations, and API evaluations to the disk. Eliminates terminal syntax errors and shell injection risks.

## 🛠️ Interface (v5.0-MCP Native)

**MANDATORY:** Use typed arguments. `params_json` is **DEPRECATED**.

### Typed Parameters

- `agent` (string): Your Agent ID (must be 'RESEARCH_AGENT').
- `target_project` (string): Absolute path to the project root.
- `report_name` (string): Exact name of the markdown file (e.g., 'RESEARCH_AI_MODELS.md').
- `content` (string): Full markdown content of the research.
- `category` (enum): `RESEARCH` (default), `ARCH`, `MARKETING`.
- `isolate` (boolean): Execution in Clean Session.

## 🛡️ Industrial Constraints

- **No Shell Escaping:** Using `cat <<EOF` in standard bash/zsh for reports is **STRICTLY FORBIDDEN**.
- **Sovereign Routing:** Artifacts are strictly routed to the `DOCS/` hierarchy.
- **SI Standards:** Size in **Bytes (B)** and time in **Seconds (s)**.

---
*Standard v5.0-MCP | Dasafo Factory Research Hub.*
