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

## Protocol
1.  **Normalize:** Identify the ArXiv ID and point to the metadata API.
2.  **Fetch Metadata:** Download entry details (title, summary, authors).
3.  **Summary Generation:** Produce a technical breakdown in `$TARGET_PROJECT/LOCAL_KNOWLEDGE/research/PAPER_SUMMARY_{ID}.md`.
4.  **Output Focus:** Focus on formulas, pseudocode, and limitations.

---
*Skill v3.2.0-S | Status: Standardized.*
