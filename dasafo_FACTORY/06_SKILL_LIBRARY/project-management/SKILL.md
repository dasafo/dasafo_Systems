---
version: 3.3.1-S
agent: PRODUCT_OWNER
source: https://skills.sh/googleworkspace/cli/persona-project-manager
---

# 📅 Skill | Project Management (v3.3.1-S)

## Objective

Coordinate industrial projects through task tracking, resource orchestration, and stakeholder communication. This skill integrates with the project's physical artifacts and provides workflows for standup reports, weekly digests, and automated status logging.

## 🛠️ Interface (v3.3.1-S)

### Input Schema (SkillInput.params)

- `action` (enum): `standup_report`, `weekly_digest`, `log_status`, `announce_artifact`.
- `target_project` (string, mandatory): Absolute path to the project workspace.
- `report_data` (object, optional): Data for the report or log entry.
- `stakeholders` (array, optional): List of stakeholder IDs or emails to notify.

### Output Schema (SkillOutput.result)

- `status`: (string) "LOGGED" | "REPORT_GENERATED"
- `artifact_path`: (string, optional) Path to the generated report in `DOCS/MANAGEMENT/`.
- `next_steps`: (list) Priority tasks inferred from the state.
- `industrial_status`: (string) "SOLIDIFIED - PROJECT STATE SYNCED"

### ⚖️ Mandato SI (Sistema Internacional)

Cualquier métrica de progreso, tiempo de ejecución de tareas o hitos temporales debe expresarse estrictamente en **segundos** (s). Los tamaños de archivos o cuotas de recursos se expresan en **bytes**.

## 🛡️ Industrial Constraints (Zero-Trust)

- **Physical Grounding:** Status reports MUST be derived from `TASKS/registry.json` and `PROJECT_STATE.json`. Do not guess progress.
- **Audit Trail:** Every status update or announcement must leave a physical trace in the project's `DOCS/MANAGEMENT/` folder.
- **Stakeholder Integrity:** All communications must follow the tone and safety guardrails defined in the project's metadata.
- **Dry-Run Protocol:** For any external tool invocation (Drive, Sheets), a dry-run is required unless explicitly skipped.

## 🧠 Coordination Workflow (v3.3.1-S)

1. **State Analysis:** Parse the physical `registry.json` to identify blockers and progress ratios.
2. **Task Logging:** Append updates to the project's status log (physical file or Google Sheet).
3. **Artifact Sharing:** Upload key architectural or logic deliverables to the project's centralized storage (Drive).
4. **Announcement:** Notify stakeholders of significant milestones or blockers via automated digests.
5. **Standup:** Generate the daily "Stark-Standup" based on the last 24h of task completions.

---
**ORIGIN:** [persona-project-manager by googleworkspace](https://skills.sh/googleworkspace/cli/persona-project-manager)
*Skill v3.3.1-S | Status: Standardized & Industrialized (Dasafo Edition).*
