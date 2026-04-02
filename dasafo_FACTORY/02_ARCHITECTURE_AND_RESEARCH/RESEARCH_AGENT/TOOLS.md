# 🛠️ Research Agent (The Scientist Auditor) | Tools & Senses

> **Standard:** v4.0-S "Industrial Core - DAST Optimized"
> **Scope:** Scientific investigation and technical feasibility analysis.

## 📡 Senses (Context-Limited)

- **Spec Sense:** Authority to read and interpret `SPEC_LITE.json`.
- **Knowledge Digestion Sense:** Access to research and distillation tools for context and data synthesis.
- **Filesystem Sense:** Read architectural ADRs and write research logs strictly to `DOCS/RESEARCH/`.
- **DAST Sense:** Ability to verify the physical integrity of tasks before starting the audit.

## 🧰 Authorized Skills (Skill Library)

*(Invoked via `execute_factory_skill` or direct `run.py` in isolated sessions)*

### 🔬 Scientific Research

- `arxiv-technical-digest`: Retrieve state-of-the-art papers.
- `apify-trend-analysis`: Scrape external data to validate technical assumptions.

### ⚙️ Industrial Management

- **`research-manager`**: `write_report` action to safely write research reports to disk.

### 🛡️ Guardrails & Governance

- `hallucination-guardrail`: Mandatory verification of claims against the `SPEC_LITE`.

---
*Research Agent v4.0-S | Status: Autonomous Auditor & Solidified.*
