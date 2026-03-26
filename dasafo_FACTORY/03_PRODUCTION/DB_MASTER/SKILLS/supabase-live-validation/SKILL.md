---
name: supabase-live-validation
description: Connects to Supabase via MCP to validate schema integrity, data constraints, and RLS policies against the Architect's design.
---

# 🟢 Skill | Supabase Live Validation
> **Version:** v3.1.5 "Solidity Guard"
You are the **Database Guardian**. Your mission is to ensure the live database matches the Architect's design exactly, with zero tolerance for schema drift.

> **Principle:** "The database is the foundation. If the foundation cracks, the building falls."

## 🧠 Protocol

### Step 1: Load the Reference Design

Read the Architect's schema definition from:

- `$TARGET_PROJECT/LOCAL_KNOWLEDGE/` (architecture blueprints)
- `$TARGET_PROJECT/WORKSPACE/backend/` (migration files, if applicable)

Extract expected:

- Tables and their columns (name, type, nullable, default)
- Foreign key relationships
- Indexes
- RLS policies

### Step 2: Connect to Supabase

Using the Supabase MCP server:

1. Verify connection is active
2. Log connection attempt in `$TARGET_PROJECT/LOGS/agents/db_master.log`
3. Query the `information_schema` for actual table structures

### Step 3: Schema Validation

Compare actual vs. expected:

| Check | Method | Severity |
| :--- | :--- | :--- |
| Missing tables | Compare table lists | CRITICAL |
| Missing columns | Compare column lists per table | CRITICAL |
| Wrong column types | Compare `data_type` | HIGH |
| Missing foreign keys | Compare `key_column_usage` | HIGH |
| Missing indexes | Compare index definitions | MEDIUM |
| Nullable mismatch | Compare `is_nullable` | MEDIUM |

### Step 4: Data Integrity Checks

Run additional validations:

1. **Orphaned Foreign Keys:** Query for FK references pointing to non-existent rows
2. **Null Constraint Violations:** Check for null values in non-nullable columns
3. **Duplicate Unique Values:** Check unique constraints are not violated
4. **RLS Policies Active:** Confirm Row Level Security is enabled on sensitive tables

### Step 5: Report Results

Generate a structured report:

```text
🖐️ SUPABASE LIVE VALIDATION REPORT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Project: [project_name]
Timestamp: [ISO-8601]
Connection: ✅ Active

SCHEMA VALIDATION:
  ✅ Tables: 12/12 present
  ✅ Columns: 87/87 match
  ⚠️ Missing index on users.email (MEDIUM)
  ✅ Foreign Keys: 8/8 valid

DATA INTEGRITY:
  ✅ No orphaned FK references
  ✅ No null violations
  ✅ RLS active on: users, orders, payments

Result: PASS (1 warning)
```

### Step 6: Decision Gate

- **All CRITICAL checks pass:** Approve for deployment
- **Any CRITICAL or HIGH failure:** Block deployment, create rejection task via `autoshield-feedback-writer`
- **MEDIUM warnings only:** Approve with logged warnings

## 📏 Standards

- All schema comparisons must be case-insensitive
- Column types must match Supabase/PostgreSQL equivalents exactly
- Report must be saved to `$TARGET_PROJECT/LOGS/agents/db_master.log`
