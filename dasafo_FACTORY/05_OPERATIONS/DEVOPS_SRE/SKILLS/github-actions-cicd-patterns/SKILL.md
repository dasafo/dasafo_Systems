# Skill: GitHub Actions CI/CD Patterns
> **Source:** https://skills.sh/diegocv/github-actions
> **Agent:** DEVOPS_SRE

## Objective
Design and automate the CI/CD pipeline from code submission to cloud deployment.

## Pipeline Phases
1.  **Validation:** Run `lint` and `type-check`.
2.  **Testing:** Execute the `QA_TESTER` suites (Unit/Integration).
3.  **Security:** Trigger a `SECURITY_AUDITOR` scan for secrets and CVEs.
4.  **Artifact Creation:** Build and push Docker images to Registry.
5.  **Deployment:** Update the cloud infrastructure (GCP/AWS/Azure) upon successful RA-approval.

## Monitoring
Integrate status checks in GitHub to block pull requests failing the "Safety Threshold".
