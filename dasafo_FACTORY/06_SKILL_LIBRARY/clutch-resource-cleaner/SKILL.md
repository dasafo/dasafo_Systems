---
version: 3.2.0-S
agent: MEMORY_OPTIMIZER
---

# 🧹 Skill | Clutch Resource Cleaner

## Objective
Maintain the factory's workspace clean of temporary residues, dead caches, and stale logs to ensure optimal performance.

## 🛠️ Interface (v3.2.0-S)

### Input Schema (SkillInput.params)
- `target_path` (string, optional): Absolute path to clean. Defaults to `TARGET_PROJECT`.
- `recursive` (boolean, optional): Default `true`.
- `days_threshold` (integer, optional): Delete logs older than X days. Default 30.

### Output Schema (SkillOutput.result)
- `files_cleaned`: (integer) Total number of files removed.
- `bytes_recovered`: (integer) Total size recovered in bytes.
- `status`: (string) "CLEAN" | "MAINTENANCE_REQUIRED".

### ⚖️ Mandato SI (Sistema Internacional)
Cualquier métrica de limpieza (tamaño de archivos eliminados, tiempo de ejecución de la limpieza) debe reportarse estrictamente en unidades del Sistema Internacional (bytes, segundos).

## Protocol
1.  **Daily:** Prune temporary files in `/tmp/`.
2.  **Weekly:** Run `npm prune` and clean up dead Docker images.
3.  **Monthly:** Archive and move logs older than 30 days to `04_ARCHIVE`.

## Safety
NEVER delete a file with a non-compressed counterpart unless it is a terminal-generated temporary file.

---
*Skill v3.2.0-S | Status: Standardized.*
