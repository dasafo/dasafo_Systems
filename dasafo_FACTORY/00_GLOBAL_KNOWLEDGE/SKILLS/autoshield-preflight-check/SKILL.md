---
name: autoshield-preflight-check
description: Universal pre-execution skill. All agents MUST run this before starting any task to absorb relevant golden rules from FEEDBACK-LOG.
---

# 🛡️ AutoShield Preflight Check

You are the **Factory Immune System**. Before any agent executes a task, you inject the relevant intelligence from the collective memory of past mistakes.

> **Principle:** "The factory remembers every wound. No agent walks into battle blind."

## 🧠 Protocol

### Step 1: Read FEEDBACK-LOG

Parse `dasafo_FACTORY/FEEDBACK-LOG.md` and extract all YAML entries.

### Step 2: Filter by Relevance

Match entries to the current agent and task using:

1. **Agent Match:** Check if the current agent's ID appears in `affected_agents`
2. **Category Match:** Check if any entry `categories` overlap with the agent's domain:

   | Agent Domain | Relevant Categories |
   | :--- | :--- |
   | BACKEND_DEV | routing, api, database, authentication, performance |
   | FRONTEND_DEV | ui-ux, authentication, performance |
   | DB_MASTER | database, data-integrity, performance |
   | DEVOPS_SRE | deployment, infrastructure, configuration |
   | SECURITY_AUDITOR | security, authentication, configuration |
   | QA_TESTER | testing, routing, ui-ux, api |
   | ARCHITECT | routing, api, database, ui-ux, infrastructure |
   | ALL | security, configuration |

3. **Severity Priority:** Always include `critical` and `high` entries regardless of category match.

### Step 3: Inject Golden Rules

Compile the filtered golden rules into a **context injection block**:

```text
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🛡️ AUTOSHIELD PREFLIGHT ACTIVE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
The following rules MUST be respected during this execution:

[FB-0001] ⚠️ CRITICAL — "Never commit raw credentials. Use environment variables."
[FB-0002] 🔶 HIGH — "FastAPI: fixed routes MUST be declared before parameterized routes."

Total rules loaded: 2
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### Step 4: Log Execution

Record that the preflight check was executed in:

`$TARGET_PROJECT/LOGS/agents/[agent_name].log`

```text
[YYYY-MM-DD HH:MM:SS] AUTOSHIELD_PREFLIGHT: Loaded 2 rules (FB-0001, FB-0002). Agent: BACKEND_DEV.
```

## 📏 Mandatory Rules

- **Zero Skip Policy:** No agent may skip this preflight. If an agent executes a task without running the preflight check, QA_TESTER MUST reject the task.
- **Critical Rules Override:** Any `critical` severity rule applies to ALL agents, regardless of domain.
- **Cache-Safe:** If the FEEDBACK-LOG has not changed since the last preflight (check file modification timestamp), the agent may use the cached rules from the previous execution.
