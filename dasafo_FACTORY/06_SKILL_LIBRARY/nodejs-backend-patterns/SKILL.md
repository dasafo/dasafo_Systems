---
name: nodejs-backend-patterns
description: Enforces industrial-grade Node.js/TypeScript design patterns (Repository, DTOs, Service Layer) and TDD. Use this skill when generating or refactoring backend logic in a Node.js environment to ensure architectural purity.
---

# ⚙️ Skill | Node.js Backend Patterns (v4.0-MCP)

## Objective

Act as the Node.js Architectural Enforcer for the dasafo_Factory. Ensure that all TypeScript/JavaScript backend code adheres to strict separation of concerns, utilizing DTOs (Data Transfer Objects) for input validation and Repository patterns for data access.

## 🛠️ Interface (v4.0-MCP)

### Input Schema (SkillInput.params)

- `target_project` (string, mandatory): Absolute path to the project root.
- `module_name` (string, mandatory): The domain module being built (e.g., `Users`, `Payments`).

### Output Schema (SkillOutput.result)

- `is_node_environment`: (boolean) Confirms physical presence of package.json.
- `scaffold_paths`: (object) Recommended paths for the Controller, Service, and Repository.
- `testing_mandate`: (string) Instructions for the accompanying Jest/Mocha test files.

## 🧠 Industrial Constraints & Best Practices

- **Layered Architecture:** Always separate routing (Controllers) from business logic (Services) and database queries (Repositories).
- **TypeScript First:** Strongly type all responses and external inputs using interfaces or DTO classes.
- **Test-Driven Delivery:** For every `[module].service.ts` created, you MUST concurrently create a `[module].service.test.ts` to satisfy the factory's QA phase.
- **Physical Containment:** Strictly write all files within `WORKSPACE/backend/`. Never create an `src/` folder in the project root.

## 🚀 Execution Guide

1. Receive the target module requirement from the `SPEC_LITE.json`.
2. Run this skill to physically verify the Node.js environment and obtain the approved file path structure.
3. Once verified, generate the logic adhering to the provided layered architecture paths.
