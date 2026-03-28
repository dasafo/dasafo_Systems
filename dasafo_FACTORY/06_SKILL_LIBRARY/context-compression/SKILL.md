---
version: 3.2.0-S
agent: MEMORY_OPTIMIZER
---

# 🧠 Skill | Context Compression

## Objective

Safely compress episodic logs into semantic memory without losing critical technical facts, optimizing the agent's context window.

## 🛠️ Interface (v3.2.0-S)

### Input Schema (SkillInput.params)

- `log_pattern` (string, optional): Glob pattern for logs (e.g., "*.log").
- `target_project` (string, optional): Absolute path to the project.

### Output Schema (SkillOutput.result)

- `compression_ratio`: (string) e.g., "95%".
- `facts_extracted`: (integer) Number of key facts identified.
- `index_path`: (string) Path to the `SEMANTIC_INDEX.md`.

### ⚖️ Mandato SI (Sistema Internacional)

La reducción de tamaño del contexto (en bytes o tokens) y el tiempo de extracción semántica deben reportarse en el SI.

## 🛡️ Industrial Constraints (Zero-Trust)

- **Cognitive Mandate:** Requires `OPENAI_API_KEY` or `ANTHROPIC_API_KEY`. Truncating logs without real semantic extraction is strictly FORBIDDEN to prevent data loss.
- **Physical Sweep:** Only processes existing `.log` or `.md` files in the specified paths.

## Protocol

1. **Sweep:** Scan `$TARGET_PROJECT/LOGS/agents/*.log` for physical artifacts.
2. **Extract:** Isolate facts using LLM-enabled context analysis.
3. **Format:** Combine facts into physical `SEMANTIC_INDEX.md`.
4. **Truncate:** Verified semantic extraction leads to log truncation on disk.

---
*Skill v3.2.0-S | Status: Standardized.*
