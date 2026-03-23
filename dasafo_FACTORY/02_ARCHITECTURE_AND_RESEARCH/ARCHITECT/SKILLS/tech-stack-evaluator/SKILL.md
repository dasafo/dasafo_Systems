# Skill: Tech Stack Evaluator & TCO Analyzer
> **Source:** https://skills.sh/alirezarezvani/claude-skills/tech-stack-evaluator
> **Agent:** ARCHITECT

## Objective
Perform objective comparisons of technologies to minimize technical debt and maximize performance ROI in $TARGET_PROJECT.

## Evaluation Domains
1.  **Mantenibilidad:** ¿Qué tan fácil es encontrar soporte o agentes que entiendan esta librería?
2.  **Performance:** Latency and memory benchmarks (SI units only).
3.  **Security:** External vulnerability audit (CVSS scores).
4.  **Ecosystem:** Library size, community activity, and update frequency.

## Analysis Workflow
- **Quick Comparison:** (2 technologies) -> One-page summary.
- **Full Report:** Save in `$TARGET_PROJECT/LOCAL_KNOWLEDGE/architecture/stack_evaluation.md`.
- **Constraint:** Must reject any tech stack that lacks a clear "Dockerizable" path.
