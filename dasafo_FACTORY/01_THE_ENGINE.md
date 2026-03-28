# ⚙️ 01_THE_ENGINE | The Motor Executive

> **Standard:** v3.2.5-S "Stark-Solidity"
> **Focus:** Operations, Pipeline & Phase-Gate Protocol (Universal Customs)

---

## 🛣️ 1. Universal Pipeline (M1-M5 Maturity)

The 5-phase journey mandated for every industrial project.

### 🔍 M1: Discovery

- **Owner:** `PRODUCT_OWNER`
- **Output:** `PRP_CONTRACT.json` (Status: `signed`).
- **Signature Gate:** `PROJECT_STATE.json -> "M1": "APPROVED"`.

### 📐 M2: Architecture

- **Owner:** `ARCHITECT`
- **Output:** Blueprint artifacts + `TASKS/registry.json`.
- **Signature Gate:** `PROJECT_STATE.json -> "M2": "APPROVED"`.

### ⚙️ M3: Production

- **Owner:** `BACKEND_DEV` / `FRONTEND_DEV`
- **Output:** Functional code (100% SoC) + **SUCCESSFUL BUILD LOG**.
- **Signature Gate:** `PROJECT_STATE.json -> "M3": "APPROVED"`.

### 🧪 M4: Compliance

- **Owner:** `QA_TESTER` / `DOCS_MASTER`
- **Output:** Security Audit + Audit Signatures.
- **Signature Gate:** `PROJECT_STATE.json -> "M4": "APPROVED"`.

### 🔄 M5: Operations

- **Owner:** `DEVOPS_SRE` / `FACTORY_EVOLVER`
- **Output:** Deployment + Global Semantic Index.
- **Signature Gate:** `PROJECT_STATE.json -> "M5": "APPROVED"`.

---

## 🛡️ 2. Phase-Gate Protocol (Universal Customs)

### 🚫 Anti-Chat Rule (No-Trust Policy)

**Chat is for coordination; the filesystem is for authorization.**

Any "OK" or approval in the chat history is **perceived** but **not binding**. Agents are prohibited from promoting a phase without physical verification of the disk state.

### 🗂️ Physical Synchronization Mandate (v3.2.5-S)

**The Master Tally (`registry.json` / `task.md`) is NOT ENOUGH.**
Every task MUST have a physical JSON artifact representing its state in the corresponding folder:

- `TASKS/01_PENDING/`
- `TASKS/02_IN_PROGRESS/`
- `TASKS/03_COMPLETED/`

Any status change MUST include physically creating or moving the JSON file to the correct directory. Falsifying task status without physical artifacts is a severe Industrial Break.

### 🛂 The Customs Flow (Step-by-Step)

1. **Technical Closure:** The phase agent completes all tasks in `TASKS/registry.json` **AND** physically moves the JSON artifact to `TASKS/03_COMPLETED/`. **BLOCKING REQUIREMENT:** Must attach physical proof of a successful `build` (v3.2.4-S).
2. **Signature Request:** The agent formally requests the Human to review the generated artifacts.
3. **Physical Signature (Human):** The user must physically open **`PROJECT_STATE.json`** and change the current phase status from `"PENDING"` to `"APPROVED"`.
4. **Sensory Validation (Agent):** The orchestrator agent uses its `filesystem` sense to read the file. Only if it physically detects `"APPROVED"`, is the transition to the next phase enabled.

---

## 📡 3. MCP Senses Protocol (The Sensory Bridge)

### 🧠 The Sensory Philosophy

Agents do not "run commands"; they **perceive** and **act** through the Sensory Bridge (MCP).

### 📡 Core Senses

- **Filesystem Sense:** Read/Write/Search within `$TARGET_PROJECT`.
  - **Constraint:** Mandatory check of `PROJECT_STATE.json` before any Phase Promotion.
- **GitHub Sense:** PR creation, issue tracking, and code reviews.
  - **Constraint:** Use semantic commit messages (feat, fix, refactor).
- **NotebookLM Sense:** Deep research and source synthesis (Phases M1/M2).
- **Custom Skills (`run.py`):** Executable logic tailored for specific agent roles.
  - **Constraint:** All skills reside in **`06_SKILL_LIBRARY/`**. Agents invoke them modularly. Mandatory execution of `kanban-solidity-gate` for phase transitions (Checks **TASKS/registry.json** as SSoT) and state-gate (linked to **PROJECT_STATE.json**).
  - **🚨 Human-in-the-Loop Mutation Gate (v3.2.5-S):** Direct modification of any `run.py` within `06_SKILL_LIBRARY/` is **STRICTLY PROHIBITED** without an explicit **Mutation Proposal**.
    - **Step 1:** The agent MUST diagnose the error or improvement.
    - **Step 2:** The agent MUST show the exact code diff to be applied.
    - **Step 3:** The agent MUST wait for an explicit user approval (e.g., "@David, I approve the mutation for skill X"). 
    - **Exception:** Only `FACTORY_EVOLVER` can propose mutations as part of its core identity. All other agents must justify the "Critical Fault" causing the need for change.

---

## 🏗️ 4. Operations Manual (Synergy & Strategy)

### 🔄 Global Operational Events

- **Atomic Reflection (❤️):** Agents update their operational performance in their internal `IDENTITY.md` after every major task.
- **Pre-Flight Check (🛸):** Mandatory `autoshield-preflight-check` before destructive actions.
- **Shared Infra Health:** Verify `INFRA` via Glances (Port 61208) before Phase M3.
- **Stateless Execution:** Agents must be able to reconstruct their current intent by reading `PROJECT_STATE.json`, without depending on previous chat history.

---

*01_THE_ENGINE v3.2.5-S | Status: Stark-Solidified.*
