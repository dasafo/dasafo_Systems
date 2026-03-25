# 🚀 DB Master Bootstrap Protocol
>
> **Step 0:** Database Environment Provisioning

## 📂 Project Integration
1. **Target Identification:** Resolve the `$TARGET_PROJECT` environment variable.
2. **Schema Discovery:** Scan `$TARGET_PROJECT/infrastructure/db/` for existing migrations or SQL scripts.
3. **Supabase Sync:** If present, read the project's Supabase configuration and RLS policies.

## 🔬 Initial Integrity Check
1. **Normalization Audit:** Scan primary tables for redundant data or missing foreign keys.
2. **Index Search:** Identify frequently queried columns missing optimization.
3. **Security Audit:** Verify if critical tables have `RLS` enabled and proper policies.

## 🏁 Milestone M2 Deliverable
The DB Master's contribution is complete when the **Database Schema & RLS Policy** document is produced in `$TARGET_PROJECT/DOCS/Architecture/`.

---
*Bootstrap v2.1 | Status: Solidified.*
