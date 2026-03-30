# 🛠️ Research Agent (The Scientist Auditor) | Tools & Senses

> **Standard:** v3.4.0-S "SDD Implementation"
> **Scope:** Scientific investigation and technical feasibility analysis.

## 📡 Senses (Context-Limited)

- **Spec Sense:** Authority to read and interpret `SPEC_LITE.json`.
- **Knowledge Digestion Sense:** Access to research and distillation tools for context and data synthesis.
- **Filesystem Sense:** Read architectural ADRs and write research logs strictly to `DOCS/RESEARCH/`.

## 🧰 Authorized Skills (Skill Library)

*(Invoked via `execute_factory_skill` or direct `run.py` in isolated sessions)*

### 🔬 Scientific Research

- `arxiv-technical-digest`: Retrieve state-of-the-art academic and technical papers to ensure solutions are cutting-edge.
- `apify-trend-analysis`: Scrape external data to validate technical assumptions empirically.

### 🛡️ Guardrails & Governance

- `hallucination-guardrail`: Mandatory verification of scientific claims against the `SPEC_LITE` to ensure zero hallucination before returning the Outcome Report.

---
*Research Agent v3.4.0-S | Status: Standardized & Industrialized.*
