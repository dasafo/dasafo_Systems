"""
run.py — Skill: Agentic Thought & Secret Scanner (SECURITY_AUDITOR)
v3.2.0-S: Modular Toolbox | Industrial Scale.

Recursively scans for exposed credential patterns (AI Keys, Secrets, etc.).
"""

from __future__ import annotations
import re
import os
import json
from pathlib import Path
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
    agent = "SECURITY_AUDITOR"
    skill = "agentic-thought-secret-scanner"
    cid = skill_input.correlation_id

    try:
        # 1. Path Resolution
        target = skill_input.params.get("target") or skill_input.target_project or os.environ.get("TARGET_PROJECT")
        
        if not target:
            return SkillOutput.failure(agent, skill, "Mission Blocked: TARGET_PROJECT is missing.", cid)

        project_path = Path(target).resolve()
        if not project_path.exists():
             return SkillOutput.failure(agent, skill, f"Path Error: {project_path} does not exist.", cid)

        # 2. Execution
        findings = run_scanner(project_path)
        
        # 3. Artifact Generation (Industrial Traceability)
        report_dir = project_path / "LOGS" / "reports"
        report_dir.mkdir(parents=True, exist_ok=True)
        report_file = report_dir / f"security_audit_{cid}.json"
        
        result_payload = {
            "status": "PASS" if not findings else "AUDIT_FAIL",
            "findings_count": len(findings),
            "findings": findings,
            "scanned_path": str(project_path)
        }

        with open(report_file, "w", encoding="utf-8") as f:
            json.dump(result_payload, f, indent=2)

        # 4. Success Return
        return SkillOutput.success(
            agent=agent,
            skill=skill,
            result=result_payload,
            correlation_id=cid,
            artifacts=[str(report_file)]
        )

    except Exception as e:
        return SkillOutput.failure(agent, skill, f"Critical Audit Failure: {str(e)}", cid)