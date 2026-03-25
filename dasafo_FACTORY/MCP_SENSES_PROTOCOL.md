# 🧬 MCP Senses Protocol

> **Version:** v1.0
> **Purpose:** Define how agents use Model Context Protocol (MCP) servers as sensory organs to interact with the external world.
> **Principle:** "The factory is not blind. It sees (browser), touches (database), hears (events), and remembers (memory)."

---

## 🧠 Sensory Mapping

| Sense | MCP Server | Primary Agent | Purpose | Phase |
| :--- | :--- | :--- | :--- | :--- |
| 👁️ Eyes | Playwright / Browser Sandbox | QA_TESTER | Visual validation of UI flows | M4 (QA Gate) |
| 🖐️ Hands | Supabase | DB_MASTER | Direct database manipulation & validation | M3/M4 |
| 📡 Nerve System | Filesystem | All Agents | File I/O, task state transitions | All |
| 🧠 Memory | NotebookLM | MEMORY_OPTIMIZER | Long-term knowledge storage & retrieval | All |
| 🌐 Ears | GitHub | DEVOPS_SRE | Repository events, CI/CD triggers | M5 |
| 🔍 Intuition | Search Web | RESEARCH_AGENT | Market research, technical validation | M1 |
| ⚡ Reflexes | Run Command | Production Agents | Terminal execution, build, test | M3/M4 |

---

## 📋 Pre-Conditions

Before any agent uses an MCP sense, these conditions MUST be met:

### 1. Authorization Check

- The agent MUST be listed in `AGENT_REGISTRY.md` with the relevant MCP in its `Authorized MCPs` field.
- **Unauthorized MCP access is a CRITICAL security violation.**

### 2. Connection Validation

Before executing MCP operations:

1. Verify the MCP server is reachable (health check / ping)
2. Confirm credentials are configured (environment variables, not hardcoded)
3. Log the connection attempt in `$TARGET_PROJECT/LOGS/agents/[agent_name].log`

### 3. Scope Limitation

- **Principle of Least Privilege:** Agents ONLY access the MCP capabilities strictly required for their current task.
- Read-only agents (ARCHITECT, RESEARCH) cannot use write operations on database MCPs.
- Production agents cannot access MCPs outside their declared scope.

---

## 👁️ Eyes — Browser Visual Validation

**Agent:** QA_TESTER
**MCP:** Playwright / Browser Sandbox
**Skill:** `browser-visual-validation`

### When to Use

- **Mandatory** during Phase 4 (QA Gate) for all projects with a UI component.
- After every deployment in Phase 5 (Go-Live) as a smoke test.

### Protocol

1. Open the deployed application URL
2. Navigate critical user flows:
   - Login/Authentication
   - Dashboard/Main view
   - Core CRUD operations
   - Edge cases (empty states, error states, overflow)
3. Capture visual state at each step
4. Compare against PRP Contract `success_criteria`
5. Report results to `$TARGET_PROJECT/LOGS/agents/qa_tester.log`
6. On failure → Reject task via `autoshield-feedback-writer`

---

## 🖐️ Hands — Database Live Validation

**Agent:** DB_MASTER
**MCP:** Supabase
**Skill:** `supabase-live-validation`

### When to Use

- During Phase 3 (Execution) for schema creation and data seeding.
- **Mandatory** during Phase 4 (QA Gate) for all projects with a database.

### Protocol

1. Connect to Supabase via MCP
2. Validate actual schema matches the Architect's design in `LOCAL_KNOWLEDGE/`
3. Run integrity checks:
   - Orphaned foreign keys
   - Null constraint violations
   - Index coverage on query-heavy tables
   - Row Level Security (RLS) policies active
4. Report results to `$TARGET_PROJECT/LOGS/agents/db_master.log`
5. On critical failure → Block deployment

---

## 🧠 Memory — Knowledge Persistence

**Agent:** MEMORY_OPTIMIZER
**MCP:** NotebookLM
**Skill:** `nblm-memory-bridge`

### When to Use

- End of every Phase (M1-M5) to persist learnings.
- When context window approaches capacity.

### Protocol

1. Distill current conversation/logs into structured summaries
2. Store in NotebookLM as a source for future retrieval
3. Tag with project name, phase, and date for searchability

---

## 🌐 Ears — Repository Events

**Agent:** DEVOPS_SRE
**MCP:** GitHub
**Skill:** `github-actions-cicd-patterns`

### When to Use

- Phase 5 (Go-Live) for deployment orchestration.
- Continuous monitoring for CI/CD triggers.

### Protocol

1. Push deployment artifacts to repository
2. Monitor GitHub Actions for build status
3. On failure → Escalate to DEVOPS_SRE for diagnosis

---

## ⚠️ Error Handling

When an MCP connection fails:

1. **Log the failure** in `$TARGET_PROJECT/LOGS/agents/[agent_name].log`
2. **Retry once** after 5-second delay
3. **If retry fails:**
   - For non-critical operations → Skip and log as WARNING
   - For critical operations (QA visual validation, DB integrity) → Block the pipeline and escalate to ORCHESTRATOR
4. **Never silently swallow MCP errors** — every failure must be traceable

---

## 🔒 Security Constraints

1. **Zero Trust:** Every MCP connection is untrusted until verified
2. **No Credential Leakage:** MCP credentials MUST come from environment variables, never from source code or logs
3. **Audit Trail:** All MCP operations are logged with timestamp, agent ID, operation type, and success/failure status
4. **Blast Radius:** If an MCP server is compromised, only agents authorized for that MCP are affected. No lateral movement is possible.

---

*This protocol is enforced by the ORCHESTRATOR. Any agent bypassing MCP authorization will trigger a SECURITY_AUDITOR alert.*
