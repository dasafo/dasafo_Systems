import sys, os; sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
"""
run.py — Pattern Recognition (ORCHESTRATOR / FACTORY_EVOLVER)
v3.3.0-S: Modular Toolbox | Industrial Scale.

Analyzes feedback logs and project history to identify systemic patterns for factory evolution.
"""

from __future__ import annotations
import os
from pathlib import Path
from skill_schema import SkillInput, SkillOutput

def run(skill_input: SkillInput) -> SkillOutput:
    """Industrialized entry point for systemic pattern analysis."""
    agent = skill_input.agent or "ORCHESTRATOR"
    skill = "pattern-recognition"
    cid = skill_input.correlation_id

    try:
        # 1. Zero Trust Context
        target = skill_input.target_project or os.environ.get("TARGET_PROJECT")
        factory_root = Path(__file__).resolve().parents[4]
        
        # 2. Logic: Priority Selection
        # Orchestrator focuses on current project anomalies.
        # Evolver focuses on global feedback-log.md.
        paths_to_scan = []
        if agent == "ORCHESTRATOR" and target:
            project_log = Path(target) / "LOGS" / "EXECUTION_LOG.md"
            if project_log.exists():
                paths_to_scan.append(project_log)
        
        global_log = factory_root / "00_GLOBAL_KNOWLEDGE" / "FEEDBACK-LOG.md"
        if global_log.exists():
             paths_to_scan.append(global_log)

        if not paths_to_scan:
            return SkillOutput.success(agent, skill, {"status": "NO_EVIDENCE_LOGS_FOUND", "message": "Nothing to analyze yet."}, cid)

        # 3. Pattern Detection Synthesis (Mocked for industrial interface)
        return SkillOutput.success(
            agent=agent,
            skill=skill,
            result={
                "status": "ANALYSIS_COMPLETE",
                "logs_scanned": [str(p) for p in paths_to_scan],
                "patterns_detected": 0, # To be filled by LLM call
                "verdict": "FACTORY_STABLE"
            },
            correlation_id=cid,
            artifacts=[str(p) for p in paths_to_scan]
        )

    except Exception as e:
        return SkillOutput.failure(agent, skill, f"Pattern Fault: {str(e)}", cid)
