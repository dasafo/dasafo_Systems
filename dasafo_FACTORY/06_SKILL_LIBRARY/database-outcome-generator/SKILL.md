---
name: database-initiation
description: Use this skill whenever you need to architect and provision a database schema. This triggers the fully integrated database outcome generator that combines strategic schema planning, Supabase optimizations, Indexing strategy, and physical script generation in a single atomic tool call.
compatibility: Postgres, Supabase, SQLAlchemy
---
<!-- LEVEL_1_END -->



# Database Outcome Generator

This is a **Macro Skill (Outcome)** that performs the end-to-end database provisioning in a single invocation, significantly reducing token churn and latency.

Instead of writing SQL incrementally or making multiple calls, the agent uses the `database-initiation` tool to generate the definitive schema and optimization report. 

## Requirements
When triggering this skill, provide the following parameters:
- `target_project` (string): Path to the project root.
- `agent` (string): e.g. "BACKEND_DEV".
- `resource_entity` (string): The main entity or context for the schema (e.g. "users", "ecommerce_full", "video_processing").

## Internal Mechanics
1. Resolves the hybrid infrastructure (Shared VS Isolated).
2. Generates the strategic JSON schema definition for the entity.
3. Automatically applies Supabase best practices (RLS, concurrent indexes).
4. Persists the artifacts in `INFRASTRUCTURE/DATABASE/`.
5. Returns a unified validation payload containing both the schema and the optimization report.
