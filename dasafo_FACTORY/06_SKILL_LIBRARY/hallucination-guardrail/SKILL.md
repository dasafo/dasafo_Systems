---
version: 3.2.0-S
agent: RESEARCH_AGENT
---

# 🛡️ Skill | Hallucination Guardrail

## Objective
Enforce fact-checking and consistency audits to ensure every research piece produced by the factory is 100% veracious and context-backed.

## 🛠️ Interface (v3.2.0-S)

### Input Schema (SkillInput.params)
- `content` (string): The research text to audit.
- `sources_path` (string, optional): Path to the `research_nexus.md` or similar.

### Output Schema (SkillOutput.result)
- `verdict`: (string) "TRUE" | "HIGH_RISK_HYPOTHESIS" | "HALLUCINATION".
- `flags`: (list) Identified inconsistencies or unverified claims.
- `confidence_score`: (integer) (0-100).

### ⚖️ Mandato SI (Sistema Internacional)
Cualquier desviación en benchmarks numéricos o métricas de sistema comparadas debe reportarse estrictamente bajo el SI.

## Guardrail Checks
1.  **Fact-Check:** Verify claims against retrieved industrial context.
2.  **Safety Policy:** Ensure Zero-Trust (no PII or hardcoded secrets).
3.  **Self-Correction:** Flag benchmark inconsistencies and suggest alternative verified sources.
4.  **Tone:** Enforce Surgical & Academic voice.

---
*Skill v3.2.0-S | Status: Standardized.*
