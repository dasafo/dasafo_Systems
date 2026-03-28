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

## 🛡️ Industrial Constraints (Zero-Trust)

- **Physical Sitemap:** Operates by physically scanning the repository for mandatory files (`README.md`, `ARCHITECTURE.md`). Mocks are impossible as the skill reports "NEEDS_DOCUMENTATION" if artifacts are missing.
- **Strict Pathing:** Validates directory hierarchy against the project's physical state.

## Protocol

1. **Mapping:** Physically scan for required standard files.
2. **Integrity Check:** Verify headers and cross-references in physical MDs.
3. **GAP Analysis:** Identify missing documentation components.
4. **Structural Report:** List necessary artifacts to meet v3.2.0-S compliance.

---
*Skill v3.2.0-S | Status: Standardized.*
