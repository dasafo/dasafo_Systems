# Skill: Strategic Database Architect
> **Source:** https://skills.sh/sickn33/antigravity-awesome-skills/database-architect
> **Agent:** DB_MASTER

## Objective
Provide high-level architecture decisions for data storage, consistency, and scalability across the factory.

## Tactical Decisions
- **Normalization vs Denormalization:** Only denormalize for performance reasons documented with benchmarks.
- **Storage Strategy:** Choose between Relational (PG), Vector (Supabase Vector), or Document (JSONB) based on data access patterns.
- **Disaster Recovery:** Every schema must include a plan for backups, point-in-time recovery (PITR), and high availability.

## Alignment
The DB_MASTER must sync with the ARCHITECT to ensure the Database Schema matches the API DTOs 1:1.
