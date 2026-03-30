---
version: 3.4.0-S
agent: ARCHITECT / LEAD_DEV
source: https://skills.sh/wshobson/agents/architecture-decision-records
---

# 📝 Skill | Architecture Decision Records (ADR)

## Objective

Capture and manage technical decisions in a formal, searchable, and persistent log. This skill ensures that the "Why" behind every architectural choice is documented, enabling future agents and humans to understand the system's evolution and trade-offs.

## 🛠️ Interface (v3.4.0-S)

### Input Schema (SkillInput.params)

- `action` (string, optional): "new" (default) | "init" | "list" | "supersede".
  - `init`: Initialize the ADR directory and index.
  - `new`: Create a new ADR entry.
  - `list`: Show all current ADRs and their status.
  - `supersede`: Mark an old ADR as superseded by a new one.
- `title` (string, required for "new"): Short, descriptive title.
- `context` (string, optional): The problem background and constraints.
- `decision` (string, optional): The chosen solution and its rationale.
- `consequences` (string, optional): Trade-offs (positive/negative) resulting from the choice.
- `target_id` (string, required for "supersede"): The ID of the ADR being replaced (e.g., "0003").

### Output Schema (SkillOutput.result)

- `status`: (string) "SOLIDIFIED - ADR RECORDED" | "ADR_INDEX_UPDATED"
- `adr_path`: (string, optional) Path to the newly created ADR file.
- `adr_id`: (string, optional) Assigned sequential ID (e.g., "0021").
- `summary`: (list) Brief recap of the decision and its impact.

### ⚖️ Mandato SI (Sistema Internacional)

Cualquier métrica técnica mencionada en el ADR (ej: latencias < 200ms, almacenamiento > 50GB, ancho de banda > 1Gbps) debe expresarse estrictamente en unidades del SI (segundos, bytes).

## 🛡️ Industrial Constraints (Zero-Trust)

- **Sequential Integrity:** ADR IDs must be strictly sequential (0001, 0002...).
- **Physical Immutability:** Once an ADR is "ACCEPTED", it should only be changed via a "SUPERSEDE" action in a new ADR.
- **Index Sync:** Every new or updated ADR must trigger a physical update of the `DOCS/ADR/README.md` index.

## 🧠 Core Lifecycle (v3.4.0-S)

1. **Identify Decision:** Recognize a strategic choice (Pattern, Library, Infrastructure).
2. **Standard Format:** Use the MADR (Markdown Architecture Decision Record) template.
3. **Capture Rationale:** Document context, decision, and consequences.
4. **Lifecycle Management:** Transition states: `Proposed → Accepted → Deprecated → Superseded`.
5. **Update Index:** Ensure the central README reflects the current architectural state.

---
**ORIGIN:** [architecture-decision-records by wshobson](https://skills.sh/wshobson/agents/architecture-decision-records)
*Skill v3.4.0-S | Status: Standardized & Industrialized (Dasafo Edition).*
