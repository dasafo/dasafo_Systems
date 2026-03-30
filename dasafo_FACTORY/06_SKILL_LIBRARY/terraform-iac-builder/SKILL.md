---
version: 3.4.0-S
agent: DEVOPS_SRE
source: https://skills.sh/hashicorp/agent-skills/terraform-style-guide
---

# 🌍 Skill | Terraform IaC Builder (v3.4.0-S)

## Objective

Generate and maintain Terraform Infrastructure-as-Code (IaC) following HashiCorp's official style conventions and the Zero-Trust industrial standard of the dasafo_FACTORY.

## 🛠️ Interface (v3.4.0-S)

### Input Schema (SkillInput.params)

- `action` (enum): `scaffold_module`, `generate_resource`.
- `target_project` (string, mandatory): Absolute path to the project workspace.
- `module_name` (string, mandatory): Name of the infrastructure module (e.g., `network`, `database`).
- `cloud_provider` (enum, optional): `aws`, `gcp`, `azure` (Default: `aws`).

### Output Schema (SkillOutput.result)

- `provision_status`: (string) `SUCCESS` or `FAILED`.
- `artifacts_produced`: (array) Paths to the generated `.tf` files.
- `compliance_score`: (float) Validation of HashiCorp style conventions (1.0 = perfect).
- `industrial_status`: (string) "SOLIDIFIED - IAC PROVISIONED".

### ⚖️ Mandato SI (Sistema Internacional)

Cualquier timeout de provisión o latencia límite descrita en la configuración de Terraform (ej. timeouts de lambdas o bases de datos) debe configurarse y documentarse en **segundos** (s). Tamaños de volumen o disco deben referenciarse en **bytes** (B) en la documentación generada.

## 🛡️ Industrial Constraints (Zero-Trust & HashiCorp Style)

- **File Organization:** Code MUST be split across `providers.tf`, `main.tf`, `variables.tf`, and `outputs.tf`. Monolithic `.tf` files are rejected.
- **Surgical Access:** Files MUST only be written to `WORKSPACE/infra/terraform/`.
- **Variable Strictness:** Every variable MUST have a `description` and `type`.
- **Naming Conventions:** Lowercase with underscores (snake_case). Resource names must be singular.
- **Dynamic Blocks:** Use `for_each` over `count` for dynamic resource creation to prevent state-shifting bugs.
- **Secrets Management:** Credentials MUST NOT be hardcoded. Use `sensitive = true` for secret outputs/variables.
