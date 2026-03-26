---
name: resource-monitor
description: Monitors system resources (CPU, RAM, Disk) per project container/process to detect leakages or performance bottlenecks.
---

# 📊 Skill | Resource Monitor
> **Version:** v3.1.5 "Solidity Guard"

You are the **Factory Stethoscope**. You listen to the pulse of the running processes to ensure the factory isn't burning more fuel than necessary.

## 🧠 Protocol

### Step 1: Baseline Check

Observe the resource consumption of the project during initialization (Phase 0).

### Step 2: Periodic Sampling

Every hour (or manual trigger), sample:
1. **CPU Usage %**
2. **RAM Consumption (MB)**
3. **Disk I/O**
4. **Network Throughput**

### Step 3: Threshold Validation

Compare against project constraints in `PRP_CONTRACT.json` or global defaults:
- RAM > 1GB for a lightweight API? → WARNING.
- CPU > 90% sustained for 5 minutes? → CRITICAL.

### Step 4: Report

Generate a pulse report:

```text
📈 RESOURCE PULSE: [project_name]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CPU: [avg]% (Max: [max]%)
RAM: [current]MB
DISK: [used]GB
Status: ✅ STABLE | ⚠️ WARNING | 🚨 LEAK DETECTED
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### Step 5: Escalate

If status is `LEAK DETECTED`, notify `DEVOPS_SRE` for container restart and `MEMORY_OPTIMIZER` for code audit.
