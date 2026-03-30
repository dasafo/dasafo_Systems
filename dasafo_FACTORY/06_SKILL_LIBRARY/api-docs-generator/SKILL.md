---
version: 3.3.0-S
agent: ARCHITECT / DOCS_MASTER
source: https://skills.sh/sickn33/antigravity-awesome-skills/api-documentation-generator
---

# 📚 Skill | API Documentation Generator (v3.4.0-S)

## Objective

Transform physical API contracts (OpenAPI) into professional, user-friendly, and actionable Markdown documentation. This skill ensures that all stakeholders (Frontend, Mobile, QA, Clients) have clear, up-to-date guidance on how to consume the system's APIs.

## 🛠️ Interface (v3.4.0-S)

### Input Schema (SkillInput.params)

- `contract_path` (string, optional): Path to the OpenAPI contract (YAML). Defaults to `$TARGET_PROJECT/DOCS/API-CONTRACT.yaml`.
- `output_name` (string, optional): Name of the generated Markdown file. Defaults to `API_REFERENCE.md`.
- `include_examples` (boolean, optional): Default `true`. If `true`, generates code examples (cURL, Python, TS) for each endpoint.
- `target_project` (string, optional): Absolute path to the project workspace.

### Output Schema (SkillOutput.result)

- `markdown_docs`: (string) The generated markdown documentation content (truncated in output).
- `path`: (string) Absolute path where the documentation was saved.
- `summary`:
  - `endpoints_documented`: (integer) Count of endpoints parsed and documented.
  - `errors_documented`: (integer) Count of error response patterns found.
- `industrial_status`: (string) "SOLIDIFIED - PRO DOCS GENERATED"

### ⚖️ Mandato SI (Sistema Internacional)

Cualquier métrica mencionada en la documentación (límites de tiempo de respuesta, cuotas de datos, cuotas de peticiones) debe expresarse estrictamente en unidades del SI (segundos, bytes).

## 🛡️ Industrial Constraints (Zero-Trust)

- **Physical Parsing:** Must read and parse the physical YAML on disk. Mocking documentation from non-existent contracts is FORBIDDEN.
- **Reference Integrity:** All generated documentation must include a reference to the source contract and its version.

## 🧠 Documentation Workflow (v3.4.0-S)

1. **Ingest Specs:** Parse the OpenAPI 3.x contract from the Architect.
2. **Endpoint Specification:** Detail HTTP methods, URL paths, and authentication requirements.
3. **Request/Response Mapping:** Generate clear tables for parameters and body schemas.
4. **Usage Guidelines:** Add authentication setup, common use cases, and best practices.
5. **Code Samples:** Provide ready-to-use snippets for multiple languages.

---
**ORIGIN:** [api-documentation-generator by sickn33](https://skills.sh/sickn33/antigravity-awesome-skills/api-documentation-generator)
*Skill v3.4.0-S | Status: Standardized & Industrialized (Dasafo Edition).*
