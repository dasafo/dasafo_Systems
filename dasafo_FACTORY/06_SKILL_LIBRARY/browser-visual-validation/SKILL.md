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

## 🧠 Protocol
1.  **Navigate:** Open the target URL using browser automation (Playwright/Puppeteer).
2.  **Verify:** Check for console errors, broken assets, and layout stability.
3.  **Flows:** Execute critical user flows (Auth, CRUD, Navigation).
4.  **Report:** Generate a visual validation report against PRP criteria.

---
*Skill v3.2.0-S | Status: Standardized.*
