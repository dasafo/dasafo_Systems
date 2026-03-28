---
version: 3.2.0-S
agent: FACTORY_EVOLVER
---

# 🛡️ Skill | Checkpoint Manager

## Objective
Handle versioning and rollback of factory-wide skills, rules, and configurations to ensure industrial history integrity.

## 🛠️ Interface (v3.2.0-S)

### Input Schema (SkillInput.params)
- `action` (string, optional): "backup" | "restore" | "list". Default "backup".
- `skill_name` (string, optional): Target skill to checkpoint.

### Output Schema (SkillOutput.result)
- `checkpoint_id`: (string) Unique ID for the backup.
- `status`: (string) "STABLE" | "RESTORED".
- `backup_path`: (string) Location of the archived version.

### ⚖️ Mandato SI (Sistema Internacional)
Los intervalos de tiempo entre backups y el tamaño de los archivos comprimidos de respaldo deben reportarse estrictamente en unidades del SI (segundos, bytes).

## 🛡️ Industrial Constraints (Zero-Trust)
- **Atomic Persistence:** Backups must be physically written to `.archive/` within the `TARGET_PROJECT`. Failure to write to disk must be treated as a `SkillOutput.failure`.
- **Integrity Validation:** Archiving processes verify the physical checksum of files before and after the move.

## Protocol
1.  **Pre-mutation Backup:** Before any optimization task, physically copy current state to `.archive/v[X]/`.
2.  **Version Logging:** Update `FACTORY_VERSION.md` with timestamp and summary.
3.  **Integrity Validation:** Ensure no dead links or broken dependencies post-checkpoint.
4.  **Rollback:** Automatic restoration if errors are detected in subsequent iterations.

---
*Skill v3.2.0-S | Status: Standardized.*
