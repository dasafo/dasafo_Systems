# Skill: Clutch Resource Cleaner (Factory Sweep)
> **Source:** https://skills.sh/karpathy/nanochat/clutch-audit (Adapted)
> **Agent:** MEMORY_OPTIMIZER

## Objective
Maintain the factory's workspace clean of temporary residues, dead caches, and stale logs.

## Maintenance Schedule
- **Daily:** Prune temporary files in `/tmp/`.
- **Weekly:** Run `npm prune` and clean up dead Docker images (if authorized by DEVOPS_SRE).
- **Monthly:** Archive and move logs older than 30 days to the "Deep Cold Storage" (`04_ARCHIVE`).

## Safety
NEVER delete a file with a non-compressed counterpart unless it is a terminal-generated temporary file.
