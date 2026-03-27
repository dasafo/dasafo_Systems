---
version: 3.2.0-S
agent: ARCHITECT
---

# 📝 Skill | Architecture Decision Records (ADR)

## Objective
Establish a formal, immutable log of technical decisions, explaining the "Why" behind the "How" for every $TARGET_PROJECT.

## 🛠️ Interface (v3.2.0-S)

### Input Schema (SkillInput.params)
- `id` (string, optional): Target ADR ID (e.g., "0001").
- `title` (string): Descriptive title of the decision.
- `context` (string): Problem statement and technical context.
- `decision` (string): The chosen solution and rationale.
- `alternatives` (string, optional): Other options considered.
- `consequences` (string, optional): Trade-offs and impact.

### Output Schema (SkillOutput.result)
- `path`: (string) Absolute path to the created ADR file.
- `status`: (string) "ACCEPTED" | "PROPOSED".

### ⚖️ Mandato SI (Sistema Internacional)
Cualquier métrica técnica referenciada en el ADR (ej: tiempos de respuesta requeridos, límites de memoria, anchos de banda) debe utilizar obligatoriamente el Sistema Internacional.

## Workflow
1.  **Draft:** Create an ADR when a significant tech stack or structural choice is made.
2.  **Format:** Use the MADR format (Context, Alternatives, Decision, Consequences).
3.  **Persist:** Save in `$TARGET_PROJECT/DOCS/ADR/ADR-XXX-title.md`.
4.  **Index:** Maintain a `README.md` index in the same folder with the current status of each ADR (Accepted, Deprecated, Proposed).

---
*Skill v3.2.0-S | Status: Standardized.*
