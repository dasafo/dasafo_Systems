---
version: 3.4.0-S
agent: FACTORY_EVOLVER / PRODUCT_ANALYST
source: https://skills.sh/eddiebe147/claude-settings/feedback-analyzer
---

# 🧠 Skill | Autonomous Feedback Analyzer

## Objective

Proactively automate the collection, categorization, and deep analysis of user and system feedback. This skill identifies emotional context, urgency, and recurring patterns to drive the evolution of the agentic factory, ensuring continuous performance optimization and user satisfaction.

## 🛠️ Interface (v3.4.0-S)

### Input Schema (SkillInput.params)

- `action` (string, optional): "analyze" (default) | "score_urgency" | "synthesize".
  - `analyze`: Classify feedback into themes and sentiment categories.
  - `score_urgency`: Calculate priority based on risk, frequency, and customer tier.
  - `synthesize`: Generate a structured "Insight Report" with actionable recommendations.
- `feedback_data` (list, required): List of raw feedback objects or text strings.
- `target_project` (string, optional): Absolute path for saving analysis reports.

### Output Schema (SkillOutput.result)

- `status`: (string) "ANALYSIS_COMPLETE" | "INSIGHTS_GENERATED"
- `report_path`: (string, optional) Path to the physical Markdown report.
- `sentiment_distribution`: (dict) Mapping of sentiment levels (v_neg, neg, neutral, pos, v_pos).
- `priority_alerts`: (list) High-urgency issues that triggered immediate flags.
- `si_metrics`: (dict) Performance metrics (e.g., `avg_response_time_seconds`).

### ⚖️ Mandato SI (Sistema Internacional)

Cualquier métrica técnica analizada (tiempos medios de respuesta, latencias de procesamiento de tickets, tamaños de logs) debe expresarse estrictamente en el SI (segundos, bytes).

## 🛡️ Industrial Constraints (Zero-Trust)

- **Evidence-Based:** Insights must be backed by representative quotes or physical log data. Hallucinated feedback patterns are FORBIDDEN.
- **Physical Archiving:** Analysis results must be physically saved to `DOCS/feedback/` or `LOCAL_KNOWLEDGE/evolution/`.
- **SI Only:** Ensure all time-to-address estimates follow the SI (e.g., using prefix `s`).

## 🧠 Analysis Frameworks (v3.4.0-S)

1. **Sentiment & Urgency:** Map emotional indicators to Action Levels (Urgent Escalation → Sprint Address → Standard Review).
2. **Pattern Recognition:** Use qualitative analysis to discover pain points and unmet needs.
3. **Insight Synthesis:** Structure findings using the (FINDING → EVIDENCE → IMPACT → RECOMMENDATION) template.
4. **Root Cause Analysis (RCA):** Distinguish between symptoms and causes by mapping feedback to user journey stages.

---
**ORIGIN:** [feedback-analyzer by eddiebe147](https://skills.sh/eddiebe147/claude-settings/feedback-analyzer)
*Skill v3.4.0-S | Status: Standardized & Industrialized (Dasafo Edition).*
