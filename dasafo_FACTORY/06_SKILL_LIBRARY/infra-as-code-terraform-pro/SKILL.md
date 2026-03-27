---
version: 3.2.0-S
agent: DEVOPS_SRE
---

# 🏗️ Skill | IaC Terraform Support

## Objective
Manage industrial cloud infrastructure through declarative, version-controlled code using the Terraform standard.

## 🛠️ Interface (v3.2.0-S)

### Input Schema (SkillInput.params)
- `action` (string, optional): "plan" | "apply" | "audit". Default "plan".
- `module` (string, optional): Target infrastructure module (e.g., "db", "vpc").

### Output Schema (SkillOutput.result)
- `plan_summary`: (string) Summary of infrastructure changes.
- `drift_detected`: (boolean) If real infrastructure differs from code.
- `status`: (string) "DEPLOYMENT_READY" | "DRIFT_ALERT".

### ⚖️ Mandato SI (Sistema Internacional)
Cualquier métrica de rendimiento de infraestructura (ancho de banda en bits/s, latencia de red, IOPS) debe reportarse en el SI.

## Key Protocols
- **State Management:** Use remote backends with mandatory locking.
- **Modularity:** Group resources into reusable modules for scaling.
- **Drift Detection:** Periodic `terraform plan` to ensure SSoT consistency.
- **Optimization:** Lifecycle tagging (SI) for cost tracking and auto-destruction.

---
*Skill v3.2.0-S | Status: Standardized.*
