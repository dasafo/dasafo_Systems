import sys, os; sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
"""
run.py — MCP Capabilities Architect (RESEARCH_AGENT)
v3.2.0-S: Modular Toolbox | Industrial Scale.

Proposes new agentic capabilities via the Model Context Protocol.
"""

from __future__ import annotations
import os
from pathlib import Path
from skill_schema import SkillInput, SkillOutput

def run(skill_input: SkillInput) -> SkillOutput:
    """Standardized entry point for the skill."""
    agent = "RESEARCH_AGENT"
    skill = "mcp-capabilities-architect"
    cid = skill_input.correlation_id

    try:
        # 1. Resolve Path
        target = skill_input.target_project or os.environ.get("TARGET_PROJECT")
        if not target:
             return SkillOutput.failure(agent, skill, "Missing TARGET_PROJECT", cid)
        
        project_path = Path(target).resolve()
        tool_need = skill_input.params.get("tool_need", "Generic Data API")
        
        # 2. Logic (Proposal Generation)
        proposal = f"""# 📑 NEW MCP PROPOSAL | {tool_need}
Architecture Standard: v3.2.0-S
Objective: Enable autonomous access to {tool_need}.

Resources:
  - GET /v1/industrial-data/{{id}}
Tools:
  - query_{tool_need.lower().replace(" ", "_")}
"""
        proposal_dir = project_path / "LOCAL_KNOWLEDGE" / "proposals"
        proposal_dir.mkdir(parents=True, exist_ok=True)
        proposal_file = proposal_dir / f"mcp_proposal_{cid}.md"
        proposal_file.write_text(proposal, encoding="utf-8")

        return SkillOutput.success(
            agent=agent,
            skill=skill,
            result={
                "proposal_path": str(proposal_file),
                "status": "PROPOSED",
                "vibe_check": "SCALABLE"
            },
            correlation_id=cid,
            artifacts=[str(proposal_file)]
        )

    except Exception as e:
        return SkillOutput.failure(agent, skill, f"MCP Architect Failure: {str(e)}", cid)
