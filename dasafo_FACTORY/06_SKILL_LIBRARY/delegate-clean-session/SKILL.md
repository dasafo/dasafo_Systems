---
version: v4.0-S
agent: ORCHESTRATOR
description: Delegate execution to a sub-agent in a context-isolated session.
---

# 🚀 Skill | Delegate Clean Session (v4.0-S)

## Objective

Execute a technical task by spawning a specialized sub-agent (FRONTEND, BACKEND, QA, etc.) in a "Clean Slate" context. This prevents the Orchestrator's high-level strategic memory from being contaminated by low-level implementation details (Token Decay prevention).

## 🛠️ Interface (v4.0-S)

### Input Schema (SkillInput.params)

- `agent_type` (enum): `FRONTEND_DEV`, `BACKEND_DEV`, `QA_TESTER`, `RESEARCH_AGENT`.
- `spec_path` (string, mandatory): Path to the `SPEC_LITE.json` defining the task.
- `context_pointers` (array, optional): List of specific files the sub-agent is allowed to read.
- `timeout` (integer): Seconds before the session is forced to close.

### Output Schema (SkillOutput.result)

- `task_status`: `COMPLETED`, `FAILED`, `BLOCKED`.
- `outcome_report`: (string) Summary of the work done and evidence found.
- `artifacts_produced`: (array) Paths to new or modified files.
- `token_usage_estimated`: (integer) Total tokens consumed by the clean session.

## 🛡️ Industrial Constraints (SSD)

- **Context Wall:** The sub-agent must NOT have access to the Orchestrator's conversation history beyond the provided `SPEC_LITE`.
- **Artifact Physicality:** No task is "Completed" without a physical change on disk or a new JSON artifact.
- **Blind Return:** The Orchestrator reads only the `outcome_report` and `artifacts_produced`, never the raw logs of the sub-session.
