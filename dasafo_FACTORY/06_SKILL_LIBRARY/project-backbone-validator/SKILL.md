---
name: project-backbone-validator
description: Inspects the physical filesystem to ensure framework scaffolding (e.g., Next.js layout, FastAPI main) exists before allowing the Orchestrator to delegate tasks. Use when validating a project's structural readiness.
---

# 🏗️ Skill | Project Backbone Validator (v4.0-MCP)

## Objective

Act as the "Inspector de Obra" for the dasafo_Factory. Ensure that the necessary framework scaffolding (the "skeleton") physically exists on disk before any atomic implementation agent (`BACKEND_DEV`, `FRONTEND_DEV`) is dispatched by the Orchestrator.

## 🛠️ Interface (v4.0-MCP)

### Input Schema (SkillInput.params)

- `target_project` (string, mandatory): Absolute or relative path to the project root.
- `framework` (string, mandatory): The core stack expected (e.g., `nextjs`, `fastapi`).

### Output Schema (SkillOutput.result)

- `scaffolding_ready`: (boolean) True if the structural files are verified on disk.
- `missing_bones`: (list) Files required by the framework that are missing.
- `validation_time_s`: (float) Execution time in seconds.

## 🧠 Industrial Constraints & Best Practices

- **Validate Physical Truth (DAST):** Always inspect the file system directly to confirm existence rather than relying on assumed context.
- **Instruct Positively:** When scaffolding is missing, provide clear, actionable feedback to the Orchestrator to generate the missing files first (e.g., "Trigger framework-bootstrapper to create layout.tsx").
- **Enforce SI Units:** Report all performance and execution metrics strictly in seconds (s).

## 🚀 Execution Guide

1. Receive the target project path and the framework type.
2. Check for framework-specific foundational files (e.g., `WORKSPACE/frontend/app/layout.tsx` for Next.js, `WORKSPACE/backend/main.py` for FastAPI).
3. Provide the validation payload detailing readiness and missing dependencies.
