# 📊 FACTORY EVALUATION METRICS (Quality Gate Ratios)

> **Objective:** Establishing mathematical and qualitative thresholds for evaluating the output of non-deterministic models before they are promoted to `04_ARCHIVE`.

---

## 🏗️ 1. Code Generation Evaluation (Backend/Frontend)

**Responsibility:** `QA_TESTER`

| Metric | Tolerance/Threshold | Consequence of Failure |
| :--- | :--- | :--- |
| **Separation of Concerns (SoC) Integrity** | 100% | Hard failure. Returning task to `05_REJECTED`. |
| **Docker Build Execution (Dry-Run)** | 0 Exit Code | Hard failure. Write to `FEEDBACK-LOG.md`. |
| **Design Token Adherence (Frontend)** | Zero hardcoded pixels/colors (must use `var(--Token)`) | Rejection with lint highlights. |
| **Atomic Completeness (Entry Points)** | All orphaned functions must have active triggers | Rejection for "Partial Work". |

---

## 🗣️ 2. Natural Language Generation (B2B Bots, AI-Workflow-Assistant)

**Responsibility:** `EVALUATOR` (Critic Meta-Agent)

| Metric | Constraint | Consequence of Failure |
| :--- | :--- | :--- |
| **Format Integrity** | 100% JSON/DAG compliance | Recursive retry with negative feedback prompt. |
| **Factual Halucination Ratio** | 0% acceptable on Internal Docs. | Task paused. Security auditor notified. |
| **Tone and Vibe Resonance** | High (Premium, Technical, Concise) | Warning emitted to `LOGS/agents/`. |

---

## 🔒 3. Security & Trust Validations

**Responsibility:** `SECURITY_AUDITOR` (Guardrail)

| Metric | Rule | Consequence of Failure |
| :--- | :--- | :--- |
| **Prompt Injection Detection** | Blocks "Ignore previous instructions", payload obfuscations. | Connection dropped. Incident logged. |
| **Data Exfiltration Prevention** | Blocks `SELECT * FROM users` if unauthorized. Masks Personal Identifiable Data (PII). | Hard Reject. Query nullified. |
| **Database SI Unity Verification** | 100% | Numeric values not respecting Pascal/Kelvin/Meters are rejected. |
