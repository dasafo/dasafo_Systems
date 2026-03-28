import sys, os; sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
"""
run.py — ML Experiment Tracker (DATA_SCIENTIST)
v3.2.0-S: Modular Toolbox | Industrial Scale.

Maintains an immutable record of machine learning experiments.
"""

from __future__ import annotations
import os
import json
from pathlib import Path
from datetime import datetime
from skill_schema import SkillInput, SkillOutput

def run(skill_input: SkillInput) -> SkillOutput:
    """Standardized entry point for the skill."""
    agent = "DATA_SCIENTIST"
    skill = "ml-experiment-log"
    cid = skill_input.correlation_id

    try:
        # 1. Resolve Path
        target = skill_input.target_project or os.environ.get("TARGET_PROJECT")
        if not target:
             return SkillOutput.failure(agent, skill, "Missing TARGET_PROJECT", cid)
        
        project_path = Path(target).resolve()
        log_file = project_path / "LOGS" / "ML_EXPERIMENT_LOG.md"
        
        # 2. Logic (Log Appending)
        exp_data = skill_input.params.get("experiment_data", {})
        model_id = skill_input.params.get("model_id", "v1.0")
        
        entry = f"""
### 🧪 Experiment | {datetime.now().isoformat()}
- **Model ID:** {model_id}
- **CID:** {cid}
- **Metrics:** {json.dumps(exp_data)}
---
"""
        log_file.parent.mkdir(parents=True, exist_ok=True)
        if not log_file.exists():
            log_file.write_text("# 📊 ML Experiment Log (v3.2.0-S)\n\n", encoding="utf-8")
        
        with open(log_file, "a", encoding="utf-8") as f:
            f.write(entry)

        return SkillOutput.success(
            agent=agent,
            skill=skill,
            result={
                "log_path": str(log_file),
                "status": "REPRODUCIBLE"
            },
            correlation_id=cid,
            artifacts=[str(log_file)]
        )

    except Exception as e:
        return SkillOutput.failure(agent, skill, f"ML Tracking Failed: {str(e)}", cid)
