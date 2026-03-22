---
description: Triggers the Orchestrator to assess project state and dispatch the next batch of tasks.
---

# Factory Orchestration Workflow

1. Identify the current active `$TARGET_PROJECT` within `PROJECTS/`.
2. Assume the role of the `@orchestrator`.
3. Check `TASKS/03_COMPLETED` for finished tasks.
4. Check `TASKS/05_REJECTED` for failed tasks that need loop remediation.
5. If the current phase is fully completed and archived, advance the project phase according to `UNIVERSAL_PIPELINE.md`.
6. Generate new task JSONs in `TASKS/01_PENDING` for the upcoming phase.
7. Print a summary of the orchestration actions taken, listing newly dispatched tasks by ID and Assigned Role.
