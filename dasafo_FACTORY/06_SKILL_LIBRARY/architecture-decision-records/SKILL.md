---
version: 3.3.0-S
agent: Multiple (ARCHITECT / DB_MASTER / BACKEND)
source: https://skills.sh/supercent-io/skills-template/architecture-decision-records
---

# 📝 Skill | Architecture Decision Records (ADR)

## Objective

Establish a formal, immutable log of technical decisions, explaining the "Why" behind the "How" for every $TARGET_PROJECT.

## 🛠️ Interface (v3.3.0-S)

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

## 🛡️ Industrial Constraints (Zero-Trust)

- **Immutable Persistence:** ADRs must be physically written to `DOCS/ADR/` within the `TARGET_PROJECT`. Failure to write a physical artifact results in skill failure.
- **Sequential Integrity:** The skill verifies the current physical list of ADRs to suggest the next ID, avoiding collisions in a multi-agent environment.

## Workflow

1. **Draft:** Create an ADR when a significant tech stack or structural choice is made.
2. **Format:** Use the MADR format (Context, Alternatives, Decision, Consequences).
3. **Persist:** Physically save in `$TARGET_PROJECT/DOCS/ADR/ADR-XXX-title.md`.
4. **Index:** Maintain a physical `README.md` index in the same folder.

---
**ORIGIN:** [architecture-decision-records by supercent-io](https://skills.sh/supercent-io/skills-template/architecture-decision-records)
*Skill v3.3.0-S | Status: Standardized & Industrialized.*
