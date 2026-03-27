---
version: 3.2.0-S
agent: RESEARCH_AGENT
---

# 🌉 Skill | MCP Capabilities Architect

## Objective
Design and propose new MCP (Model Context Protocol) capabilities for the factory's infrastructure, enabling self-evolving agentic tools.

## 🛠️ Interface (v3.2.0-S)

### Input Schema (SkillInput.params)
- `tool_need` (string): Description of the missing tool or API.
- `priority` (string, optional): "URGENT" | "HIGH" | "MEDIUM". Default "MEDIUM".

### Output Schema (SkillOutput.result)
- `proposal_path`: (string) Path to the `NEW_MCP_PROPOSAL.md`.
- `status`: (string) "PROPOSED".
- `vibe_check`: (string) "SCALABLE".

### ⚖️ Mandato SI (Sistema Internacional)
Cualquier parámetro de rendimiento de la nueva capability (latencia de API, throughput, carga computacional) debe proyectarse en unidades del SI.

## Workflow
1.  **Identify Gap:** Researcher identifies a missing tool (e.g. specialized API).
2.  **Design:** Use MCP standard to define resources, tools, and prompts.
3.  **Proposal:** Generate a `NEW_MCP_PROPOSAL.md` for the `ORCHESTRATOR`.

---
*Skill v3.2.0-S | Status: Standardized.*
