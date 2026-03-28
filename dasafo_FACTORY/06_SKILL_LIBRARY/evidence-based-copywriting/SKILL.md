---
version: 3.2.0-S
agent: MARKETING_GROWTH
---

# 📝 Skill | Evidence-Based Copywriting

## Objective

Create persuasive, high-quality promotional and strategic content backed by technical and scientific evidence to ensure brand authority and trust.

## 🛠️ Interface (v3.2.0-S)

### Input Schema (SkillInput.params)

- `evidence_context` (string): The technical context or breakthrough to explain.
- `audience` (string, optional): Default "AI Developers".
- `tone` (string, optional): "hype" | "technical" | "balanced". Default "balanced".

### Output Schema (SkillOutput.result)

- `marketing_copy`: (string) Generated content with verified claims.
- `citations`: (list) References to ADRs, research, or codebase facts.
- `solidity_score`: (integer) Confidence level in the evidence (0-100).

### ⚖️ Mandato SI (Sistema Internacional)

Cualquier métrica de conversión proyectada o velocidad de lectura debe expresarse en unidades del SI (eventos por segundo, bits/segundo).

## 🛡️ Industrial Constraints (Zero-Trust)

- **LLM Lock:** This skill is physically locked if `OPENAI_API_KEY` or `ANTHROPIC_API_KEY` is missing. Hallucinating copy without a real LLM verification is banned.
- **Traceability:** Sources of evidence MUST be physically referenced from the `LOCAL_KNOWLEDGE/` directory.

## Verification Workflow

1. **Drafting:** Create value proposition based on project goals.
2. **Fact-Checking:** Verify claims against `RESEARCH_AGENT` and `DATA_SCIENTIST` findings.
3. **Citation:** Include technical breadcrumbs (ADRs, Papers, Code).
4. **Alignment:** Balance growth-hype with industrial scientific rigor.

---
*Skill v3.2.0-S | Status: Standardized.*
