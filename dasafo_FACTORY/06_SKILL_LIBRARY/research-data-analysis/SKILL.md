---
version: 3.2.0-S
agent: DATA_SCIENTIST
---

# 📊 Skill | Research Data Analysis

## Objective
Execute automated Exploratory Data Analysis (EDA) on experimental datasets, ensuring statistical rigor (P-value < 0.05) and absolute compliance with the System International (SI).

## 🛠️ Interface (v3.2.0-S)

### Input Schema (SkillInput.params)
- `dataset_path` (string): Absolute path to the CSV/Parquet file.
- `statistical_test` (string, optional): "IQR" | "Z-score". Default "IQR".

### Output Schema (SkillOutput.result)
- `profile_summary`: (object) Rows, Columns, Missing values.
- `si_compliance_check`: (boolean) True if all units are SI.
- `solidity_score`: (float) (0.0-1.0).

### ⚖️ Mandato SI (Sistema Internacional)
Los reportes de análisis prohíben el uso de unidades no estándar. Todo dato cuantitativo debe normalizarse al SI antes del reporte final.

## Workflow
1.  **Sanitization:** Outlier removal via industrial statistical methods.
2.  **Visualization:** Generation of distribution and heatmap artifacts.
3.  **Persistence:** Export findings to `$TARGET_PROJECT/ANALYSIS/reports/`.
4.  **Lineage:** Mapping of every insight to its raw data source.

---
*Skill v3.2.0-S | Status: Standardized.*
