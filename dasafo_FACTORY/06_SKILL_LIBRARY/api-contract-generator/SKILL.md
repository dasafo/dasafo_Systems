---
version: v4.0-S
agent: ARCHITECT / BACKEND_DEV
source: https://skills.sh/jeffallan/claude-skills/api-designer
---

# 📡 Skill | API Designer & Contract Generator

## Objective

Design and maintain industrial-grade API contracts (OpenAPI 3.1) by following a "Design-First" methodology. This skill ensures that APIs are resource-oriented, consistent, and semantically correct, providing a solid foundation for both Frontend and Backend workers.

## 🛠️ Interface (v4.0-S)

### Input Schema (SkillInput.params)

- `action` (string, optional): "design" (default) | "lint" | "analyze".
  - `design`: Create a new resource-oriented OpenAPI 3.1 contract.
  - `lint`: (Mock/Rec) Validate the contract using Redocly rules.
  - `analyze`: Scan the codebase to extract endpoints (Legacy support).
- `resource` (string, optional): Name of the primary resource (e.g., `user`, `order`).
- `specification` (object, optional): Data model definition if design-first.
- `target_project` (string, optional): Absolute path to the active project.

### Output Schema (SkillOutput.result)

- `status`: (string) "SOLIDIFIED - PRO DESIGN"
- `contract_path`: (string) Path to the YAML file.
- `validation_report`: (list, optional) Results from linting/validation.
- `design_summary`:
  - `resource_entity`: (string) Primary entity name.
  - `endpoints_count`: (integer) Count of generated/active endpoints.
  - `standards_compliance`: (string) "OpenAPI 3.1 + RFC 7807"

### ⚖️ Mandato SI (Sistema Internacional)

Cualquier métrica numérica (latencias, tamaños de payload, cuotas) debe expresarse estrictamente en unidades del Sistema Internacional (segundos, bytes).

## 🛡️ Industrial Constraints (Zero-Trust)

- **RESTful Enforcement:** Resource-oriented URIs only. Verbs in URIs (e.g., `/getUser`) are FORBIDDEN.
- **Error Reliability (RFC 7807):** All error responses must follow the Problem Details standard.
- **OpenAPI 3.1 ONLY:** This skill is physically locked to the latest industry standard for contracts.
- **Physical Proof:** Must write files to `DOCS/API-CONTRACT.yaml`.

## 🧠 Core Workflow (v4.0-S)

1. **Analyze Domain:** Understand business requirements and data models.
2. **Model Resources:** Identify resources, relationships, and operations before writing the spec.
3. **Design Endpoints:** Define URI patterns (snake_case), HTTP methods, and request/response schemas.
4. **Specify Contract:** Create the physical OpenAPI 3.1 specification.
5. **Lint and Verify:** Recommend/simulate `npx @redocly/cli lint` to ensure quality.

---
**ORIGIN:** [api-designer by jeffallan](https://skills.sh/jeffallan/claude-skills/api-designer)
*Skill v4.0-S | Status: Standardized & Industrialized (Dasafo Edition).*
