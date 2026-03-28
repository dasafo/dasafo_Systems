import sys, os; sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
"""
run.py — AutoShield Pattern Analysis (FACTORY_EVOLVER)
v3.2.0-S: Modular Toolbox | Industrial Scale.

Analyzes the FEEDBACK-LOG.md to identify recurring failure patterns and propose evolutions.
"""

from __future__ import annotations
import os
import re
from pathlib import Path
from datetime import datetime
from collections import Counter
from skill_schema import SkillInput, SkillOutput

def run(skill_input: SkillInput) -> SkillOutput:
    """Industrialized entry point: Physics-based Pattern Analysis."""
    agent = "FACTORY_EVOLVER"
    skill = "autoshield-pattern-analysis"
    cid = skill_input.correlation_id

    try:
        # 1. Path Resolution
        factory_root = Path(__file__).resolve().parents[4]
        feedback_log = factory_root / "FEEDBACK-LOG.md"
        
        if not feedback_log.exists():
            feedback_log = factory_root / "dasafo_FACTORY" / "FEEDBACK-LOG.md"

        if not feedback_log.exists():
             return SkillOutput.failure(agent, skill, "FEEDBACK-LOG.md not found.", cid)

        # 2. Logic (Physical Parsing)
        content = feedback_log.read_text(encoding="utf-8")
        
        # Regex to match errors
        pattern = re.compile(r"### \[(?P<id>FB-\d+|FB-NEW)\]")
        matches = pattern.findall(content)
        total_entries = len(matches)
        
        # Score penalty: 2 points per error occurrence detected.
        base_score = 100
        health_score = max(0, base_score - (total_entries * 2))
        
        # Identify hotspots: we look for affected_agents count
        agent_pattern = re.compile(r"affected_agents:\s*\[\"?(.*?)\"?\]")
        agent_matches = agent_pattern.findall(content)
        agent_counter = Counter(agent_matches)
        top_hotspots = [f"{agent} ({count} entries)" for agent, count in agent_counter.most_common(3)]
        
        report = f"📊 AUTOSHIELD ANTIFRAGILITY REPORT (v3.2.0-S)\n"
        report += "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        report += f"Period: {datetime.now().isoformat()}Z\n"
        report += f"Total Entries Analysed: {total_entries}\n"
        report += f"Physical Health Score: {health_score}/100\n\n"
        
        report += "🔥 TOP HOTSPOTS (Affected Agents):\n"
        if top_hotspots:
            for i, hs in enumerate(top_hotspots, 1):
                report += f"  {i}. {hs}\n"
        else:
            report += "  None detected.\n"
            
        report += "\n🛡️ PROPOSED EVOLUTIONS:\n"
        report += "  - [DEPENDING ON LOG] Factory Evolver must self-correct these agents.\n"
        report += "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"

        # 3. Artifact Generation
        report_dir = factory_root / "LOGS" / "analysis"
        report_dir.mkdir(parents=True, exist_ok=True)
        report_file = report_dir / f"antifragility_{cid}.txt"
        report_file.write_text(report, encoding="utf-8")

        return SkillOutput.success(
            agent=agent,
            skill=skill,
            result={
                "health_score": health_score,
                "total_entries": total_entries,
                "hotspots": [k for k,v in agent_counter.most_common(3)],
                "report": report,
                "industrial_verification": True
            },
            correlation_id=cid,
            artifacts=[str(report_file)]
        )

    except Exception as e:
        return SkillOutput.failure(agent, skill, f"Pattern Analysis Failed: {str(e)}", cid)
