---
version: 3.3.0-S
agent: Multiple (SECURITY / DEPLOYMENT / DEVOPS)
source: https://skills.sh/supercent-io/skills-template/resource-monitor
---

# 📊 Skill | Resource Monitor

## Objective

Monitor system-level resources (CPU, RAM, Disk, IO) at an industrial scale to detect bottlenecks, memory leaks, or unauthorized consumption.

## 🛠️ Interface (v3.3.0-S)

### Input Schema (SkillInput.params)

- `sampling_interval_s` (integer, optional): Default 30.
- `report_format` (string, optional): "pulse" | "json". Default "pulse".

### Output Schema (SkillOutput.result)

- `health_status`: (string) "STABLE" | "WARNING" | "CRITICAL".
- `metrics`: (object) CPU%, RAM(MB), IO.
- `leak_detected`: (boolean) Result of heuristic check.

### ⚖️ Mandato SI (Sistema Internacional)

Toda métrica de consumo (RAM en Megabytes, disco en Gigabytes, tiempo de CPU en segundos) debe reportarse bajo el estándar SI.

## 🛡️ Industrial Constraints (Zero-Trust)

- **Physical Pulse:** Metrics MUST be derived from physical `/proc` or `psutil` reads. Hallucinated "metrics" result in immediate container quarantine.
- **Contract Verification:** Compare against `PRP_CONTRACT.json` hardware constraints if present.

## Protocol

1. **Baseline:** Measure project consumption during initialization (Phase 0).
2. **Sampling:** Real-time monitoring of container/process health.
3. **Validation:** Compare against `PRP_CONTRACT.json` hardware constraints.
4. **Escalation:** Sustained CPU > 90% or RAM growth triggers SRE notification.

---
**ORIGIN:** [resource-monitor by supercent-io](https://skills.sh/supercent-io/skills-template/resource-monitor)
*Skill v3.3.0-S | Status: Standardized & Industrialized.*
