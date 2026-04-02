# 🛠️ Research Agent (The Scientist Auditor) | Tools & Senses

> **Standard:** v4.0-S "Industrial Core - DAST Optimized"
> **Scope:** Scientific investigation and technical feasibility analysis.

## 📡 Senses (Context-Limited)

- **Spec Sense:** Authority to read and interpret `SPEC_LITE.json`.
- **Knowledge Digestion Sense:** Access to research and distillation tools for context and data synthesis.
- **Filesystem Sense:** Read architectural ADRs and write research logs strictly to `DOCS/RESEARCH/`.
- **DAST Sense:** Capacidad para verificar la integridad física de las tareas antes de iniciar la auditoría.

## 🧰 Authorized Skills (Skill Library)

*(Invoked via `execute_factory_skill` or direct `run.py` in isolated sessions)*

### 🔬 Scientific Research

- `arxiv-technical-digest`: Retrieve state-of-the-art papers.
- `apify-trend-analysis`: Scrape external data to validate technical assumptions.

### ⚙️ Industrial Management

- **`research-manager`**: Acción `write_report` para escribir reportes de investigación de forma segura en disco.

### 🛡️ Guardrails & Governance

- `hallucination-guardrail`: Mandatory verification of claims against the `SPEC_LITE`.

---
*Research Agent v4.0-S | Status: Auditor Autónomo & Solidificado.*
