---
version: v4.0-S
agent: FACTORY_EVOLVER
source: https://skills.sh/github/awesome-copilot/refactor
---

# 🧬 Skill | Skill Refactor Pro (v4.0-S)

## Objective

Provide surgical code refactoring to improve maintainability, structure, and readability without changing external behavior. Refactoring is treated as a gradual evolution, heavily relying on existing tests before any mutation occurs.

## 🛠️ Interface (v4.0-S)

### Input Schema (SkillInput.params)

- `action` (enum): `analyze_smells`, `apply_refactor`.
- `target_project` (string, mandatory): Absolute path to the project workspace.
- `file_path` (string, mandatory): Specific file within `WORKSPACE/` to analyze or refactor.
- `target_smell` (string, optional): Specific smell to target (e.g., `nested_conditionals`, `magic_numbers`).

### Output Schema (SkillOutput.result)

- `refactor_status`: (string) `ANALYZED` or `REFACTORED`.
- `identified_smells`: (array) List of detected code smells and their line numbers.
- `artifacts_produced`: (array) Paths to the generated `.refactored` physical files.
- `industrial_status`: (string) "SOLIDIFIED - CODE REFACTORED".

### ⚖️ Mandato SI (Sistema Internacional)

Cualquier métrica de rendimiento comparativo (antes/después de la refactorización) debe expresarse en **segundos** (s) para el tiempo de ejecución y en **bytes** (B) para el tamaño del archivo o consumo de memoria.

## 🛡️ Industrial Constraints (Zero-Trust & Safe Refactoring)

- **Test-Driven Mutation:** Refactoring is FORBIDDEN on files that lack corresponding tests (`test_*.py` or `*.spec.ts`). Without tests, you're not refactoring, you're editing.
- **Single Responsibility:** Apply only one type of refactor pattern (e.g., Extract Method, Introduce Strategy Pattern) per execution to avoid regression.
- **Physical Sandboxing:** The refactored code MUST be output to a new file appended with `_refactored` (e.g., `main_refactored.py`). The Orchestrator or QA_TESTER must approve it before it replaces the original.
- **No Behavior Change:** The logic must yield the exact same output.
