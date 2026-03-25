---
name: self-healing-deployment
description: Ability to check and repair local environment dependencies (like Docker) before deployment.
---

# 🛡️ self-healing-deployment

## 📐 Description
This skill enables the `DEVOPS_SRE` agent to verify the sanity of the target environment before executing deployment commands. It specifically focus on "Pulse Checking" the Docker daemon.

## 🛠️ Execution Logic (Algorithm)
1.  **Pulse Check**: Run `docker info > /dev/null 2>&1` or `systemctl is-active docker`.
2.  **Diagnosis**: If the exit code is non-zero, identify the cause (daemon down, permissions, missing install).
3.  **Self-Healing**: 
    -   If down: Suggest or run `sudo systemctl start docker`.
    -   If permissions: Suggest checking user group `docker`.
4.  **Reporting**: Log the environment status in `LOGS/incidents` if fixed, or `LOGS/reports` if nominal.

## 📜 Usage
- Invoke this skill before `docker-compose up`.
- Use the `PulseCheck` perception to inform the user about the environment state.

---
*Skill v2.1 | Authority: DEVOPS_SRE*
