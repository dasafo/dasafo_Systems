---
version: 3.3.0-S
agent: RESEARCH_AGENT / ACADEMIC_STRATEGIST
source: https://skills.sh/actionbook/actionbook/active-research
---

# 📚 Skill | Active Academic Research (ArXiv)

## Objective

Design and execute high-fidelity academic research strategies. This skill allows agents to search, filter, and synthesize technical papers from ArXiv and other verified sources, transforming complex scientific data into actionable architectural insights and structured reports.

## 🛠️ Interface (v3.4.0-S)

### Input Schema (SkillInput.params)

- `action` (string, optional): "search" (default) | "digest" | "synthesize".
  - `search`: Find papers based on keywords, authors, or categories.
  - `digest`: Perform a deep read and technical breakdown of a specific paper ID.
  - `synthesize`: Combine multiple digests into a thematic research report.
- `query` (string, required for "search"): Search keywords (e.g., "Large Language Model Agents").
- `id` (string, required for "digest"): ArXiv Paper ID (e.g., "2301.12345").
- `max_results` (integer, optional): Default `10`.
- `target_project` (string, optional): Absolute path to the active project.

### Output Schema (SkillOutput.result)

- `status`: (string) "RESEARCH_SOLIDIFIED" | "DIGEST_CREATED" | "SYNTHESIS_COMPLETE"
- `results_count`: (integer) Number of items found or processed.
- `report_path`: (string, optional) Path to the physical Markdown/JSON artifact.
- `key_findings`: (list) Core technical insights extracted during the process.

### ⚖️ Mandato SI (Sistema Internacional)

Cualquier métrica técnica extraída (latencias, parámetros de modelo, consumo energético, frecuencias) debe expresarse estrictamente en el Sistema Internacional (segundos, bytes, hercios).

## 🛡️ Industrial Constraints (Zero-Trust)

- **Authenticity Only:** Must query the live ArXiv API. Hallucinating paper titles or summaries is FORBIDDEN.
- **Physical Proof:** Every research cycle must result in a physical artifact in `LOCAL_KNOWLEDGE/research/`.
- **SI Only:** Any numeric data found in papers (e.g., "50ms") must be converted to SI ("0.05s") in the final digest.

## 🧠 Active Research Workflow (v3.4.0-S)

1. **Plan Strategy:** Define clear research questions and target categories (e.g., cs.AI).
2. **Search & Filter:** Use URL-based API queries to find the most relevant and recent papers.
3. **Deep Read (Digest):** Analyze abstracts, methodologies, and conclusions for technical viability.
4. **Synthesize Findings:** Aggregate multi-paper insights into a structured report with actionable architectural recommendations.

---
**ORIGIN:** [active-research by actionbook](https://skills.sh/actionbook/actionbook/active-research)
*Skill v3.4.0-S | Status: Standardized & Industrialized (Dasafo Edition).*
