---
version: 3.2.0-S
agent: ARCHITECT
---

# 📡 Skill | API Contract Generator

## Objective

Generate strict data contracts (DTOs) and documentation BEFORE logic implementation to decouple Frontend and Backend workers.

## 🛠️ Interface (v3.2.0-S)

### Input Schema (SkillInput.params)

- `action` (string, optional): Default "generate". Action to perform.
- `title` (string, optional): Title of the API.
- `version` (string, optional): API Version (e.g., "0.1.0").
- `target_project` (string, optional): Absolute path to the project.

### Output Schema (SkillOutput.result)

- `message`: (string) Success message or description.
- `spec`: (object, optional) The generated OpenAPI specification if not saved to file.
- `path`: (string, optional) Path to the generated contract file.

### ⚖️ Mandato SI (Sistema Internacional)

Cualquier métrica numérica generada (ej: latencias estimadas en el contrato, límites de tamaño de payload) debe usar el Sistema Internacional.

## 🛡️ Industrial Constraints (Zero-Trust)

- **Physical Write:** Contracts must be physically persisted to the filesystem. Mocking a "generated" state in memory without a corresponding `.yaml` file is FORBIDDEN.
- **Spec Validation:** Internally invokes `swagger-cli` or similar (physical check) to ensure the generated contract is valid OpenAPI before success.

## Workflow

1. **Analyze Demand:** Map requirements to physical endpoints.
2. **Generate Contract:** Create a physical `contract_v1.yaml`.
3. **Produce DTO Models:** Generate Pydantic/Zod models using current AST.
4. **Publish:** Persist to `$TARGET_PROJECT/DOCS/API-CONTRACT.yaml`.

## Rule of Decoupling

Backend and Frontend workers are FORBIDDEN to start coding logic until this contract has a `qa_passed: true` verdict from the Architect.

---
*Skill v3.2.0-S | Status: Standardized.*
