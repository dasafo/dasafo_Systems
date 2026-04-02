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
- `ltp_injected_rules`: (integer) Number of Golden Rules extracted from Neo4j and injected into the Spec.

## 🛡️ Industrial Constraints (SSD)

- **Context Wall:** The sub-agent must NOT have access to the Orchestrator's conversation history beyond the provided `SPEC_LITE`.
- **Auto-Start Protocol (DAST):** The skill automatically moves the physical JSON artifact from `01_PENDING` to `02_IN_PROGRESS` prior to delegation.
- **JIT LTP Injection:** The skill actively queries the Neo4j Knowledge Graph for past `CulturalViolations` and rewrites the `SPEC_LITE.json` constraints to immunize the sub-agent.
- **Artifact Physicality:** No task is "Completed" without a physical change on disk.
