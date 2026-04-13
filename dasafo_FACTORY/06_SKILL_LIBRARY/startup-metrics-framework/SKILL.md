---
version: v5.0-MCP (Native)
agent_authorization: [PRODUCT_OWNER]
production_category: DEFINE
source: internal/financial-engine
protocol: Financial-Viability / DAST
---

> [ ⬆️ Up: [[../MOC_SKILL_LIBRARY]] | 📂 Global: [[../../_dasafo_FACTORY]] ]


# 📈 Skill | startup-metrics-framework

## Objective

Translate industrial execution metrics (Seconds, Bytes) into SaaS business KPIs (CAC, LTV, ROI). Used during Phase M1 to formulate the financial success criteria for the PRP_MASTER contract.

## 🛠️ Interface (v5.0-MCP Native)

**MANDATORY:** Use direct typed arguments. `params_json` is **DEPRECATED**.

### Typed Parameters

- `agent` (string): Your Agent ID (must be 'PRODUCT_OWNER').
- `target_project` (string): Absolute path to the project root.
- `business_model` (string): Business model type (e.g., 'B2B SaaS', 'B2C Freemium').
- `target_audience` (string): Primary end-user description.
- `estimated_execution_s` (float): (Optional) Expected server time per task in **Seconds (s)**.
- `isolate` (boolean): Execution in Clean Session.

## 🛡️ Industrial Constraints

- **SI-to-Financial Mapping:** All financial costs must be anchored to SI units (e.g., 1s of compute = $X cost).
- **LTV/CAC Ratio:** Enforce a minimum 3:1 ratio for project viability.
- **No Hallucinations:** Use realistic baseline estimates based on factory technical standards.

---

> [ ⬆️ Up: [[../MOC_SKILL_LIBRARY]] | 📂 Global: [[../../_dasafo_FACTORY]] ]

*Standard v5.0-MCP | Dasafo Factory Strategy Hub.*
