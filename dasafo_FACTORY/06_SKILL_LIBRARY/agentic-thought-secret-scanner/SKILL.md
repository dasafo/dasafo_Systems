---
version: 3.3.0-S
agent: Multiple (SECURITY / PO / BACKEND / QA)
source: https://skills.sh/supercent-io/skills-template/agentic-thought-secret-scanner
---

# 🔍 Skill | Agentic Thought & Secret Scanner

## Objective

Detect accidental secret leakage and internal insecurity within the agents' internal chain-of-thought and logs.

## 🛠️ Interface (v3.3.0-S)

### Input Schema (SkillInput.params)

- `target` (string, optional): Absolute path to the project to scan. If not provided, defaults to `TARGET_PROJECT`.
- `recursive` (boolean, optional): Default `true`. Scans all subdirectories except `.git`, `node_modules`, etc.

### Output Schema (SkillOutput.result)

- `status`: (string) "PASS" | "AUDIT_FAIL"
- `findings_count`: (integer) Total number of secrets found.
- `findings`: (list) List of findings:
  - `file`: (string) Path to the offending file.
  - `type`: (string) Pattern type (e.g., "OPENAI_KEY").
  - `match_count`: (integer) Number of matches in that file.
- `scanned_path`: (string) The absolute path that was audited.

### ⚖️ Mandato SI (Sistema Internacional)

Cualquier métrica numérica generada como parte de este escaneo (tamaño de archivos escaneados, tiempo de ejecución, etc.) debe expresarse utilizando las unidades del Sistema Internacional (ej: segundos para tiempo, bytes/kilobytes para tamaño).

## 🛡️ Industrial Constraints (Zero-Trust)

- **Physical Scan Only:** This skill is FORBIDDEN from generating mock results. It MUST physically access the filesystem.
- **Path Validation:** If `target` is not a valid physical directory, the skill MUST return a `SkillOutput.failure`.
- **Exclusion Rules:** Automatic bypass of `.git`, `node_modules`, and binary artifacts to optimize compute resources (SI).

## 📖 Audit Checklist

1. **Thought Scan:** Monitor agent "Thinking" blocks for accidental extraction of hidden architectural secrets.
2. **Secret Redaction:** If an agent accidentally logs an API key during an error, the Auditor must flag it for immediate rotation and redaction from `LOGS/`.
3. **Privilege Decay:** Periodically review if an agent has more MCP tool access than it actually uses. Recommend "tool-pruning" in the `AGENT_REGISTRY.md`.

## 💡 Usage Example

```json
{
  "agent": "security_auditor",
  "skill": "agentic-thought-secret-scanner",
  "params": {
    "target": "/home/david/Documents/AI/AGENTES/WORKSPACE"
  }
}
```

## Goal

Minimize the internal attack surface by enforcing "Least Privilege" and ensuring zero-trace of sensitive credentials via physical file inspection.

---
**ORIGIN:** [agentic-thought-secret-scanner by supercent-io](https://skills.sh/supercent-io/skills-template/agentic-thought-secret-scanner)
*Skill v3.3.0-S | Status: Standardized & Industrialized.*
