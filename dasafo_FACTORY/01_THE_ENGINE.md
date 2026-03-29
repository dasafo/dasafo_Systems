# ⚙️ 01_THE_ENGINE | The Motor Executive

> **Standard:** v3.3.1-S "Industrial Core"
> **Focus:** Operations, Pipeline & Phase-Gate Protocol (Aduana Universal)

---

## 🛣️ 1. Universal Pipeline (M1-M5 Maturity)

The 5-phase journey mandated for every industrialized project.

### 🔍 M1: Discovery
- **Owner:** `PRODUCT_OWNER`
- **Output:** **12-Section PRP Contract** (Status: `signed`).
- **Signature Gate:** `PROJECT_STATE.json -> "M1": "APPROVED"`.

### 📐 M2: Architecture
- **Owner:** `ARCHITECT`
- **Output:** Blueprint artifacts in `DOCS/ARCH/` + `TASKS/registry.json`.
- **Signature Gate:** `PROJECT_STATE.json -> "M2": "APPROVED"`.

### ⚙️ M3: Production
- **Owner:** `BACKEND_DEV` / `FRONTEND_DEV`
- **Output:** Functional code (Standard v3.3.1-S) + **BUILD_REPORT.json**.
- **Signature Gate:** `PROJECT_STATE.json -> "M3": "APPROVED"`.

### 🧪 M4: Compliance
- **Owner:** `QA_TESTER` / `DOCS_MASTER`
- **Output:** Security Scan + Playwright/JUnit reports + `DOCS/`.
- **Signature Gate:** `PROJECT_STATE.json -> "M4": "APPROVED"`.

### 🔄 M5: Operations
- **Owner:** `FACTORY_EVOLVER` / `MEMORY_OPTIMIZER`
- **Output:** Deployment + FEEDBACK-LOG entries + Knowledge Vectorization.
- **Signature Gate:** `PROJECT_STATE.json -> "M5": "APPROVED"`.

---

## 🛡️ 2. Phase-Gate Protocol (Aduana Universal)

### 🚫 Anti-Chat Rule (Zero-Trust)
**Chat Is for coordination; the filesystem is for authorization.**
Agents are prohibited from promoting a phase without physical detecting `"APPROVED"` in **`PROJECT_STATE.json`** and synchronizing **`TASKS/registry.json`**.

### 🗂️ Zero-Trust Synchronization (Modul-T)
Every task MUST have its corresponding JSON artifact in the project's `TASKS/` hierarchy:
- `TASKS/01_PENDING/`
- `TASKS/02_IN_PROGRESS/`
- `TASKS/03_COMPLETED/`
Any status change WITHOUT physical file movement is an architectural breach.

### 🛂 The Customs Flow (kanban-solidity-gate)
1. **Technical Closure:** The agent completes all tasks **AND** physically moves artifacts to `03_COMPLETED/`.
2. **Signature Request:** The agent formally requests the Human to review the generated evidence.
3. **Physical Signature (HITL):** The user physically updates **`PROJECT_STATE.json`** to `"APPROVED"`.
4. **Gate Verification:** The **`kanban-solidity-gate`** skill verifies the task registry against the disk state. If synchronized, the next phase is unlocked.

---

## 📡 3. Sensory Hub (Top 18 Modular Toolbox)

### 🧠 Tactical Execution
Agents do not "run commands" blindly. They act through specialized, auditable skills from the **Top 18 Mapping**.

### 📡 Core Hub Skills
- **`kanban-solidity-gate`**: The Phase-Gate executor.
- **`agentic-thought-secret-scanner`**: The Security pre-flight check.
- **`prp-generator`**: The M1 contract engine (12 sections).
- **`factory-audit-pro`**: The M4 compliance scanner.
- **`hallucination-guardrail`**: The Memory Optimizer safeguard.

---

## 🏗️ 4. Operational Synergy

### 🔄 Global Operational Rules
- **SI Units Reporting:** All performance logs MUST use **Seconds (s)** and **Bytes (B)**.
- **Shared Infrastructure:** Heavy services (Supabase, Neo4j, Redis) reside on the `INFRA` node.
- **AutoShield Policy:** Every critical failure must generate a `FEEDBACK-LOG` entry adhering to `FEEDBACK_SCHEMA.json` to vaccinate against systemic recurrence.

---
*01_THE_ENGINE v3.3.1-S | Industrial Engine Active.*
