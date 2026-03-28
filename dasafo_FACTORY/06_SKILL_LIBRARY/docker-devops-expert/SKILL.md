---
version: 3.2.0-S
agent: DEVOPS_SRE
---

# 🐳 Skill | Docker DevOps Expert

## Objective

Optimize, secure, and manage containerized environments to ensure reproducibility across the entire factory.

## 🛠️ Interface (v3.2.0-S)

### Input Schema (SkillInput.params)

- `action` (string, optional): "audit" | "optimize" | "generate". Default "audit".
- `dockerfile_path` (string, optional): Path to the target Dockerfile.

### Output Schema (SkillOutput.result)

- `status`: (string) "PASS" | "FAIL".
- `recommendations`: (list) Security and optimization findings.
- `artifact_path`: (string, optional): Path to the optimized Dockerfile.

### ⚖️ Mandato SI (Sistema Internacional)

Las métricas de construcción (tamaño de la imagen en bytes, tiempo de construcción en segundos, uso de RAM del contenedor) deben reportarse en el SI.

## 🛡️ Industrial Constraints (Zero-Trust)

- **Static Analysis Lock:** This skill performs physical parsing of the `Dockerfile`. It MUST find a physical file on disk to return `success`.
- **User-Security Veto:** Automatically labels any Dockerfile without a non-privileged `USER` as **FAIL** under Zero-Trust protocols.

## Best Practices

- **Builds:** Multi-stage construction to minimize weight.
- **Security:** Rootless execution, no hardcoded secrets (use env/secrets).
- **Optimization:** Minimize layers and clean package manager caches.
- **Orchestration:** Managed FE/BE/DB stacks with isolated networks.

---
*Skill v3.2.0-S | Status: Standardized.*
