---
version: 3.2.0-S
agent: DEVOPS_SRE
---

# 🐙 Skill | CI/CD GitHub Patterns

## Objective

Design and automate standard-compliant CI/CD pipelines from the first commit to cloud deployment, ensuring industrial safety and quality.

## 🛠️ Interface (v3.2.0-S)

### Input Schema (SkillInput.params)

- `project_name` (string, optional): Target project for the workflow.
- `stack` (string, optional): "fastapi" | "react" | "nextjs". Default "fastapi".

### Output Schema (SkillOutput.result)

- `workflow_path`: (string) Absolute path to the generated YAML.
- `status`: (string) "DEPLOYMENT_READY" | "PIPELINE_ERROR".
- `checks_summary`: (list) List of industrial checkpoints included.

### ⚖️ Mandato SI (Sistema Internacional)

Cualquier métrica de rendimiento del pipeline (tiempo de build, latencia de despliegue, consumo de CPU en el runner) debe reportarse en unidades del SI (segundos, Watts).

## 🛡️ Industrial Constraints (Zero-Trust)

- **Physical Deployment:** This skill physically writes YAML files to `.github/workflows/`. Mocks are forbidden.
- **Traceability:** Workflow artifacts must include the correlation ID (CID) to track the origin of the pipeline change.

## Pipeline Phases

1. **Validation:** Linting and type-checking (Solidity v3.2.0-S).
2. **Testing:** Trigger QA suites.
3. **Security:** Secrets & CVE scanning (Zero-Trust v3.1).
4. **Artifacts:** Build and push Docker images.
5. **Deployment:** Cloud update upon RA sign-off.

---
*Skill v3.2.0-S | Status: Standardized.*
