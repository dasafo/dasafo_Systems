---
version: v4.0-S
agent: MARKETING_GROWTH / RESEARCH_AGENT
source: https://skills.sh/apify/agent-skills/apify-trend-analysis
---

# 📈 Skill | Apify Trend Analysis

## Objective

Identify and analyze market trends, consumer behavior, and niche opportunities across global platforms (Google Trends, Instagram, TikTok, YouTube, etc.) using Apify Actors. This skill provides a structured framework for data-driven strategic decision-making.

## 🛠️ Interface (v4.0-S)

### Input Schema (SkillInput.params)

- `actor` (string): The Apify Actor ID to execute (e.g., `apify/google-trends-scraper`).
- `input_data` (object): The specific parameters for the selected actor (as per its schema).
- `format` (string, optional): Output format. "json" (default) or "csv".
- `target_project` (string, optional): Absolute path to the active project.

### Output Schema (SkillOutput.result)

- `status`: (string) "TREND_CAPTURED" | "ANALYSIS_FAILED"
- `summary`:
  - `actor_used`: (string) ID of the actor executed.
  - `data_points_count`: (integer) Total number of items captured.
  - `file_path`: (string) Path to the physical artifact.
- `insights`: (string) Automated summary of key trend patterns identified in the data.
- `recommendations`: (list) Actionable next steps based on trend analysis.

### ⚖️ Mandato SI (Sistema Internacional)

Cualquier métrica temporal (intervalos, crecimiento) o de volumen de datos debe expresarse estrictamente en unidades del Sistema Internacional (segundos, bytes).

## 🛡️ Industrial Constraints (Zero-Trust)

- **Authenticity Only:** Requires a valid `APIFY_API_TOKEN`. Generating "hallucinated trends" without a live run is FORBIDDEN.
- **Physical Proof:** Raw data must be persisted to `LOCAL_KNOWLEDGE/trends/` before success is returned.
- **Schema-Driven:** Before execution, agents are encouraged to fetch the actor's schema for parameter accuracy.

## 🧠 Strategic Workflow (v4.0-S)

1. **Identify Trend Type:** Select a specialized actor (Google Trends, Instagram Search, etc.).
2. **Fetch Schema:** Retrieve the actor's input requirements dynamically to ensure valid parameters.
3. **Execution:** Run the analysis script with the defined input and selected format.
4. **Summarize Findings:** Report the number of results, key patterns, and content opportunities.

---
**ORIGIN:** [apify-trend-analysis by apify](https://skills.sh/apify/agent-skills/apify-trend-analysis)
*Skill v4.0-S | Status: Standardized & Industrialized (Dasafo Edition).*
