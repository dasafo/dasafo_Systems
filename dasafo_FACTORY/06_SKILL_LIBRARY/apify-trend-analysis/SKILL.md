---
version: 3.2.0-S
agent: MARKETING_GROWTH
---

# 📈 Skill | Apify Trend Analysis

## Objective
Enable real-time trend scraping across Google, Instagram, TikTok, and YouTube to identify market gaps for dasafo_FACTORY projects.

## 🛠️ Interface (v3.2.0-S)

### Input Schema (SkillInput.params)
- `actor` (string): The Apify actor to run (e.g., "apify/google-trends-scraper").
- `keywords` (list of strings): List of keywords or hashtags to analyze.
- `location` (string, optional): Location code for trends.

### Output Schema (SkillOutput.result)
- `status`: (string) "SUCCESS" | "FAILED"
- `data_points_count`: (integer) Total data points found.
- `insights`: (string) Summary of identified trends.
- `file`: (string) Path to the saved raw results.

### ⚖️ Mandato SI (Sistema Internacional)
Cualquier métrica temporal (intervalos de tendencia) o de tamaño de datos debe expresarse en el Sistema Internacional de Unidades.

## Workflow

### 1. Identify Trend Type
Select the correct actor based on research needs:
- `apify/google-trends-scraper`
- `apify/instagram-hashtag-scraper`
- `clockworks/tiktok-trends-scraper`
- `streamers/youtube-shorts-scraper`

### 2. Execution Logic
1.  **Fetch Schema:** Get the actor's input schema dynamically.
2.  **Define Scope:** Set keywords, hashtags, or locations.
3.  **Run:** Execute the actor and save results in `$TARGET_PROJECT/LOCAL_KNOWLEDGE/trends/YYYY-MM-DD_[actor].json`.

### 3. Insights Extraction
After completion, report:
- Total data points found.
- Key trend insights for the specific niche.
- **Actionable Step:** Propose a content piece or a feature based on the data.

---
*Skill v3.2.0-S | Status: Standardized.*
