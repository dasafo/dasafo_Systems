---
description: Handles versioning and rollback of factory-wide skills and rules.
---

# 🛡️ SKILL: checkpoint-manager

1. **Pre-mutation Backup:** Before any `skill-optimization` task, copy the current `SKILL.md` to `.archive/skills_v[X]/`.
2. **Version Logging:** Update `FACTORY_VERSION.md` with a timestamp and a brief summary of the change.
3. **Integrity Validation:** Run `factory-audit-pro` immediately after a change to ensure no dead links were created.
4. **Rollback Protocol:** If an error is detected in the next 10 project iterations, restore the last known stable version from the archive.
