# 📡 Skill | API Contract Generator
> **Version:** v3.1.5 "Solidity Guard"
> **Source:** https://skills.sh/sickn33/antigravity-awesome-skills/api-documentation-generator (Adapted)
> **Agent:** ARCHITECT

## Objective
Generate strict data contracts (DTOs) and documentation BEFORE logic implementation to decouple Frontend and Backend workers.

## Workflow
1.  **Analyze Demand:** Map the Product Owner's requirements to needed endpoints.
2.  **Generate Contract:** Create a `contract_v1.yaml` using OpenAPI 3.x standards.
3.  **Produce DTO Models:** Generate Pydantic/Zod models based on the contract.
4.  **Publish:** Save to `$TARGET_PROJECT/LOCAL_KNOWLEDGE/architecture/API_CONTRACT.yaml`.

## Rule of Decoupling
Backend and Frontend workers are FORBIDDEN to start coding logic until this contract has a `qa_passed: true` verdict from the Architect.
