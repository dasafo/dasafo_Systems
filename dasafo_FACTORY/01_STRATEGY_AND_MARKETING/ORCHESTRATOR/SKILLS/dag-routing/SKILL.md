---
description: How to decompose a user prompt into a Directed Acyclic Graph (DAG) of parallel and sequential tasks.
---

# 🧠 SKILL: DAG Routing & Task Decomposition

1. **Ingest the `PROJECT_STATE.json` intent.**
2. **Identify Parallel vs. Sequential Tasks.**
   - *Example:* If the user wants a "Login Page connected to a Postgres DB".
   - *Sequential Phase 1:* `ARCHITECT` designs the user schema (Task A).
   - *Parallel Phase 2:* `BACKEND_DEV` builds the FastAPI endpoint (Task B) AND `FRONTEND_DEV` builds the React UI (Task C). Both depend on Task A.
3. **Format Output.** Write strict JSON files into `01_PENDING/`:
   ```json
   {
     "task_id": "T-1001",
     "assigned_to": "BACKEND_DEV",
     "depends_on": ["T-1000_ARCHITECT_SCHEMA"],
     "instructions": "Build FastAPI login endpoint."
   }
   ```
4. **Publish Event.** Ensure the assigned agent's queue is updated.
