---
version: v4.0-S
agent: DEVOPS_SRE
source: https://skills.sh/sickn33/antigravity-awesome-skills/docker-expert
---

# 🐳 Skill | Docker Stack Provisioner (v4.0-S)

## Objective

Advanced Docker containerization expert for multi-stage builds, security hardening, and production deployment patterns. Provision infrastructure-as-code (IaC) strictly within the `WORKSPACE/infra/` boundary.

## 🛠️ Interface (v4.0-S)

### Input Schema (SkillInput.params)

- `action` (enum): `generate_dockerfile`, `generate_compose`.
- `target_project` (string, mandatory): Absolute path to the project workspace.
- `service_name` (string, mandatory): Name of the service being containerized.
- `stack_type` (enum, optional): The base stack (e.g., `node`, `python`, `static`).

### Output Schema (SkillOutput.result)

- `provision_status`: (string) `SUCCESS` or `FAILED`.
- `artifacts_produced`: (array) Paths to the generated `Dockerfile` or `docker-compose.yml`.
- `security_score`: (float) Evaluation of non-root usage and attack surface reduction.
- `industrial_status`: (string) "SOLIDIFIED - INFRA PROVISIONED".

### ⚖️ Mandato SI (Sistema Internacional)

Cualquier límite de memoria o tamaño de disco debe expresarse en **bytes** (B). Los tiempos de timeout, interval o delay en los Healthchecks y reinicios deben definirse en **segundos** (s).

## 🛡️ Industrial Constraints (Zero-Trust)

- **Surgical Access:** Files MUST only be written to `WORKSPACE/infra/` or `$TARGET_PROJECT/ops/`. Domain layers are strictly off-limits.
- **Rootless by Default:** All generated Dockerfiles must drop privileges and run as a non-root user (e.g., `USER appuser`).
- **Layer Caching Optimization:** Dependencies MUST be copied and installed before the application source code to maximize cache hits.
- **No Hardcoded Secrets:** Docker Compose files must use external secrets or environment variable passthroughs.
