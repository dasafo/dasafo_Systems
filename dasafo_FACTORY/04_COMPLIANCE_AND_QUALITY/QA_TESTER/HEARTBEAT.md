# dasafo_System | QA Heartbeat
>
> **Function:** Automated Task Monitoring.

## ⏱️ Pulse Frequency

- **Check Interval:** Every 30 minutes.
- **Target Directory:** `TASKS/03_COMPLETED/`

## 💓 Routine

1. **Scan:** Look for new `.json` tasks in the COMPLETED folder.
2. **Claim:** Move the task to `TASKS/02_IN_PROGRESS/` and assign `QA_TESTER` as the active agent.
3. **Execute:** Run the corresponding `.skill` for the task type.
4. **Report:** If it fails, move back to `TASKS/01_PENDING` with an error log. If it passes, move to `TASKS/04_ARCHIVE`.
