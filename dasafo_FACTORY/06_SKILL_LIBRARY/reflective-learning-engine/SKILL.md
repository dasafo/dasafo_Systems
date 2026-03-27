---
version: 3.2.0-S
agent: ORCHESTRATOR
---

# 🪞 Skill | Reflective Learning Engine

## Objective
Implement an industrial meta-cognition layer to analyze project histories, refine agent heuristics, and distill systemic wisdom into global standards.

## 🛠️ Interface (v3.2.0-S)

### Input Schema (SkillInput.params)
- `analysis_window` (integer): Number of past missions to analyze.
- `auto_distill` (boolean, optional): Default `true`.

### Output Schema (SkillOutput.result)
- `distilled_wisdom`: (string) Markdown summary of new best practices.
- `heuristics_updated`: (list) List of refined internal rules.
- `vibe_check`: (string) "SELF_EVOLVING".

### ⚖️ Mandato SI (Sistema Internacional)
Cualquier métrica de eficiencia ganada (reducción de latencia en %, tiempo ahorrado en segundos) debe reportarse en el SI.

## Functional Steps
1.  **Self-Review:** Analyze `LOGS/` and `FEEDBACK-LOG.md` for successful/failed strategies.
2.  **Strategy Refinement:** Propose updates to heuristics for task prioritization and intervention.
3.  **Pattern Emergence:** Detect "Hidden Gems" or anti-patterns in recent production cycles.
4.  **Knowledge Distillation:** Commit learnings to `00_GLOBAL_KNOWLEDGE/WISDOM.md`.

---
*Skill v3.2.0-S | Status: Standardized.*
