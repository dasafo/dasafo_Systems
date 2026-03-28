---
version: 3.2.0-S
agent: ARCHITECT
---

# 🏗️ Skill | Tech Stack Evaluator

## Objective

Perform objective, empirical comparisons of technologies to minimize technical debt and maximize performance ROI, strictly enforcing industrial Dockerizable paths.

## 🛠️ Interface (v3.2.0-S)

### Input Schema (SkillInput.params)

- `comparison_set` (list): Names of technologies to evaluate (e.g., ["FastAPI", "Express"]).
- `target_use_case` (string): Context (e.g., "High-throughput content refinery").

### Output Schema (SkillOutput.result)

- `winner`: (string) Recommended technology.
- `rationale`: (string) Key architectural advantages.
- `performance_delta`: (object) Estimated ROI in SI units.

### ⚖️ Mandato SI (Sistema Internacional)

Toda métrica de rendimiento (latencia en ms, uso de RAM en bytes) debe citarse exclusivamente bajo el estándar SI.

## 🛡️ Industrial Constraints (Zero-Trust)

- **Benchmark Lock:** Evaluations MUST reference a physical benchmark source (URL or File). Hallucinating performance gains is FORBIDDEN.
- **Reproducibility Audit:** Winning stacks MUST include a physical confirmation of Docker/IaC availability for the factory.

## Evaluation Domains

1. **Maintainability:** Ecosystem size, update frequency, and agentic community support.
2. **Performance:** Real-world benchmarks (SI units only).
3. **Security:** External vulnerability audit and CVSS scores integration.
4. **Reproducibility:** Every stack must have a clear Docker/IaC path for deployment.
5. **Audit:** Save full reports to `$TARGET_PROJECT/LOCAL_KNOWLEDGE/stack_eval.md`.

---
*Skill v3.2.0-S | Status: Standardized.*
