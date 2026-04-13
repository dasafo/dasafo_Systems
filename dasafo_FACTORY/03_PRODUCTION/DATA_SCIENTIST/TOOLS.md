# 🛠️ DATA_SCIENTIST | Tools & Senses (v5.0-MCP)

> [ ⬆️ Up: [[../MOC_PRODUCTION]] | 📂 Index: [[MOC_DATA_SCIENTIST]] ]

> **Standard:** v5.0-MCP "Industrial Core - DAST Optimized"
> **Scope:** Data analysis, model training, and empirical metric generation.

## 📡 Senses (Context-Limited)

- **Spec Sense:** Authority to read and interpret `SPEC_LITE.json`.
- **Targeted File Sense:** Read/Write access restricted to `WORKSPACE/data/`, `DOCS/RESEARCH/`, and specific `context_pointers`.
- **DAST Sense:** Ability to verify the physical integrity of datasets and tasks before starting training processes.
- **Terminal Sense:** Execution of Python (pandas, scikit-learn, etc.) and data pipelines locally.

## 🧰 Authorized Skills (Skill Library)

*(CRITICAL: All skills must be executed **directly by name** (e.g., the tool name matches the skill name)).*

*(Lazy loaded only when mandated by the Spec)*

- `autonomous-feedback-analyzer`: Deep synthesis of data patterns, logs, and telemetry.
- `apify-trend-analysis`: Scraping external datasets for model enrichment.
- `agentic-thought-secret-scanner`: Mandatory check to ensure no PII or API keys leak into output datasets.

---
*Data Scientist v5.0-MCP | Status: Autonomous Insight Guardian & Solidified.*
