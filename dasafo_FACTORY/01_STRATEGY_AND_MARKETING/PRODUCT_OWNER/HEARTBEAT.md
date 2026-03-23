# dasafo_System | Product Owner's Heartbeat
> 
> **Function:** Master Trigger & Vision Alignment.

## ⏱️ Pulse Frequency

- **Check Interval:** Every 1 hour (or upon external trigger).
- **Target:** `$TARGET_PROJECT/LOCAL_KNOWLEDGE/` and `$TARGET_PROJECT/PROJECT_STATE.json`.

## 💓 Routine

1. **Scan:** Check for new project briefs or client preferences in the knowledge base.
2. **Synchronize:** Update `PROJECT_STATE.json` with the latest mission objectives and determine the **RA Level** (RA0-RA5) of requirements.
3. **Decompose:** Break down validated goals (RA5) into technical tasks using the `TSK_` schema.
4. **Pending:** Place new tasks in `TASKS/01_PENDING/` for the ARCHITECT to refine or workers to claim.
5. **Review:** Inspect `TASKS/03_COMPLETED/` to ensure the final output matches the "Definition of Done".
