# 📊 Skill | Research Data Analysis
> **Version:** v3.1.5 "Solidity Guard"
> **Agent:** DATA_SCIENTIST

## Objective
Perform deep exploratory data analysis (EDA) on experimental datasets with a focus on statistical integrity and SI metric compliance.

## Key Constraints
- **SI Units Only:** No non-standard units allowed in analysis reports.
- **Statistical Significance:** All correlations must be backed by a P-value < 0.05.
- **Data Lineage:** Document the source of every dataset used in the analysis.

## Workflow
1. **Sanitize:** Remove outliers using the IQR method.
2. **Visualize:** Generate distributions and correlation heatmaps.
3. **Report:** Export results to `$TARGET_PROJECT/ANALYSIS/research_reports/`.

---
*Skill v3.1.5 | Status: Solidified.*
