---
name: startup-metrics-framework
description: Translates industrial execution metrics (Seconds, Bytes) into SaaS business KPIs (CAC, LTV, ROI). Use this during Phase M1 to formulate the financial success criteria for the PRP_MASTER contract.
---

# 📈 Skill | Startup Metrics Framework (v4.0-MCP)

## Objective

Act as the Financial Engine for the dasafo_Factory. Empower the `PRODUCT_OWNER` to define the business viability of a project by calculating projected Customer Acquisition Cost (CAC), Lifetime Value (LTV), and Cost Per Execution based on the factory's technical capabilities.

## 🛠️ Interface (v4.0-MCP)

### Input Schema (SkillInput.params)

- `target_project` (string, mandatory): Absolute path to the project root.
- `business_model` (string, mandatory): e.g., "B2B SaaS", "B2C Freemium".
- `target_audience` (string, mandatory): Who is the end user?
- `estimated_execution_s` (float, optional): Expected server time per task in seconds.

### Output Schema (SkillOutput.result)

- `financial_kpis`: (object) Contains calculated/projected metrics (CAC, LTV, Target ROI).
- `prp_injection_payload`: (string) The exact formatted text to inject into the `03_success_criteria` of the PRP_MASTER.
- `execution_time_s`: (float) Execution time of the calculation.

## 🧠 Industrial Constraints & Best Practices

- **SI to Financial Mapping:** Always anchor financial costs to SI units (e.g., 1 Second of compute = $X cost).
- **LTV/CAC Ratio:** Enforce a minimum 3:1 LTV to CAC ratio for the project to be considered viable.
- **Evidence-Based:** Do not hallucinate numbers wildly. Provide realistic baseline estimates for cloud infrastructure (AWS/Supabase) based on the inputs.

## 🚀 Execution Guide

1. Receive the initial project idea and business model.
2. Execute this skill to generate the financial baselines.
3. Once the `financial_kpis` are returned, inject the `prp_injection_payload` directly into the `03_success_criteria` of the `PRP_MASTER.json`.
