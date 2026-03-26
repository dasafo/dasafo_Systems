# 🛡️ Skill | MLOps Deployment Guard
> **Version:** v3.1.5 "Solidity Guard"
> **Source:** https://skills.sh/davila7/claude-code-templates/scikit-learn (Adapted for Ops)
> **Agent:** DEVOPS_SRE

## Objective
Safely deploy and monitor Machine Learning models in production.

## Deployment Standards
- **Model Versioning:** Never replace a model without a version tag and a fallback strategy.
- **Dependency Pinning:** Ensure the production Python environment matches the `DATA_SCIENTIST` training environment exactly.
- **Performance Profiling:** Monitor inference latency and resource usage (CPU/GPU/RAM).
- **A/B Testing:** Support blue-green or canary deployments for gradual model rollouts.

## Health Check
Monitor "Model Drift" in production logs—if accuracy drops below threshold, notify the DATA_SCIENTIST immediately.
