# 🛠️ DOCS_MASTER | Tools & Senses (v4.0-MCP)

> **Standard:** v4.0-MCP "Industrial Core - DAST Optimized"
> **Scope:** Technical writing, automated docs extraction, and context synthesis.

## 📡 Senses (Context-Limited)

- **Spec Sense:** Authority to read and interpret `SPEC_LITE.json`.
- **Targeted File Sense:** Read access to code in `WORKSPACE/` and write access restricted strictly to `$TARGET_PROJECT/DOCS/`.
- **DAST Sense:** Ability to verify the physical integrity of artifacts and tasks.

## 🧰 Authorized Skills (Factory Engine)

*(CRITICAL: All skills MUST be invoked EXCLUSIVELY by passing their name to the `execute_industrial_skill` MCP Tool. Do NOT use bash).*

### 📝 Drafting & Analysis

- `api-docs-generator`: Automated extraction of documentation from backend codebases.
- `arxiv-technical-digest`: Retrieve state-of-the-art papers to enrich context.

### 🛡️ Guardrails

- `hallucination-guardrail`: Mandatory verification of technical claims against the project's source of truth.

---
*Docs Master v4.0-MCP | Status: Autonomous Strategist & Solidified.*
