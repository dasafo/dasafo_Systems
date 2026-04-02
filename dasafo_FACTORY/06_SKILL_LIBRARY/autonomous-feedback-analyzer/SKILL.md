---
version: v4.0-S
agent: FACTORY_EVOLVER / DATA_SCIENTIST
source: https://skills.sh/phuryn/pm-skills/sentiment-analysis
---

# 🧠 Skill | Autonomous Feedback Analyzer (v4.0-S)

## Objective

Perform sentiment analysis, segment insights, and extract actionable "Golden Rules" from user feedback or factory engram logs to drive continuous systemic improvement.

## 🛠️ Interface (v4.0-S)

### Input Schema (SkillInput.params)

- `action` (enum): `analyze_file`, `analyze_text`.
- `target_project` (string, mandatory): Absolute path to the project workspace.
- `file_path` (string, optional): Path to the feedback log (Default: `LOGS/FEEDBACK-LOG.md`).
- `raw_text` (string, optional): Direct string input if analyzing isolated feedback.

### Output Schema (SkillOutput.result)

- `sentiment_score`: (string) `POSITIVE`, `NEGATIVE`, or `MIXED`.
- `key_insights`: (array) Processed bullet points of user friction or delight.
- `golden_rules`: (array) Universal rules extracted to update agent instructions.
- `report_path`: (string) Physical path to the generated JSON analysis artifact.
- `industrial_status`: (string) "SOLIDIFIED - FEEDBACK ANALYZED".

### ⚖️ SI Mandate (International System)

The weight of the analyzed data (`source_payload_bytes`) must be reported in **bytes** (B), and the computation time of the semantic analysis in **seconds** (s).

## 🛡️ Industrial Constraints (Zero-Trust & Empirical Analysis)

- **No Hallucination:** Insights MUST be directly traceable to the source text. Do not invent user complaints or feature requests.
- **Physical Sandboxing:** The analysis results MUST be saved to a physical artifact (`LOGS/FEEDBACK_ANALYSIS_*.json`) for the Orchestrator to review.
- **Schema Alignment:** Golden Rules extracted should align with the structure defined in `FEEDBACK_SCHEMA.json`.
