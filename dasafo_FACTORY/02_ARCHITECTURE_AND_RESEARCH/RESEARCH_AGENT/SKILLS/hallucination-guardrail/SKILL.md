# Skill: Hallucination Guardrail (NeMo)
> **Source:** https://skills.sh/davila7/claude-code-templates/nemo-guardrails
> **Agent:** RESEARCH_AGENT

## Objective
Perform fact-checking and consistency audits to ensure every research piece is 100% veracious and non-hallucinated.

## Guardrail Checks
1.  **Fact-Check:** Verify claims against the retrieved context from Exa or NotebookLM.
2.  **Safety Policy:** Ensure no PII or sensitive keys are exposed in research.
3.  **Self-Correction:** If the model detects an inconsistency in a benchmark, it MUST flag it and provide an alternative source.
4.  **Tone Check:** Enforce the **Surgical & Academic** voice in all responses.

## Rule of Truth
If a claim cannot be cited with a valid URL or paper ID, it must be presented as a "High-Risk Hypothesis" or removed.
