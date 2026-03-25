# dasafo_System | Master Feedback Log

> **Version:** v2.0
> **Status:** Active & Mandatory
> **Schema:** `00_GLOBAL_KNOWLEDGE/FEEDBACK_SCHEMA.json`
> **Purpose:** Eradicate repeated mistakes. One correction here improves ALL agents.
> **Rule:** ALL AGENTS MUST execute the `autoshield-preflight-check` before acting.

---

## 📋 Quick Lookup Index

| Category | Entry IDs | Key Rules |
| :--- | :--- | :--- |
| security | FB-0001 | Never commit raw credentials |
| routing | FB-0002 | FastAPI: fixed routes before params |

---

## 📝 Feedback Entries

### FB-0001

```yaml
id: FB-0001
version: v2.0
timestamp: 2026-03-22
context:
  agent: SECURITY_AUDITOR
  project: Pulse-X
  file: twitter_connect.py
severity: critical
error_description: "Hardcoded API KEY found in twitter_connect.py. Credential exposed in source code."
correction: "Use os.getenv() + .env file. Add .env to .gitignore. Never store secrets in source."
golden_rule: "Never commit raw credentials. Use environment variables or secure secret managers."
categories:
  - security
  - configuration
affected_agents:
  - BACKEND_DEV
  - FRONTEND_DEV
  - DEVOPS_SRE
```

### FB-0002

```yaml
id: FB-0002
version: v2.0
timestamp: 2026-03-22
context:
  agent: QA_TESTER
  project: Pulse-X
  file: main.py
severity: high
error_description: "FastAPI routing conflict: static route /users/me was matched by dynamic route /users/{user_id}."
correction: "Move static routes (e.g., /users/me) BEFORE dynamic parameter routes (e.g., /users/{user_id})."
golden_rule: "FastAPI parses paths in declaration order. Fixed routes MUST be declared before parameterized routes."
categories:
  - routing
  - api
affected_agents:
  - BACKEND_DEV
  - ARCHITECT
```

---

*New entries must conform to `FEEDBACK_SCHEMA.json`. Agents proposing entries must use the `autoshield-feedback-writer` skill and obtain Human Approval before appending.*
