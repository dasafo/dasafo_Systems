---
version: v5.0-MCP (Native)
agent_authorization: [ORCHESTRATOR, ARCHITECT, FACTORY_EVOLVER]
production_category: REVIEW
source: internal/factory-doctor
protocol: Forensic-DAST / Solidification
---

# 🚑 Skill | factory-doctor

## Objective

Perform a forensic audit of the file system to heal corrupt project states. Regenerates `registry.json` and `PROJECT_STATE.json` based strictly on physical evidence.

## 🛠️ Interface (v5.0-MCP Native)

**MANDATORY:** Use typed arguments. The `params_json` structure is **DEPRECATED**.

### Typed Parameters

- `agent` (string): Your Agent ID authorized in AGENT_SKILL_MAPPING.md.
- `target_project` (string): Absolute path to the project to heal.
- `sync_neo4j` (boolean): (Optional) Sync the healed state to the Knowledge Graph (Default: true).
- `isolate` (boolean): (Optional) Execution in Clean Session (Default: false).

## 🛡️ Industrial Constraints

- **Disk Supremacy:** Physical files in task folders OVERWRITE any previous registry data.
- **SI Standards:** All timings in **Seconds (s)** and file sizes in **Bytes (B)**.
- **Bypass Mandate:** This tool is authorized to bypass phase locks to perform emergency recovery.

---
*Standard v5.0-MCP | Dasafo Factory Core DAST.*
