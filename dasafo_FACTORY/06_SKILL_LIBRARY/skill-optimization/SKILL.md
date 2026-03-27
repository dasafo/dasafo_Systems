---
version: 3.2.0-S
agent: SYSTEM_ARCHITECT
---

# 🛠️ Skill | Skill Optimization

## Objective
Refine and evolve `SKILL.md` instructions based on real-world iterative feedback from logs, ensuring the library remains frictionless and hallucination-free.

## 🛠️ Interface (v3.2.0-S)

### Input Schema (SkillInput.params)
- `skill_to_optimize` (string): The ID of the skill folder.
- `feedback_sample` (list, optional): Specific log entries to analyze.

### Output Schema (SkillOutput.result)
- `diff_applied`: (string) Markdown diff of the changes.
- `solidity_uplift`: (float) Estimated improvement (0.0-1.0).

### ⚖️ Mandato SI (Sistema Internacional)
Toda métrica de éxito post-optimización (reducción de errores, mejora de latencia) debe citarse bajo el estándar SI.

## Procedure
1.  **Feedback Scan:** Read `dasafo_FACTORY/FEEDBACK-LOG.md` to identify friction points.
2.  **Root Cause:** Isolate if failure was due to ambiguous instructions or missing constraints.
3.  **Drafting:** Write concise, surgical updates for the relevant `SKILL.md`.
4.  **Consistency Check:** Ensure the change aligns with `00_GLOBAL_KNOWLEDGE`.
5.  **Application:** Patch the file and increment version in YAML.

---
*Skill v3.2.0-S | Status: Standardized.*
