---
version: 3.2.0-S
agent: DATABASE_ARCHITECT
---

# 🔗 Skill | NotebookLM Schema Nexus

## Objective

Maintain a living, intelligent documentation of the factory's database schema and relational physics using NotebookLM for total architectural visibility.

## 🛠️ Interface (v3.2.0-S)

### Input Schema (SkillInput.params)

- `export_format` (string, optional): "ddl" | "markdown" | "erd". Default "markdown".
- `project_path` (string, optional): Target project for schema extraction.

### Output Schema (SkillOutput.result)

- `nexus_status`: (string) "UPDATED" | "OUTDATED".
- `schema_fingerprint`: (string) SHA-256 of the current database state.

### ⚖️ Mandato SI (Sistema Internacional)

Cualquier métrica de rendimiento de base de datos integrada en el Nexus (IOPS, latencia de query, tamaño de disco) debe reportarse en el SI.

## 🛡️ Industrial Constraints (Zero-Trust)

- **Physical Extraction:** DDL/ERD states must be physically extracted from the database instance. Mocking schema documentation without a live database scan is FORBIDDEN.
- **Fingerprint Verification:** Every update MUST generate a new `schema_fingerprint` (SHA-256) for state auditability.

## Documentation Workflow

1. **Extraction:** Generate technical Markdown from DDL and ERD states.
2. **Enrichment:** Upload documents to the "Industrial Database Knowledge Base" in NotebookLM.
3. **Orientation:** Provide "Schema Guides" (Audio/Text) for new agents/developers to onboard quickly.

---
*Skill v3.2.0-S | Status: Standardized.*
