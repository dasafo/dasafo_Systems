# 📡 dasafo_FACTORY | MCP Senses Protocol
>
> **Standard:** v2.1 "Sensory Bridge"
> **Focus:** High-Fidelity Infrastructure Interaction

## 🧠 The Sensory Philosophy
Agents do not "run commands"; they **perceive** and **act** through the Sensory Bridge. This ensures a zero-trust, audited, and project-agnostic interaction model.

## 📡 Core Senses (MCP Servers)

### 1. Filesystem Sense (`filesystem`)
- **Capabilities:** Read/Write/Search within `$TARGET_PROJECT`.
- **Constraint:** Never access paths outside the allowed workspace.
- **Audit:** All file mutations must be logged to `LOGS/agents/{agent}.log`.

### 2. GitHub Sense (`github`)
- **Capabilities:** PR creation, issue tracking, and code reviews.
- **Constraint:** Use semantic commit messages (feat, fix, refactor).

### 3. NotebookLM Sense (`notebooklm`)
- **Capabilities:** Deep research and source synthesis.
- **Constraint:** Only use for Phase M1 (Discovery) and M2 (Architecture).

### 4. Custom Skills (`run.py`)
- **Capabilities:** Executable logic tailored for specific agent roles.
- **Constraint:** Must follow the `skill_schema.py` and be 100% project-agnostic.

---
*Senses Protocol v2.1 | Status: Solidified.*
