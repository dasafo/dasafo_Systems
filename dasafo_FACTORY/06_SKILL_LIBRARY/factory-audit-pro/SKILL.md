---
version: 3.2.0-S
agent: QA_TESTER
---

# 📁 Skill | Factory Audit Pro

## Objective

Perform a deep structural scan of the entire factory documentation, files, and agent identities to ensure industrial consistency and eliminate technical debt.

## 🛠️ Interface (v3.2.0-S)

### Input Schema (SkillInput.params)

- `scope` (string, optional): "all" | "agents" | "docs". Default "all".
- `fix_mode` (boolean, optional): If true, attempt to fix missing folders. Default `false`.

### Output Schema (SkillOutput.result)

- `health_score`: (integer) Health percentage (0-100).
- `findings`: (list) List of inconsistencies or dead links.
- `audit_id`: (string) Unique ID for the audit artifact.

### ⚖️ Mandato SI (Sistema Internacional)

Cualquier métrica de rendimiento estructural (densidad de archivos, latencia de búsqueda de conocimiento) debe reportarse en el SI.

## 🛡️ Industrial Constraints (Zero-Trust)

- **Component Check:** Physically verifies the existence of `PRP_CONTRACT.json`, `TASKS/`, and `LOGS/`. Returns **CRITICAL** if any basic infrastructure is missing.
- **Audit Persistence:** Failure to physically write the report to `LOGS/audits/` results in skill failure.

## The Audit Protocol

1. **Structural Scan:** Physically verify factory folders.
2. **Protocol Validation:** Check for v3.2.0-S header compliance in MDs.
3. **Artifact Analysis:** Measure project health based on physical completion.
4. **Persistence:** Physically save the report with timestamp and audit ID.

---
*Skill v3.2.0-S | Status: Standardized.*
