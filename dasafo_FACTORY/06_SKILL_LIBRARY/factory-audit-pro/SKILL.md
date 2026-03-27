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

## Protocol
1.  **Consistency:** Verify every agent has `IDENTITY.md`, `TOOLS.md`, and `SKILLS/`.
2.  **Drift:** Identify outdated instructions (Legacy v3.1.5).
3.  **Links:** Auto-scan for dead internal documentation links.
4.  **Report:** Generate "Industrial Health Status" every 30 days.

---
*Skill v3.2.0-S | Status: Standardized.*
