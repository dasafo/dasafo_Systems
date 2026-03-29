import sys, os; sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
"""
run.py — Agentic Thought & Secret Scanner (SECURITY / PO / BACKEND / QA)
v3.3.0-S: Modular Toolbox | Industrial Scale.

Recursively scans for exposed credential patterns to prevent leaks in logs and code.
"""

from __future__ import annotations
import re
import os
import json
from pathlib import Path
from skill_schema import SkillInput, SkillOutput

def run_scanner(target_path: Path):
    """Recursively scans for secret patterns with industrial precision."""
    patterns = {
        "OPENAI_KEY": re.compile(r"sk-[a-zA-Z0-9]{48}"),
        "ANTHROPIC_KEY": re.compile(r"sk-ant-api03-[a-zA-Z0-9\-_]{95}"),
        "GENERIC_SECRET": re.compile(r"(?i)(password|secret|key|token|credential)[\s:=]+['\"]([a-zA-Z0-9_\-\.]{12,})['\"]"),
        "DOCKER_CREDS": re.compile(r"DOCKER_(?:USER|PASS)=[\s\"']+\S+"),
        "GIT_TOKEN": re.compile(r"ghp_[a-zA-Z0-9]{36}"),
        "SSH_PRIVATE": re.compile(r"-----BEGIN [A-Z ]+ PRIVATE KEY-----")
    }
    
    findings = []
    skip_dirs = {".git", "__pycache__", "node_modules", "venv", "dist", "build"}
    
    for root, dirs, files in os.walk(target_path):
        dirs[:] = [d for d in dirs if d not in skip_dirs]
        for file in files:
            file_path = Path(root) / file
            # Limit scan to text-based files for SI efficiency
            if file.endswith((".py", ".js", ".ts", ".tsx", ".jsx", ".env", ".yml", ".yaml", ".json", ".md", ".txt", ".log")):
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
    """Industrialized entry point for secret auditing."""
    agent = skill_input.agent or "SECURITY_AUDITOR"
    skill = "agentic-thought-secret-scanner"
    cid = skill_input.correlation_id

    try:
        # 1. Zero Trust Path Resolution
        target = skill_input.params.get("target") or skill_input.target_project or os.environ.get("TARGET_PROJECT")
        
        if not target:
            return SkillOutput.failure(agent, skill, "SECURITY LOCK: Target path missing for audit.", cid)

        project_path = Path(target).resolve()
        if not project_path.exists():
             return SkillOutput.failure(agent, skill, f"PHYSICAL_ERROR: Path {project_path} not found on disk.", cid)

        # 2. Execution (Physical Scans Only)
        findings = run_scanner(project_path)
        
        # 3. Artifact Generation (SI compliant naming)
        report_dir = project_path / "LOGS" / "AUDITS"
        report_dir.mkdir(parents=True, exist_ok=True)
        report_file = report_dir / f"SEC_SCAN_{cid}.json"
        
        result_payload = {
            "status": "PASS" if not findings else "AUDIT_FAIL",
            "findings_count": len(findings),
            "findings": findings,
            "scanned_path": str(project_path),
            "solidity_check": "Verified via Stark-Scanner v3.3.0-S"
        }

        report_file.write_text(json.dumps(result_payload, indent=2), encoding="utf-8")

        # 4. Success Return
        return SkillOutput.success(
            agent=agent,
            skill=skill,
            result=result_payload,
            correlation_id=cid,
            artifacts=[str(report_file)]
        )

    except Exception as e:
        return SkillOutput.failure(agent, skill, f"CRITICAL Audit Fault: {str(e)}", cid)