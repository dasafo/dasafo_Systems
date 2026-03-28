---
version: 3.2.0-S
agent: BACKEND_DEV
---

# ⚡ Skill | Async FastAPI Logic

## Objective
Master high-performance asynchronous logic and skeleton generation for FastAPI endpoints.

## 🛠️ Interface (v3.2.0-S)

### Input Schema (SkillInput.params)
- `route_name` (string): Name of the function/route.
- `method` (string, optional): HTTP Method (GET, POST, etc.). Default "GET".
- `target_project` (string, optional): Absolute path to save the generated logic.

### Output Schema (SkillOutput.result)
- `code_skeleton`: (string) The generated async FastAPI code.
- `path`: (string, optional) Path where the code was saved.

### ⚖️ Mandato SI (Sistema Internacional)

Cualquier métrica técnica definida en los endpoints (tiempos de timeout, límites de memoria, tamaños de archivo) debe seguir el Sistema Internacional.

## 🛡️ Industrial Constraints (Zero-Trust)

- **AST Scaffold:** This skill physically writes `.py` files to the repository. It MUST verify the target path exists.
- **Pattern Strictness:** Logic skeletons must strictly follow the `v3.2.0-S` Modular Toolbox standards for SoC (Separation of Concerns).

## Constraints (Must-Follow)

- **Async Only:** Always use `async def` for endpoints and I/O bound tasks.
- **JWT Security:** Implement secure authentication using `PyJWT` and OAuth2 password flow.
- **Background Tasks:** Use FastAPI `BackgroundTasks` for non-blocking operations.
- **Environment Safety:** NEVER hardcode secrets. Use `pydantic-settings` to load from `.env`.

---
*Skill v3.2.0-S | Status: Standardized.*
