"""
run.py — Skill: Agentic Thought & Secret Scanner
Agent: SECURITY_AUDITOR
v3.1.5: Solidity Guard | Industrial Scale.

Recursively scans for exposed credential patterns (AI Keys, Secrets, etc.).
"""

from __future__ import annotations
import sys
import re
import os
from pathlib import Path

# Add factory knowledge to path
sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "00_GLOBAL_KNOWLEDGE"))
from skill_schema import SkillInput, SkillOutput

def run_scanner(target_path: Path):
    """Recursively scans for secret patterns."""
    patterns = {
        "OPENAI_KEY": re.compile(r"sk-[a-zA-Z0-9]{48}"),
        "GENERIC_SECRET": re.compile(r"(?i)(password|secret|key|token|credential)[\s:=]+['\"]([a-zA-Z0-9_\-\.]{12,})['\"]"),
        "DOCKER_CREDS": re.compile(r"DOCKER_(?:USER|PASS)=[\s\"']+\S+"),
        "GIT_TOKEN": re.compile(r"ghp_[a-zA-Z0-9]{36}")
    }
    
    findings = []
    
    # Industrial standard: Skip .git and common ignores
    skip_dirs = {".git", "__pycache__", "node_modules", "venv"}
    
    for root, dirs, files in os.walk(target_path):
        dirs[:] = [d for d in dirs if d not in skip_dirs]
        for file in files:
            if file.endswith((".py", ".js", ".env", ".yml", ".json", ".md")):
                file_path = Path(root) / file
                try:
                    content = file_path.read_text(encoding="utf-8")
                    for p_name, p_regex in patterns.items():
                        matches = p_regex.findall(content)
                        if matches:
                            findings.append({
                                "file": str(file_path),
                                "type": p_name,
                                "match_count": len(matches)
                            })
                except Exception:
                    continue
    return findings

def run(skill_input: SkillInput) -> SkillOutput:
    """Standardized entry point for the skill."""
    agent = skill_input.agent
    skill = skill_input.skill
    cid = skill_input.correlation_id

    target = skill_input.params.get("target") or skill_input.target_project or os.environ.get("TARGET_PROJECT")
    
    if not target:
        return SkillOutput.failure(agent, skill, "Mission Blocked: Param 'target' or TARGET_PROJECT env is required.", cid)

    project_path = Path(target).resolve()
    if not project_path.exists():
         return SkillOutput.failure(agent, skill, f"Path Error: {project_path} does not exist.", cid)

    findings = run_scanner(project_path)
    
    result = {
        "status": "PASS" if not findings else "AUDIT_FAIL",
        "findings_count": len(findings),
        "findings": findings,
        "scanned_path": str(project_path)
    }

    return SkillOutput.success(
        agent=agent,
        skill=skill,
        data=result,
        correlation_id=cid
    )
