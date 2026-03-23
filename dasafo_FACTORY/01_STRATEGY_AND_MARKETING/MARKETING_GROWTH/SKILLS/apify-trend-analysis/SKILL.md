# Skill: Apify Trend Analysis
> **Source:** https://skills.sh/apify/agent-skills/apify-trend-analysis
> **Agent:** MARKETING_GROWTH

## Objective
Enable real-time trend scraping across Google, Instagram, TikTok, and YouTube to identify market gaps for dasafodata projects.

## Prerequisite
- `APIFY_TOKEN` must be present in `$TARGET_PROJECT/.env`.
- Use the `mcp-apify` tool or equivalent command line to call actors.

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
