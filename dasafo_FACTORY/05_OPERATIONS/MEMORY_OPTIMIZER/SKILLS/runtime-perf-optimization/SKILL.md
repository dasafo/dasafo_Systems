---
description: Detecting and fixing memory leaks and inefficient memory usage in Python-based agents and services.
---

# 🧠 SKILL: Runtime Memory Optimization (Python)

Based on the [Python Performance Optimization](https://skills.sh/wshobson/agents/python-performance-optimization) standard.

## 1. Detection of Memory Leaks
- Use `tracemalloc` to take snapshots before and after long-running tasks in the backend.
- Compare snapshots to find objects that are growing but never released.
- Use `gc.collect()` to force garbage collection in critical memory yield points.

## 2. Iterators vs Lists (RAM Efficiency)
- **Constraint:** Never load multi-gigabyte datasets or logs into a single list.
- **Action:** Replace `f.readlines()` with line-by-line iterators. Use generator expressions for data piping.

## 3. Weak References for Caches
- Use `weakref.WeakValueDictionary()` for caching persistent objects. This allows the garbage collector to reclaim objects if they are no longer in active use elsewhere, preventing "Cache Bloat".
