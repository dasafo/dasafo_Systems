---
version: 3.2.0-S
agent: DATA_SCIENTIST
---

# 🐼 Skill | Pandas Vectorized Pro

## Objective
Optimize data transformation workflows using high-performance vectorized operations to maximize memory efficiency and computational throughput.

## 🛠️ Interface (v3.2.0-S)

### Input Schema (SkillInput.params)
- `df_path` (string): Absolute path to the CSV/Parquet file.
- `optimization_level` (string, optional): "memory" | "speed". Default "memory".

### Output Schema (SkillOutput.result)
- `memory_saved_bytes`: (integer) (SI units).
- `transformation_stats`: (object) Dtypes and counts.
- `vibe_check`: (string) "VECTORIZED".

### ⚖️ Mandato SI (Sistema Internacional)
Cualquier métrica de rendimiento (ahorro de memoria en bytes, tiempo de procesamiento en segundos) debe informarse en el SI.

## Best Practices
1.  **Iter-Free:** Mandatory avoidance of Python `for` loops. Use NumPy/Pandas vectorization.
2.  **Memory:** Use optimized dtypes (`uint8`, `float32`, `category`) to minimize footprint.
3.  **Safety:** Mandatory use of `.loc` and `.copy()` to ensure data integrity (Solid Principle).
4.  **Validation:** Enforce unit normalization into the System International.

---
*Skill v3.2.0-S | Status: Standardized.*
