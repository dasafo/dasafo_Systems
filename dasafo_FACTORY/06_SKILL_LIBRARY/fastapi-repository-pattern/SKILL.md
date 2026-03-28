---
version: 3.2.0-S
agent: BACKEND_DEV
---

# 🏗️ Skill | FastAPI Repository Pattern

## Objective

Implement a structured, scalable application architecture using Repository and Service patterns in FastAPI to ensure high modularity and testability.

## 🛠️ Interface (v3.2.0-S)

### Input Schema (SkillInput.params)

- `module_name` (string): Name of the new module (e.g., "users").
- `target_project` (string, optional): Absolute path to the project.

### Output Schema (SkillOutput.result)

- `scaffold_status`: (string) "CREATED" | "UPDATED".
- `files_generated`: (list) List of absolute paths created.
- `vibe_check`: (string) "SOLID".

### ⚖️ Mandato SI (Sistema Internacional)

Cualquier métrica de rendimiento de la API (latencia media en ms, bytes de payload) debe ser reportada bajo el Sistema Internacional de Unidades.

## 🛡️ Industrial Constraints (Zero-Trust)

- **Physical Scaffolding:** This skill physically executes `mkdir` and `touch` for project modules. It MUST verify `TARGET_PROJECT` existence before execution.
- **SoC Enforcement:** Enforces strict boundary separation (Repository -> Service -> API) via physical folder structure.

## Key Patterns

- **Service Layer:** All complex business logic MUST reside in `/services/`.
- **Repository Pattern:** Isolated database access logic in `/repositories/`.
- **Injection:** Mandatory use of FastAPI `Depends()` for dependency management.

## Workflow

1. **Structure:** Scaffolding of `/app` with models, schemas, api, services, and repositories.
2. **DTO Compliance:** Enforce Pydantic schemas from the Architect's 1:1 blueprint.
3. **Clean Code:** PEP 8 compliance and mandatory type hinting.

---
*Skill v3.2.0-S | Status: Standardized.*
