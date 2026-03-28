---
version: 3.2.0-S
agent: DEVOPS_SRE
---

# 🛡️ Skill | MLOps Deployment Guard

## Objective

Safely deploy, monitor, and scale Machine Learning models in production environments, ensuring version integrity and performance stability.

## 🛠️ Interface (v3.2.0-S)

### Input Schema (SkillInput.params)

- `model_tag` (string): Version tag to deploy.
- `strategy` (string, optional): "blue-green" | "canary" | "recreate". Default "canary".

### Output Schema (SkillOutput.result)

- `deployment_status`: (string) "STABLE" | "DEGRADED".
- `inference_latency_ms`: (integer) Global average (SI).
- `drift_detected`: (boolean) If model performance deviates from training benchmarks.

### ⚖️ Mandato SI (Sistema Internacional)

La latencia de inferencia y el consumo de recursos (vRAM, vCPU) deben reportarse estrictamente bajo el SI.

## 🛡️ Industrial Constraints (Zero-Trust)

- **Checksum Lock:** Production environments MUST mirror training environment checksums (pinned dependencies). Cross-environment drift triggers automatic rejection.
- **Physical Verification:** Deployment success REQUIRES physical reachability of the new model endpoint and a status report in `LOGS/DEVOPS/`.

## Deployment Standards

1. **Versioning:** Mandatory unique tags for every deployment.
2. **Solidity:** Production environment must mirror training environment checksums (pinned dependencies).
3. **Observability:** Continuous monitoring of "Model Drift".
4. **Fallback:** Automatic rollback if accuracy drops below the industrial threshold.

---
*Skill v3.2.0-S | Status: Standardized.*
