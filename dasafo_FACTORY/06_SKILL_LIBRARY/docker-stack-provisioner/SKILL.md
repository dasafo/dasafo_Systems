---
version: v5.0-MCP (Native)
agent_authorization: [DEVOPS_SRE]
source: https://skills.sh/sickn33/antigravity-awesome-skills/docker-expert
protocol: IaC-First / DAST
---

# 🐳 Skill | docker-stack-provisioner

## Objective

Provide advanced Docker containerization strictly within the `WORKSPACE/infra/` boundary. Ensures rootless, multi-stage builds with strict SI metric adherence.

## 🛠️ Interface (v5.0-MCP Native)

**MANDATORY:** Use direct typed arguments. The `params_json` structure is **DEPRECATED**.

### Typed Parameters

- `agent` (string): Your Agent ID (DEVOPS_SRE).
- `target_project` (string): Path to project root.
- `action` (enum): `generate_dockerfile`, `generate_compose`.
- `service_name` (string): Name of the service (default: 'app').
- `stack_type` (enum): Base stack (e.g., 'node', 'python').
- `isolate` (boolean): Execution in Clean Session.

## 🛡️ Industrial Constraints

- **Surgical Access:** Files MUST only be written to `WORKSPACE/infra/`. Domain layers are off-limits.
- **SI Standards:** Memory limits in **Bytes (B)** and intervals in **Seconds (s)**.
- **Rootless Mandate:** All containers must run as non-root users.

---
**ORIGIN:** [docker-expert by sickn33](https://skills.sh/sickn33/antigravity-awesome-skills/docker-expert)
