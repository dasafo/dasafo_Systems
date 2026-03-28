---
version: 3.2.0-S
agent: SECURITY_AUDITOR
---

# 🛡️ Skill | OWASP LLM Top-10 Enforcement

## Objective

Enforce strict security controls specifically designed for Large Language Model applications, following the industry-standard OWASP Top-10 for LLMs.

## 🛠️ Interface (v3.2.0-S)

### Input Schema (SkillInput.params)

- `scope` (string, optional): "tools" | "mcp" | "prompts" | "all". Default "all".
- `report_mode` (boolean, optional): Default `true`.

### Output Schema (SkillOutput.result)

- `posture_score`: (integer) Security health (0-100).
- `vulnerabilities_found`: (list) List of identified Top-10 risks.
- `remediation_plan`: (string) Markdown plan to fix leaks.

### ⚖️ Mandato SI (Sistema Internacional)

Cualquier exposición de datos (tamaño de la fuga en bytes, tiempo de exposición en segundos) debe reportarse en el SI.

## 🛡️ Industrial Constraints (Zero-Trust)

- **Verification Mandatory:** Posture scores MUST be derived from physical audits of `TOOLS.md`, `SKILL.md`, and MCP deployments. Hallucinating security scores is FORBIDDEN.
- **Remediation Persistence:** Every remediation plan MUST be physically saved to `DOCS/SECURITY/` to be considered `success`.

## High-Priority Risk Vectors

1. **LLM01 Prompt Injection:** Filter direct and recursive injections.
2. **LLM02 Insecure Output Handling:** Prevent XSS or CLI injection via model output.
3. **LLM06 Sensitive Data Disclosure:** Block proprietary architectural leakage.
4. **LLM08 Insecure Plugin Design:** Audit `TOOLS.md` and MCP definitions.

---
*Skill v3.2.0-S | Status: Standardized.*
