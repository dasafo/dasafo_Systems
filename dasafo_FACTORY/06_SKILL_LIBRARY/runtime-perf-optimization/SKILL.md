---
version: 3.2.0-S
agent: BACKEND_DEV
---

# 🧠 Skill | Runtime Performance Optimization

## Objective

Detect and resolve performance bottlenecks, memory leaks, and inefficient resource usage in Python-based agentic services using industrial profiling.

## 🛠️ Interface (v3.2.0-S)

### Input Schema (SkillInput.params)

- `mode` (string, optional): "memory" | "cpu". Default "memory".
- `tracemalloc_snapshots` (integer, optional): Default 2.

### Output Schema (SkillOutput.result)

- `bottlenecks_found`: (list) Identified inefficient code sites.
- `optimization_proposed`: (string) Markdown recommendation.
- `vibe_check`: (string) "PERFORANT".

### ⚖️ Mandato SI (Sistema Internacional)

Cualquier mejora de rendimiento (ahorro de latencia en ms, reducción de RAM en bytes) debe citarse en el SI.

## 🛡️ Industrial Constraints (Zero-Trust)

- **Traceable Profiling:** Optimizations MUST reference a physical snapshot or `cProfile` dump saved in `LOGS/perf/`.
- **SI Mandatory:** Performance deltas (before/after) MUST be reported in SI units for auditability.

## Optimization Strategy

1. **Leak Detection:** Use `tracemalloc` snapshots to find objects that persist illegally.
2. **Iterative RAM:** Replace large list loads with generators and line-by-line iterators.
3. **Weak Cache:** Implement `weakref.WeakValueDictionary()` for caches to prevent "Cache Bloat".
4. **Verification:** Force `gc.collect()` in critical yield points to measure reclaimable memory.

---
*Skill v3.2.0-S | Status: Standardized.*
