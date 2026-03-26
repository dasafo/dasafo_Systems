# ⚡ Skill | Supabase Stack Expert
> **Version:** v3.1.5 "Solidity Guard"
> **Agent:** DB_MASTER

## Objective
Design and manage a full-stack database ecosystem using Supabase, including Auth, RLS, and Migrations.

## Core Commitments
- **RLS Mandatory:** Never create a table without Row Level Security (RLS) policies.
- **Migration-Driven:** Use the Supabase CLI to generate and apply migrations. Every change must be in a file.
- **Auth Integration:** Connect application logic directly to `auth.users` for secure multi-tenancy.

## Workflow
1.  **Initialize:** `supabase init` -> Link to remote project.
2.  **Schema Design:** Write SQL migrations in `supabase/migrations/`.
3.  **Local Stack:** Test all RLS policies locally using Docker before pushing to production.
