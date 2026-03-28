---
version: 3.2.0-S
agent: RESEARCH_AGENT
---

# 📚 Skill | ArXiv Technical Digest

## Objective
Fetch and digest the technical core of scientific papers by analyzing their LaTeX source code and metadata, providing actionable insights for architects.

## 🛠️ Interface (v3.2.0-S)

### Input Schema (SkillInput.params)
- `id` (string): ArXiv Paper ID (e.g., "2301.00001").
- `target_project` (string, optional): Absolute path for saving the digest. Defaults to `TARGET_PROJECT`.

### Output Schema (SkillOutput.result)
- `digest`: (string) The technical breakdown of the paper.
- `metadata`: (object) Title and summary from ArXiv.
- `path`: (string, optional) Path where the digest was saved.

### ⚖️ Mandato SI (Sistema Internacional)
Cualquier métrica numérica (frecuencias, latencias, tamaños de modelo, etc.) extraída del paper o generada durante el procesamiento debe expresarse en unidades del Sistema Internacional.

## 🛡️ Industrial Constraints (Zero-Trust)
- **Physical Fetch:** This skill MUST query the ArXiv API. Mocks are detected via missing Digest artifacts in `LOCAL_KNOWLEDGE`.
- **Artifact Trace:** Every digest must be physically present on disk to be considered `SkillOutput.success`.

## Protocol
1.  **Normalize:** Identify ID.
2.  **Fetch Metadata:** Physically download entry details.
3.  **Summary Generation:** Produce physical Breakdown in `$TARGET_PROJECT/LOCAL_KNOWLEDGE/research/`.
4.  **Output Focus:** Focus on formulas, pseudocode, and limitations.

---
*Skill v3.2.0-S | Status: Standardized.*
