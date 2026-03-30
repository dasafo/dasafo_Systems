---
version: 3.3.0-S
agent: Multiple (SECURITY / PO / BACKEND / QA)
source: https://skills.sh/useai-pro/openclaw-skills-security/credential-scanner
---

# 🔍 Skill | Agentic Thought & Secret Scanner (Credential Scanner)

## Objective

Identify and mitigate accidental exposure of sensitive credentials (API keys, passwords, private keys, database URLs) within the project workspace, logs, and agent's chain-of-thought. This skill is based on the industrial-grade **Credential Scanner** protocol.

## 🛠️ Interface (v3.4.0-S)

### Input Schema (SkillInput.params)

- `target` (string, optional): Absolute path to the project to scan. If not provided, defaults to `TARGET_PROJECT`.
- `recursive` (boolean, optional): Default `true`. Scans all subdirectories except those in the exclusion list.
- `network_preflight` (boolean, optional): Set to `true` if this scan is part of a pre-flight check for a skill that requires network access. This escalates all findings to CRITICAL.

### Output Schema (SkillOutput.result)

- `status`: (string) "PASS" | "AUDIT_FAIL"
- `summary`:
  - `files_scanned`: (integer) Total number of files inspected.
  - `secrets_found`: (integer) Total number of unique secrets detected.
- `findings`: (list) List of detailed findings:
  - `file`: (string) Path to the offending file.
  - `line`: (integer) Line number of the match.
  - `type`: (string) Type of credential (e.g., "AWS Access Key", "OpenAI API Key").
  - `severity`: (string) "CRITICAL" | "WARNING".
  - `value_masked`: (string) Masked value (e.g., `sk-proj-...████████`).
  - `action`: (string) Recommended remediation step.
- `recommendations`: (list) General security improvement suggestions.

### ⚖️ Mandato SI (Sistema Internacional)

Cualquier métrica numérica generada como parte de este escaneo (tamaño de archivos escaneados, tiempo de ejecución, etc.) debe expresarse utilizando las unidades del Sistema Internacional.

## 🛡️ Industrial Constraints (Zero-Trust)

- **Physical Scan Only:** Scans actual files on disk. No mock results allowed.
- **Zero-Exposure Rule:** Full secret values MUST NEVER be displayed in logs or reports. Use `████████` for masking.
- **Gitignore Awareness:** The scanner checks if sensitive files are correctly ignored by `.gitignore`.
- **Exclusion Rules:** Automatic bypass of `node_modules/`, `vendor/`, `.git/`, `dist/`, `build/`, and binary artifacts.

## 📖 Operational Rules

1. **Masking:** Always truncate secret values with `████████`.
2. **Git Check:** Differentiate between committed secrets (CRITICAL) and local-only files (WARNING).
3. **Escalation:** If `network_preflight` is enabled, any finding is automatically CRITICAL.
4. **Remediation:** Provide specific actions for each type of leak (e.g., "Move to Secret Manager", "Rotate Key immediately").

## 💡 Usage Example

```json
{
  "agent": "security_auditor",
  "skill": "agentic-thought-secret-scanner",
  "params": {
    "target": "/home/david/Documents/AI/AGENTES/WORKSPACE",
    "network_preflight": true
  }
}
```

---
**ORIGIN:** [credential-scanner by useai-pro](https://skills.sh/useai-pro/openclaw-skills-security/credential-scanner)
*Skill v3.4.0-S | Status: Standardized & Industrialized (Dasafo Edition).*
