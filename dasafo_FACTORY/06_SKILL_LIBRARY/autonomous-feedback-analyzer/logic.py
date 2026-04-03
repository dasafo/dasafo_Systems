import os
import json
import time
import re
from pathlib import Path

# Logic based on: https://skills.sh/phuryn/pm-skills/sentiment-analysis

# Keep the persist_to_knowledge_graph function as defined in the original logic.py
# ensuring it uses environment variables for Neo4j credentials.

def execute_feedback_analysis(
    target_project: str,
    agent: str,
    action: str = "analyze_file",
    file_path: str = "LOGS/FEEDBACK-LOG.md",
    raw_text: str = None,
    overwrite: bool = False
) -> tuple[dict, list]:
    """Pure logic for autonomous feedback analysis and LTP sync (v5.0-MCP)."""
    start_time = time.time()
    project_path = Path(target_project).resolve()
    logs_dir = project_path / "LOGS"
    
    # Context pointers resolution
    if action == "analyze_file":
        input_file = project_path / file_path
        if not input_file.exists():
            raise FileNotFoundError(f"Feedback log not found at {input_file}")
        content = input_file.read_text(encoding="utf-8")
    else:
        content = raw_text or ""

    total_bytes_processed = len(content.encode("utf-8"))
    golden_rules_extracted = []
    critical_errors = 0

    # Pattern analysis (as per the original regex logic)
    entries = re.findall(r'(\{.*?\})', content, re.DOTALL)
    for entry_raw in entries:
        try:
            entry = json.loads(entry_raw)
            if "golden_rule" in entry:
                # Basic tech deduction
                tech = "Global"
                f_path = entry.get("context", {}).get("file", "").lower()
                if "shadcn" in f_path: tech = "shadcn"
                elif ".py" in f_path: tech = "fastapi"
                
                golden_rules_extracted.append({
                    "rule": entry["golden_rule"],
                    "tech": tech,
                    "phase": entry.get("context", {}).get("phase", "M3_PRODUCTION")
                })
            if entry.get("severity") in ["critical", "high"]:
                critical_errors += 1
        except: continue

    # LTP Sync (Neo4j)
    from .logic import persist_to_knowledge_graph
    sync_success, sync_msg = persist_to_knowledge_graph(
        golden_rules_extracted, project_path.name, agent
    )

    # DAST Persistence
    report_name = f"ANALYSIS_LTP_{int(time.time())}.json"
    report_path = logs_dir / report_name
    
    analysis_data = {
        "industrial_status": "SOLIDIFIED - FEEDBACK ANALYZED",
        "metrics": {
            "total_rules": len(golden_rules_extracted),
            "payload_bytes": total_bytes_processed
        },
        "ltp_sync": {"success": sync_success, "message": sync_msg}
    }
    
    with open(report_path, 'w', encoding='utf-8') as f:
        json.dump(analysis_data, f, indent=2)

    return analysis_data, [str(report_path)]