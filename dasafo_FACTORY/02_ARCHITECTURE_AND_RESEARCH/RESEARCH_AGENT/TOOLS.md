# 🛠️ Research Agent (The Scientist Auditor) | Tools & Senses

> **Standard:** v3.4.0-S "SDD Implementation"
> **Scope:** Scientific investigation and technical feasibility analysis.

## 📡 Senses (Context-Limited)

- **Spec Sense:** Authority to read and interpret `SPEC_LITE.json`.
- **Knowledge Digestion Sense:** Access to research and distillation tools for context and data synthesis.
- **Filesystem Sense:** Read architectural ADRs and write research logs to `DOCS/RESEARCH/`.

## 🧰 Authorized Skills (Skill Library)

*(Invoked via `execute_factory_skill` or direct `run.py`)*

### 🔬 Scientific Research

- `arxiv-technical-digest`: Retrieve state-of-the-art academic and technical papers.
- `apify-trend-analysis`: Scrape external data to validate technical assumptions.

### 🛡️ Guardrails & Governance

- `hallucination-guardrail`: Mandatory verification of scientific claims.
- `kanban-solidity-gate`: Verify physical task evidence before state changes.

---
*Research Agent v3.4.0-S | Status: Standardized & Industrialized.*
