# Skill: Kanban Solidity Gate
> **Agent:** ORCHESTRATOR
> **Version:** 3.1.2-Solidity

## Objective
Programmatically enforce the "Zero-Pending Rule" for industrial project transitions. This skill prevents an agent from declaring a phase COMPLETED if there are physical task files or markdown markers that remain unaddressed.

## Logic
1.  **Directory Check**: Scan `TASKS/01_PENDING` and `TASKS/02_IN_PROGRESS` for non-hidden files.
2.  **Markdown Check**: Parse `task.md` (or the internal `task.md` artifact) for `[ ]` or `[/]` markers.
3.  **Phase Matching**: Verify that all deliverables for the current phase (per `PROJECT_STATE.json`) are finalized.

## Parameters
- `target_project`: (Optional) Path to the project root.
- `proposed_phase`: (Required) The phase the project is attempting to enter.

## Output
- `success: true`: Gate cleared.
- `success: false`: Logic blocked. Detailed list of pending tasks provided in the error field.
