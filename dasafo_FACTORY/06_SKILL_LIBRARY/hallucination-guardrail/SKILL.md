---
version: v5.0-MCP (Native)
agent_authorization: [MARKETING_GROWTH, RESEARCH_AGENT, DOCS_MASTER, QA_TESTER, DEPLOYMENT_MONITOR, DEVOPS_SRE, FACTORY_EVOLVER, MEMORY_OPTIMIZER]
production_category: VERIFY
source: https://skills.sh/davila7/claude-code-templates/nemo-guardrails
protocol: Fact-Checking / DAST
---

> [ ⬆️ Up: [[../MOC_SKILL_LIBRARY]] | 📂 Global: [[../../_dasafo_FACTORY]] ]


# 🛡️ Skill | hallucination-guardrail

## Objective

Enforce factual integrity and programmable safety for LLM outputs. Ensures all agent communication is grounded in physical project reality (DAST).

## 🛠️ Interface (v5.0-MCP Native)

**MANDATORY:** Use direct typed arguments. `params_json` is **DEPRECATED**.

### Typed Parameters

- `agent` (string): Your Agent ID.
- `content` (string): The text payload to be validated.
- `action` (enum): `check_fact`, `detect_jailbreak`, `sanitize_pii`.
- `context_path` (string): (Optional) Absolute path to the SSoT file for grounding.
- `strictness` (float): (Optional) 0.0 to 1.0 (default: 0.8).
- `isolate` (boolean): Execution in Clean Session.

## 🛡️ Industrial Constraints

- **Grounding Mandate:** Fact-checking MUST be performed against physical disk artifacts. No file = Failure.
- **Fail-Safe:** Any risk score > 0.5 blocks the output from the workspace.
- **SI Standards:** Reporting strictly in **Seconds (s)** and **Bytes (B)**.

---

> [ ⬆️ Up: [[../MOC_SKILL_LIBRARY]] | 📂 Global: [[../../_dasafo_FACTORY]] ]

**ORIGIN:** [nemo-guardrails by davila7](https://skills.sh/davila7/claude-code-templates/nemo-guardrails)
