# Skill: Docker & Container DevOps Expert
> **Source:** https://skills.sh/alinaqi/claude-bootstrap/docker
> **Agent:** DEVOPS_SRE

## Objective
Optimize, secure, and manage containerized environments for the entire factory.

## Core Best Practices
- **Multi-stage Builds:** Reduce image size by separating build and runtime environments.
- **Rootless Execution:** Never run applications as root inside a container.
- **Layer Optimization:** Minimize the number of layers and clean up caches after package installation.
- **Docker Compose Orchestration:** Manage multi-service stacks (FE, BE, DB) with shared networks and secrets.

## Workflow
1.  **Audit:** Scan existing Dockerfiles for insecurity/inefficiency.
2.  **Optimize:** Implement caching strategies for `node_modules` and `pip` packages.
3.  **Deploy:** Ensure local development matches the production image 1:1.
