---
version: v5.0-MCP (Native)
agent_authorization: [MARKETING_GROWTH, QA_TESTER, SECURITY_AUDITOR]
production_category: REVIEW
source: https://skills.sh/pbakaus/impeccable/audit
protocol: Quality-First / DAST
---

# 🔍 Skill | factory-audit-pro

## Objective

Execute a comprehensive quality audit evaluating performance, accessibility, and architectural anti-patterns. Basado en el estándar de **pbakaus**.

## 🛠️ Interface (v5.0-MCP Native)

**MANDATORY:** Use direct typed arguments. `params_json` is **DEPRECATED**.

### Typed Parameters

- `agent` (string): Your Agent ID.
- `target_path` (string): Absolute path to the audit target.
- `dimensions` (list): (Optional) Aspects to scan (e.g., `["Perf", "Theme"]`).
- `severity_threshold` (enum): Min severity to report (`P0` to `P3`).
- `strict_mode` (boolean): (Optional) Fail audit on any P0 finding.
- `isolate` (boolean): Execution in Clean Session.

## 🛡️ Industrial Constraints

- **Physical Evidence:** Reports MUST be physically saved in `LOGS/AUDITS/`.
- **SI Standards:** Technical metrics reported in **Seconds (s)** and **Bytes (B)**.
- **Brutal Honesty:** Mandatory reporting of "AI-slop" or low-quality generation.

---
**ORIGIN:** [audit by pbakaus](https://skills.sh/pbakaus/impeccable/audit)
