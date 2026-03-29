---
version: 3.3.0-S
agent: Multiple (RESEARCH_AGENT / MEMORY_OPTIMIZER)
source: https://skills.sh/supercent-io/skills-template/deep-semantic-search
---

# 🔍 Skill | Deep Semantic Search

## Objective

Go beyond keyword search to find semantically relevant technical documentation, high-quality code patterns, and industry research.

## 🛠️ Interface (v3.3.0-S)

### Input Schema (SkillInput.params)

- `query` (string): The semantic intent (not just keywords).
- `focus` (string, optional): "technical" | "code" | "industry". Default "technical".
- `sources` (list, optional): List of sources if pre-fetched.

### Output Schema (SkillOutput.result)

- `nexus_path`: (string) Absolute path where research was appended.
- `sources_found`: (integer) Count of high-relevance sources.
- `summary`: (string) Synthesis of the findings.

### ⚖️ Mandato SI (Sistema Internacional)

Cualquier métrica de rendimiento de búsqueda (tiempo de respuesta de la API, latencia de indexación) debe reportarse en unidades del SI.

## 🛡️ Industrial Constraints (Zero-Trust)

- **Nexus Traceability:** This skill is physically required to append to `LOCAL_KNOWLEDGE/research_nexus.md`. Mocks that do not modify the physical nexus are detected as failure.
- **Physical Query Lock:** Prohibits operations if the `LOCAL_KNOWLEDGE/` directory does not exist on disk.

## 🧠 Workflow

1. **Define Concept:** Transform request into a non-keyword semantic query.
2. **Filter:** Focus exclusively on technical sources (GitHub, Medium Eng, ArXiv).
3. **Synthesize:** Append findings to the `research_nexus.md` in `$TARGET_PROJECT/LOCAL_KNOWLEDGE/`.

---
**ORIGIN:** [deep-semantic-search by supercent-io](https://skills.sh/supercent-io/skills-template/deep-semantic-search)
*Skill v3.3.0-S | Status: Standardized & Industrialized.*
