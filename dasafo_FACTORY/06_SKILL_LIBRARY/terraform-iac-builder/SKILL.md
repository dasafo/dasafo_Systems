---
version: v5.0-MCP (Native)
agent_authorization: [DEVOPS_SRE]
production_category: SHIP
source: https://skills.sh/hashicorp/agent-skills/terraform-style-guide
protocol: IaC-First / DAST
---

# 🌍 Skill | terraform-iac-builder

## Objective

Generate and maintain industrial-grade Terraform IaC. Enforces HashiCorp's official style (file separation) and the Zero-Trust mandate of the factoría.

## 🛠️ Interface (v5.0-MCP Native)

**MANDATORY:** Use direct typed arguments. `params_json` is **DEPRECATED**.

### Typed Parameters

- `agent` (string): Your Agent ID (must be 'DEVOPS_SRE').
- `target_project` (string): Absolute path to the project root.
- `action` (enum): `scaffold_module`, `generate_resource`.
- `module_name` (string): Infrastructure module name (e.g., 'database').
- `cloud_provider` (enum): `aws`, `gcp`, `azure`.
- `isolate` (boolean): Execution in Clean Session.

## 🛡️ Industrial Constraints

- **File Separation:** Monolithic `.tf` files are FORBIDDEN. Must use `providers.tf`, `main.tf`, `variables.tf`, and `outputs.tf`.
- **Surgical Access:** Files MUST only be written to `WORKSPACE/infra/terraform/`.
- **SI Standards:** Timeouts and latencies in **seconds (s)**; sizes in **bytes (B)**.
- **Zero-Secrets:** Credentials must NEVER be hardcoded.

---
*Standard v5.0-MCP | Dasafo Factory Operations Hub.*
