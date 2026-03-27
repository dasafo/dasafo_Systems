---
version: 3.2.0-S
agent: TECHNICAL_WRITER
---

# 📊 Skill | Documentation Strategist

## Objective
Design and manage complete documentation systems (Wikis, FAQs, Technical Docs) to ensure information clarity and accessibility across the industrial ecosystem.

## 🛠️ Interface (v3.2.0-S)

### Input Schema (SkillInput.params)
- `scope` (string, optional): "internal" | "public" | "all". Default "all".
- `project_path` (string, optional): Absolute path to the project.

### Output Schema (SkillOutput.result)
- `hierarchy`: (object) Map of the documentation structure.
- `missing_docs`: (list) Identified gaps in the documentation.
- `health_status`: (string) "OK" | "NEEDS_UPGRADE".

### ⚖️ Mandato SI (Sistema Internacional)
Cualquier métrica de legibilidad (índice de Flesch-Kincaid, tiempo de lectura estimado) debe reportarse bajo unidades del SI (segundos, bits de información).

## Protocol
1.  **Architecture:** Map out hierarchy (Dev Docs, API Docs, User FAQ).
2.  **Navigability:** Verify cross-links between documentation modules.
3.  **Evolution:** Maintain version histories for each documentation asset.
4.  **Audit:** Periodically verify that docs reflect the current state of the code.

---
*Skill v3.2.0-S | Status: Standardized.*
