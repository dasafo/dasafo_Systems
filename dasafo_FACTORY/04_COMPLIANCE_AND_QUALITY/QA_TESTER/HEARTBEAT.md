# ⏱️ QA Tester | Heartbeat
>
> **Function:** Continuous Quality Surveillance.

## 🔄 Routine
1. **Target:** Resolve `$TARGET_PROJECT`.
2. **Scan:** Look for new artifacts in `$TARGET_PROJECT/.artifacts/` or `$TARGET_PROJECT/DOCS/`.
3. **Verify:** Run `autoshield-preflight-check` to ensure no regression.
4. **Audit:** Execute `requirements-validation-audit` to confirm PRP alignment.
5. **Feed:** If a deviation is found, trigger `autoshield-feedback-writer`.

---
*Heartbeat v2.1 | Status: Solidified.*
