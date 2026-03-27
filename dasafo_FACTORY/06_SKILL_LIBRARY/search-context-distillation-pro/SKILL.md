---
version: 3.2.0-S
agent: MEMORY_OPTIMIZER
---

# 🔍 Skill | Search Context Distillation Pro

## Objective
Filter and compress bulky agent logs into dense, high-value architectural and factual summaries to keep the factory's cognitive density optimal.

## 🛠️ Interface (v3.2.0-S)

### Input Schema (SkillInput.params)
- `log_file` (string): Absolute path to the log to distill.
- `output_format` (string, optional): "markdown" | "json". Default "markdown".

### Output Schema (SkillOutput.result)
- `distilled_summary_path`: (string) Path to the compressed facts.
- `compression_ratio`: (float) Size reduction (0.0-1.0).
- `facts_extracted`: (integer) Count of actionable items found.

### ⚖️ Mandato SI (Sistema Internacional)
Toda métrica de tamaño de log antes y después de la destilación debe expresarse en bytes o megabytes (SI).

## Procedure
1.  **Clustering:** Identify semantic "clusters" of thought in raw discourse.
2.  **Extraction:** Isolate ADRs, bug fixes, environment changes, and trade-offs.
3.  **Pruning:** Remove debug/verbose lines and conversational "noise".
4.  **Verification:** Checksum validation of facts before log rotation/deletion.

---
*Skill v3.2.0-S | Status: Standardized.*
