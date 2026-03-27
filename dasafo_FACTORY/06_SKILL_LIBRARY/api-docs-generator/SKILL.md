---
version: 3.2.0-S
agent: ARCHITECT
---

# 📚 Skill | API Docs Generator

## Objective
Generate professional API documentation from backend contracts to ensure clarity for all project stakeholders.

## 🛠️ Interface (v3.2.0-S)

### Input Schema (SkillInput.params)
- `contract_path` (string, optional): Path to the OpenAPI contract. Defaults to `$TARGET_PROJECT/DOCS/API-CONTRACT.yaml`.
- `output_name` (string, optional): Name of the output file. Defaults to `API_REFERENCE.md`.

### Output Schema (SkillOutput.result)
- `markdown_docs`: (string) The generated markdown documentation content.
- `path`: (string) Absolute path where the documentation was saved.

### ⚖️ Mandato SI (Sistema Internacional)
Cualquier métrica mencionada en la documentación (límites de tiempo de respuesta, cuotas de datos, etc.) debe expresarse estrictamente en unidades del SI.

## Workflow
1.  **Ingest API Contracts:** Read the generated DTOs or OpenAPI specs from the Architect.
2.  **Contextualize:** Understand the business purpose of each endpoint (provided by Product Owner).
3.  **Format Markdown:** Use clean tables for parameters and clear examples for JSON request/responses.
4.  **Output:** Write to `$TARGET_PROJECT/DOCS/API_REFERENCE.md`.

---
*Skill v3.2.0-S | Status: Standardized.*
