---
version: 3.2.0-S
agent: RESEARCH_AGENT
---

# 🕵️ Skill | Continuous Research

## Objective
Orchestrate multi-source technical research using documentation, web search, and scraping tools to synthesize findings.

## 🛠️ Interface (v3.2.0-S)

### Input Schema (SkillInput.params)
- `query` (string): The research topic or question.
- `depth` (string, optional): "fast" | "deep". Default "fast".
- `sources` (list, optional): Preferred search domains/sources.

### Output Schema (SkillOutput.result)
- `summary`: (string) Coherent markdown summary of findings.
- `recommendations`: (list) Actionable implementation steps.
- `file_path`: (string) Absolute path where research was saved.

### ⚖️ Mandato SI (Sistema Internacional)

Cualquier dato cuantitativo encontrado en la investigación (benchmarks, latencias, anchos de banda) debe verificarse y reportarse bajo el Sistema Internacional de Unidades.

## 🛡️ Industrial Constraints (Zero-Trust)

- **Research Engine Lock:** Requires `SERPAPI_API_KEY` or `TAVILY_API_KEY`. Mocking research results from internal training data is FORBIDDEN.
- **Persistence:** Results must be physically persisted in `LOCAL_KNOWLEDGE/research/`.

## 🛠️ Research Process

1. **Identify Channels:** Documentation, Best Practices, Web Scraping via physical APIs.
2. **Execution:** Focus on patterns and quantitative physical metrics.
3. **Synthesis:** Physically write Markdown findings to `$TARGET_PROJECT/LOCAL_KNOWLEDGE/`.

---
*Skill v3.2.0-S | Status: Standardized.*
