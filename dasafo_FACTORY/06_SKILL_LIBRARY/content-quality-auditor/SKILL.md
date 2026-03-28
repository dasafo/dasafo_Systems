---
version: 3.2.0-S
agent: MARKETING_GROWTH
---

# 🔎 Skill | Content Quality Auditor

## Objective
A 50-point automated audit of marketing and technical content to ensure it meets CORE and EEAT (Experience, Expertise, Authoritativeness, Trustworthiness) standards.

## 🛠️ Interface (v3.2.0-S)

### Input Schema (SkillInput.params)
- `content_path` (string): Absolute path to the file or directory to audit.
- `audit_type` (string, optional): "marketing" | "technical" | "full". Default "full".

### Output Schema (SkillOutput.result)
- `score`: (integer) Audit score (0-50).
- `status`: (string) "PASS" | "FAIL".
- `report_path`: (string) Absolute path to the audit report.

### ⚖️ Mandato SI (Sistema Internacional)

Cualquier métrica de legibilidad (palabras por minuto, bytes de densidad informativa) debe reportarse bajo unidades del SI.

## 🛡️ Industrial Constraints (Zero-Trust)

- **Physical Audit:** Requires a valid file target on disk. Generating an audit score for a non-existent file path results in skill failure.
- **Determinism:** Metrics (word count, chars) must be physically computed from the artifact's content.

## The Audit Protocol

1. **Veto Check:** Disclosure status, Intent alignment, Consistency.
2. **CORE Dimensions:** Context, Organization, Referenceability, Exclusivity.
3. **EEAT Scan:** Compute text density via physical word count.

---
*Skill v3.2.0-S | Status: Standardized.*
