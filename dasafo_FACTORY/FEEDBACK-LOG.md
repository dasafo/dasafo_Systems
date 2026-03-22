# dasafo_System | Master Feedback Log
>
> **Status:** Active & Mandatory
> **Purpose:** Erradicate repeated mistakes. One correction here means an improvement for all agents.
> **Rule of Thumb:** ALL AGENTS MUST read this file before acting. 

| Timestamp | Context (Agent/Project) | The Error | The Correction | The Golden Rule |
| :--- | :--- | :--- | :--- | :--- |
| *YYYY-MM-DD* | *Ej: BACKEND / OmniMarket* | *Ej: Hardcoded paths used.* | *Ej: Used `$TARGET_PROJECT` env var.* | *Ej: "Never use absolute paths, use env injects for project root."* |

---

## 📝 Error Log Entries

| Timestamp | Context (Agent/Project) | The Error | The Correction | The Golden Rule |
| :--- | :--- | :--- | :--- | :--- |
| 2026-03-22 | SECURITY / Pulse-X | Hardcoded API KEY in `twitter_connect.py`. | Use `os.getenv` + `.env` file. | **"Never commit raw credentials."** |
| 2026-03-22 | QA / Pulse-X | FastAPI Routing Conflict (Static vs Dynamic). | Move static routes BEFORE params. | **"FastAPI parses paths in order. Fixed routes go first."** |

