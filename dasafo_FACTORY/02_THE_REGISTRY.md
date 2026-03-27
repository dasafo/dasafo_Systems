# 🗺️ 02_THE_REGISTRY | The Inventory & Versioning

> **Standard:** v3.2.0-S "Modular Toolbox"
> **Focus:** State, Missions, Version & Project Initialization

---

## 🏷️ 1. Factory Version (v3.2.0-S "Modular Toolbox")

**Status:** Active Deployment | Industrial Scale.

### 📈 Current Release (v3.1.5)

- **Solidity Guard:** Implemented mandatory `kanban-solidity-gate` for all phase transitions.
- **Section 06 - Modular Toolbox (v3.2):** All agent skills centralized in `06_SKILL_LIBRARY/`. Removed `SOUL.md` and `BOOTSTRAP.md` redundancy.
- **Segregation of Duties:** Decoupled 'Implementor' (DEV) from 'Verifier' (QA/ARCH) via independent Audit Signatures.
- **Anti-Fraud Protocols:** Physical `task.md` now requires verified signatures to prevent agentic "cheating".
- **Master Registry Rule:** Instead of moving Markdown files across directories, all task orchestration is handled through **`TASKS/registry.json`**. This is the **Logistical Source of Truth**.
- **Phase-Gate Protocol (Aduana Universal):** El archivo **`PROJECT_STATE.json`** es la **Autoridad de Estado (SSoT)**. Ningún cambio de fase es válido sin la firma física del humano en este archivo.
- **Infra-Aware Agents:** All 16 agent identities synchronized to prioritize shared resources.

---

## 🚀 2. Active Missions (Project Inventory)

| Mission ID | Project Name | Status | Priority | Tags |
| :--- | :--- | :--- | :--- | :--- |
| **MISSION-VIBE-001** | **VibeBoard** | 📋 ACTIVE | HIGH | SAAS, PREMIUM, NEXTJS |
| **MISSION-K镜-001** | **KnowledgeMirror** | 🛡️ ACTIVE | CRITICAL | REFLECTION, VALIDATION, ZERO-TRUST |
| **MISSION-REPURPOSE-001** | **content-repurpose** | 🤖 ACTIVE | HIGH | AI, OPENAI, CONTENT-AUTOMATION |

---

## 🏗️ 3. Project Initialization (`init_project.sh`)

**Standard Skeleton:** The factory mandates a strict directory structure for every project.

### 🏛️ CORE Skeleton Architecture

- `LOCAL_KNOWLEDGE/`: Contract `PRP_CONTRACT.json` and local context.
- `LOGS/`:
  - `agents/`: Agent logs.
  - `sessions/`: Session data.
  - `reports/`, `incidents/`: Compliance data.
  - **`EXECUTION_LOG.md`**: Industrial chronicle.
- `TASKS/`:
  - `01_PENDING` to `05_REJECTED`: Manual task tracking.
  - **`registry.json`**: Programmatic task registry (**Single Source of Truth**).
  - `task.md`: Visual Kanban Mirror.
- `WORKSPACE/`: `backend/`, `frontend/`, `shared/`.

### 🛡️ Guardrails on Launch

- **`registry.json` (Tasks):** Seeded with initial M1 tasks. Mandatory for logistical tracking.
- **`PROJECT_STATE.json` (Aduana):** Tracks factory version (3.2.0-S) and **Authorized Phase Status**. No Phase skip is allowed without this file.
- **`.env`:** Seeded with mandatory metadata (Docker network, infrastructure endpoints).

---

*02_THE_REGISTRY v3.2.0-S | Status: Solidified.*
