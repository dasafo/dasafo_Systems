---
version: 3.2.0-S
agent: SYSTEM_ARCHITECT
---

# ⚙️ Skill | System Optimizer

## Objective
Detect bottlenecks, monitor orchestration latency, and optimize factory engine performance by streamlining agentic task transitions and resource usage.

## 🛠️ Interface (v3.2.0-S)

### Input Schema (SkillInput.params)
- `analysis_depth` (string, optional): "light" | "deep". Default "light".
- `budget_threshold_s` (integer, optional): Threshold for "bottleneck" flagging.

### Output Schema (SkillOutput.result)
- `bottlenecks_flagged`: (list) Agents or tasks with high latency.
- `token_efficiency_gain`: (float) Estimated gain from model swap.
- `optimization_report_path`: (string) Absolute path to final report.

### ⚖️ Mandato SI (Sistema Internacional)
Toda métrica de rendimiento (latencia en segundos, consumo en tokens/bytes) debe reportarse bajo el estándar SI.

## Procedure
1.  **Latency Scan:** Monitor orchestration logs for redundant task transitions or delays.
2.  **Efficiency Audit:** Estimate token consumption and propose faster/surgical model alternatives.
3.  **Redundancy Pruning:** Identify and remove duplicated architecture checks or redundant safety polls.
4.  **Reporting:** Generate a "Streamlined Workflow" report in `$TARGET_PROJECT/ANALYSIS/optimization/`.

---
*Skill v3.2.0-S | Status: Standardized.*
