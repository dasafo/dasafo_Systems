# 📡 Native MCP Protocol | Mandate v5.0.4

> [ ⬆️ Up: [[MOC_GLOBAL]] | 📂 Index: [[MOC_GLOBAL]] ]

> **Standard:** v5.0-MCP "Industrial Core"
> **Ratified:** 2026-04-15

## 🎯 Purpose

This document defines the **mandatory communication protocol** for all agents within the dasafo_FACTORY. It supersedes any previous bash/terminal execution patterns.

## 🛡️ The MCP Mandate (Article III.1 of the Constitution)

All factory operations MUST be executed via **native MCP tool invocations**. Direct terminal commands (`bash`, `sh`, `python`) are **strictly prohibited** for industrial operations.

### How Agents Communicate

```
Agent → MCP Tool (by name) → Aduana Universal (validation) → Skill Logic → DAST Artifacts
```

1. **Agent** receives a `SPEC_LITE.json` task from the Orchestrator.
2. **Agent** invokes the authorized MCP tool **by name** (e.g., `async-fastapi-logic`, `frontend-ui-designer`).
3. **Aduana Universal** intercepts the call, runs loop detection (Redis) and phase validation (DAST).
4. **Skill Logic** executes and produces physical artifacts on disk.
5. **Agent** reports an Outcome Report (Zero Fluff: `status`, `artifacts`, `summary`).

### Prohibited Patterns

| Pattern | Status | Reason |
|---------|--------|--------|
| `subprocess.run("bash ...")` | 🔴 BLOCKED | Violates Zero-Trust |
| `os.system("pip install ...")` | 🔴 BLOCKED | Uncontrolled side effect |
| `exec(user_input)` | 🔴 BLOCKED | Injection vector |
| `mcp_tool("async-fastapi-logic", ...)` | 🟢 ALLOWED | Native MCP invocation |

## ⚡ Aduana Universal (The Customs Gate)

Every MCP tool invocation passes through the `aduana_universal` decorator in `mcp_app.py`:

1. **Loop Detection:** Redis-backed counter with disk fallback circuit breaker.
2. **Pre-Flight DAST Sync:** Rebuilds `registry.json` from physical task folders.
3. **INFRA Injection:** Loads `INFRA/.env` for secure credential access.
4. **Phase Validation:** Delegates to `session_hook.verify_project_state()`.
5. **Execution:** Runs the skill's pure logic function.
6. **Anti-Fatigue Reset:** Clears loop counter on successful completion.

## 🔑 Security Layer (v5.0.4 Patch)

- **Zero hardcoded credentials:** All secrets sourced from `INFRA/.env` via `dotenv`.
- **BYPASS_SKILLS restricted:** Only pure diagnostic tools bypass phase validation.
- **AgentShield Protocol:** Destructive commands require `hallucination-guardrail` or Human Approval.
- **Atomic writes:** `registry.json` uses `tempfile + os.replace` to prevent race conditions.

---
### 🧬 Related Engrams
- [[00_CORE_CONSTITUTION]]
- [[../06_SKILL_LIBRARY/MOC_SKILL_LIBRARY|MOC_SKILL_LIBRARY]]
- [[../MOC_AGENTS|MOC_AGENTS]]
