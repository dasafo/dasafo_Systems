---
version: 3.2.0-S
agent: DEVOPS_SRE
---

# 🩹 Skill | Self-Healing Deployment

## Objective

Automatically diagnose and repair local environment dependencies (Docker, Sockets, Permissions) before executing industrial deployment workflows.

## 🛠️ Interface (v3.2.0-S)

### Input Schema (SkillInput.params)

- `check_docker` (boolean, optional): Default `true`.
- `auto_fix` (boolean, optional): Default `false`.

### Output Schema (SkillOutput.result)

- `env_health`: (string) "HEALTHY" | "REPAIRED" | "CRITICAL".
- `diagnostics`: (list) Identified issues.
- `healing_actions`: (list) Commands executed or proposed.

### ⚖️ Mandato SI (Sistema Internacional)

Toda métrica de tiempo de recuperación (MTTR) o disponibilidad debe reportarse en unidades del SI.

## 🛡️ Industrial Constraints (Zero-Trust)

- **Evidence Based:** Diagnostics MUST be supported by physical shell execution output strings.
- **Non-Destructive:** Healing actions involving `rm` or `format` are strictly FORBIDDEN unless explicit user approval is granted (RA-authorized).

## Execution Logic

1. **Pulse Check:** Run `docker info` or `systemctl is-active docker` to verify daemon status.
2. **Diagnosis:** Map non-zero exit codes to specific causes (daemon down, permissions, missing install).
3. **Self-Healing:** Propose/Execute `systemctl start docker` or user group verification.
4. **Reporting:** Log environment events in `$TARGET_PROJECT/LOGS/incidents.log`.

---
*Skill v3.2.0-S | Status: Standardized.*
