# Skill: Infrastructure as Code (Terraform Pro)
> **Source:** https://terraform.io/ (Adapted)
> **Agent:** DEVOPS_SRE

## Objective
Manage cloud infrastructure through declarative, version-controlled code.

## Key Protocols
- **State Management:** Use remote backends with locking to avoid state corruption.
- **Modular Design:** Group resources (DB, VPC, Cluster) into reusable Terraform modules.
- **Drift Detection:** Periodically run `terraform plan` to ensure the cloud matches the code.
- **Cost Optimization:** Tag resources for cost tracking and destroy temporary environments after use.

## Dependency
Must sync with the ARCHITECT to ensure Infrastructure meets the throughput requirements of the project.
