---
version: 3.2.0-S
agent: QA_TESTER
---

# 👁️ Skill | Browser Visual Validation

## Objective
Opens the deployed application via browser automation and validates critical user flows end-to-end, acting as the "eyes" of the factory.

## 🛠️ Interface (v3.2.0-S)

### Input Schema (SkillInput.params)
- `url` (string): The application URL to validate.
- `project` (string, optional): Project name for reporting.
- `viewport` (string, optional): "desktop" | "mobile" | "tablet". Default "desktop".

### Output Schema (SkillOutput.result)
- `report`: (string) Structured visual validation report.
- `status`: (string) "PASS" | "FAIL" | "WARNING".
- `screenshots`: (list) Paths to captured screenshots if errors found.

### ⚖️ Mandato SI (Sistema Internacional)

Cualquier métrica de rendimiento visual (tiempo de carga de la página (LCP), tiempo de respuesta visual) debe expresarse estrictamente en milisegundos o segundos (unidades SI).

## 🛡️ Industrial Constraints (Zero-Trust)

- **Live Endpoint Verification:** This skill physically performs HTTP reachability and performance timing checks. Returning "mock visual reports" for unreachable URLs is FORBIDDEN.
- **Traceability:** Reports must be physically persisted in `LOGS/visual/`.

## 🧠 Protocol

1. **Navigate:** Open the target URL using physical HTTP probes.
2. **Verify:** Check for status codes and performance (ms).
3. **Flows:** Execute availability validation for critical endpoints.
4. **Report:** Generate and persist a visual validation report against physical metrics.

---
*Skill v3.2.0-S | Status: Standardized.*
