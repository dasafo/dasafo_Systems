---
version: v4.0-S
agent: MARKETING_GROWTH / QA_TESTER / SECURITY_AUDITOR
source: https://skills.sh/pbakaus/impeccable/audit
---

# 🔍 Skill | Factory Audit Pro (v4.0-S)

## Objective

Perform an industrial-grade diagnostic scan and quality audit of project artifacts. This skill evaluates 5 key dimensions: Accessibility (A11y), Performance, Theming, Responsive Design, and Anti-Patterns. It produces a comprehensive **Audit Health Score** and a prioritized list of findings (P0-P3).

## 🛠️ Interface (v4.0-S)

### Input Schema (SkillInput.params)

- `target_path` (string, mandatory): Absolute path to the directory or file to audit.
- `dimensions` (array, optional): Default `["A11y", "Perf", "Theme", "Resp", "AntiPattern"]`.
- `severity_threshold` (enum, optional): Only report issues above this level (`P0`, `P1`, `P2`, `P3`).
- `strict_mode` (boolean, optional): Default `true`. Fails the audit if any P0 issues are found.

### Output Schema (SkillOutput.result)

- `health_score`: (integer) Total score (0-20) based on diagnostic criteria.
- `verdict`: (string) "PASS" | "FAIL" | "PASS_WITH_WARNINGS".
- `executive_summary`: (string) High-level overview of findings and health rating.
- `detailed_findings`: (array of objects) Issues with severity, category, location, and fix recommendation.
- `industrial_status`: (string) "AUDITED - SOLIDITY VERIFIED".

### ⚖️ Mandato SI (Sistema Internacional)

Cualquier métrica técnica en el informe (tiempos de carga, latencia de renderizado, tamaños de bundle, cuotas de memoria) debe expresarse estrictamente en unidades del SI (**segundos**, **bytes**).

## 🛡️ Industrial Constraints (Zero-Trust)

- **Physical Evidence:** Audits must be based on physical file analysis. Generic or "hallucinated" reports are strictly FORBIDDEN.
- **Brutal Honesty:** The "Anti-Patterns Verdict" must explicitly state if the code looks like low-quality AI generation.
- **Traceability:** Every finding must point to a specific file and line number.
- **No Direct Fixes:** This skill documents issues for specialized agents to fix; it does not modify the source code.

## 🧠 Audit Workflow (v4.0-S)

1. **Diagnostic Scan:** Run systematic checks across the 5 dimensions.
2. **Scoring:** Assign a score (0-4) to each dimension.
3. **P0 Detection:** Identify "Blocking" issues that prevent phase transition (Gate Lockdown).
4. **Report Generation:** Assemble findings into a structured audit report (`DOCS/AUDIT/`).
5. **Verdict:** Issue the final industrial verdict based on the health score and severity of issues.

---
**ORIGIN:** [audit by pbakaus](https://skills.sh/pbakaus/impeccable/audit)
*Skill v4.0-S | Status: Standardized & Industrialized (Dasafo Edition).*
