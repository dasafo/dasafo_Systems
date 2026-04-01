---
version: v4.0-S
agent: MEMORY_OPTIMIZER / SECURITY_AUDITOR / MARKETING_GROWTH
source: https://skills.sh/davila7/claude-code-templates/nemo-guardrails
---

# 🛡️ Skill | Hallucination Guardrail (v4.0-S)

## Objective

Enforce programmable safety and factual integrity for LLM outputs. This skill prevents hallucinations, jailbreak attempts, and PII leaks using defined guardrails (NeMo style). It ensures that agent communications are grounded in physical project reality and follow industrial safety protocols.

## 🛠️ Interface (v4.0-S)

### Input Schema (SkillInput.params)

- `action` (enum): `check_fact`, `detect_jailbreak`, `sanitize_pii`, `self_check_output`.
- `content` (string, mandatory): The text to be validated.
- `context_path` (string, optional): Absolute path to the SSoT (Single Source of Truth) to verify facts against.
- `strictness` (float, optional): 0.0 to 1.0 (default 0.8).

### Output Schema (SkillOutput.result)

- `is_safe`: (boolean)
- `hallucination_detected`: (boolean)
- `risk_score`: (float) 0-1 scale.
- `corrected_content`: (string, optional) Content with sanitized PII or corrected facts.
- `industrial_verdict`: (string) "SOLIDIFIED - CONTENT SAFE" | "BLOCKED - HALLUCINATION DETECTED"

### ⚖️ Mandato SI (Sistema Internacional)

Cualquier métrica de rendimiento del modelo (tiempos de inferencia, latencia de respuesta, cuotas de tokens) debe expresarse estrictamente en el SI (**segundos**, (**bytes** para memoria de contexto).

## 🛡️ Industrial Constraints (Zero-Trust)

- **Grounding Required:** Fact-checking MUST be done against physical files (`PROJECT_STATE.json`, `ADRs`, etc.). If no file is provided, the check fails by default.
- **Fail-Safe Mode:** If the risk score exceeds 0.5, the output is blocked from the project workspace.
- **No Self-Correction:** The skill identifies issues but does not silently rewrite logic; it reports the violation for the `MEMORY_OPTIMIZER` to handle.

## 🧠 Protection Workflow (v4.0-S)

1. **Input Interception:** Catch the proposed content before it reaches the `PROJECTS/` workspace.
2. **Context Retrieval:** Fetch the latest physical artifacts from the designated project root.
3. **Verification:**
   - **Jailbreak Detection:** Scan for prompt injection patterns.
   - **Fact Verification:** Compare claims against the physical SSoT.
   - **PII Masking:** Identity and mask sensitive data.
4. **Scoring:** Assign a reliability/risk score.
5. **Verdict:** Return an industrial PASS/FAIL signal.

---
**ORIGIN:** [nemo-guardrails by davila7](https://skills.sh/davila7/claude-code-templates/nemo-guardrails)
*Skill v4.0-S | Status: Standardized & Industrialized (Dasafo Edition).*
