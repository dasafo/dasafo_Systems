---
version: v4.0-S
agent: RESEARCH_AGENT / ALL
source: custom_dasafo_factory
---

# 🔬 Skill | Research Manager (v4.0-S)

## Objective

Safely write, manage, and persist deep-research artifacts, architectural investigations, and API evaluations to the disk. Replaces the use of insecure shell `cat` commands to prevent terminal syntax errors (zsh/bash injection).

## 🛠️ Interface (v4.0-S)

### Input Schema (SkillInput.params)

- `action` (string, optional): "write_report" (default).
- `report_name` (string, required): The exact name of the markdown file (e.g., "RESEARCH_AI_MODELS.md").
- `content` (string, required): The full markdown content of the research.
- `category` (string, optional): "RESEARCH" (default) | "ARCH" | "MARKETING". Determines the physical subfolder in `DOCS/`.

### Output Schema (SkillOutput.result)

- `industrial_status`: (string) "SOLIDIFIED - RESEARCH RECORDED".
- `report_category`: (string) The folder where it was saved.
- `file_size_bytes`: (integer) Total size of the payload generated.

### ⚖️ Mandato SI (Sistema Internacional)

La ejecución devolverá el tamaño del reporte estrictamente en **Bytes (B)** y el tiempo en **Segundos (s)**.

## 🛡️ Industrial Constraints (Zero-Trust)

- **No Shell Escaping:** Agents MUST use this tool to write markdown reports. Writing via `cat <<EOF` in standard bash/zsh is strictly forbidden to prevent backtick/quote evaluation errors.
- **DAST Enforcement:** Artifacts are strictly routed to `DOCS/RESEARCH`, `DOCS/ARCH`, or `DOCS/MARKETING`.

---
*Skill v4.0-S | Status: Standardized & Industrialized.*
