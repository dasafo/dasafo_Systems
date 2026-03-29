from __future__ import annotations
import sys, os; sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
"""
run.py — Agentic Thought & Secret Scanner (Credential Scanner) - SECURITY / PO / BACKEND / QA
v3.3.0-S: Modular Toolbox | Industrial Scale.

Advanced credential scanner that masks secrets, checks .gitignore, and provides actionable remediation steps.
Based on useai-pro/openclaw-skills-security/credential-scanner logic.
"""

import re
import os
import json
import time
from pathlib import Path
from skill_schema import SkillInput, SkillOutput

def get_patterns() -> dict[str, re.Pattern]:
    """Returns a compiled dictionary of sensitive credential patterns."""
    return {
        "AWS Access Key": re.compile(r"AKIA[0-9A-Z]{16}"),
        "OpenAI API Key": re.compile(r"sk-[a-zA-Z0-9]{48}"),
        "Anthropic API Key": re.compile(r"sk-ant-[a-zA-Z0-9-]{80,}"),
        "GitHub Personal Token": re.compile(r"gh[po]_[a-zA-Z0-9]{36}"),
        "GitLab Personal Token": re.compile(r"glpat-[a-zA-Z0-9-_]{20}"),
        "Slack Bot Token": re.compile(r"xoxb-[0-9]{10,}-[a-zA-Z0-9]{24}"),
        "SendGrid API Key": re.compile(r"SG\.[a-zA-Z0-9-_]{22}\.[a-zA-Z0-9-_]{43}"),
        "Private Key": re.compile(r"-----BEGIN (RSA |EC |DSA |OPENSSH )?PRIVATE KEY-----|-----BEGIN PGP PRIVATE KEY BLOCK-----"),
        "Database URL with Credentials": re.compile(r"(postgres|mysql|mongodb)://[^\s'\"]+:[^\s'\"]+@"),
        "Generic Secret": re.compile(r"(?i)(password|secret|token|api_key|apikey)\s*[:=]\s*['\"]([^ \s'\"]{8,})['\"]")
    }

def mask_secret(value: str) -> str:
    """Masks secret values, showing only prefix and suffix if applicable."""
    if len(value) <= 12:
        return "████████"
    return f"{value[:8]}...████████"

def is_ignored(file_path: Path, gitignore_lines: list[str], project_root: Path) -> bool:
    """Checks if a file is likely to be ignored based on simple gitignore patterns."""
    try:
        relative_path = str(file_path.relative_to(project_root))
    except ValueError:
        return False
        
    for line in gitignore_lines:
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if line.endswith("/"):
            if relative_path.startswith(line.rstrip("/")):
                return True
        elif line in relative_path:
            return True
    return False

def scan_project(project_path: Path, gitignore_lines: list[str], network_preflight: bool = False) -> list[dict]:
    """Recursively scans for secret patterns with industrial-grade rules."""
    patterns = get_patterns()
    findings = []
    
    skip_dirs = {"node_modules", "vendor", ".git", "dist", "build", "__pycache__"}
    skip_files = {"package-lock.json", "yarn.lock", "pnpm-lock.yaml"}
    text_extensions = {".py", ".js", ".ts", ".tsx", ".jsx", ".env", ".yml", ".yaml", ".json", ".md", ".txt", ".log", ".config", ".settings"}
    
    for root, dirs, files in os.walk(project_path):
        dirs[:] = [d for d in dirs if d not in skip_dirs]
        for file in files:
            if file in skip_files:
                continue
                
            file_path = Path(root) / file
            
            # Simple heuristic for binary files
            if not any(file.lower().endswith(ext) for ext in text_extensions) and not file.startswith(".env"):
                 continue

            try:
                content = file_path.read_text(encoding="utf-8")
                lines = content.splitlines()
                
                ignored = is_ignored(file_path, gitignore_lines, project_path)
                
                for p_name, p_regex in patterns.items():
                    for line_num, line_content in enumerate(lines, 1):
                        matches = p_regex.finditer(line_content)
                        for m in matches:
                            full_match = m.group(0)
                            
                            # Severity Logic
                            severity = "CRITICAL"
                            if network_preflight:
                                severity = "CRITICAL"
                            elif ignored and ".env" in file_path.name:
                                severity = "WARNING"
                            elif not ignored:
                                severity = "CRITICAL"
                            
                            # Action Suggestion
                            action = "Rotate any exposed keys immediately."
                            if ".env" in file_path.name:
                                action += " Add .env to .gitignore and move to a secret manager."
                            elif "src" in str(file_path):
                                action = "Use environment variables or a secret vault instead of hardcoding."
                            
                            findings.append({
                                "file": str(file_path.relative_to(project_path)),
                                "line": line_num,
                                "type": p_name,
                                "severity": severity,
                                "value_masked": mask_secret(full_match),
                                "action": action
                            })
                            
            except Exception:
                continue
                
    return findings

def run(skill_input: SkillInput) -> SkillOutput:
    """Industrial Entry point for Credential Audit."""
    agent = skill_input.agent or "SECURITY_AUDITOR"
    skill = "agentic-thought-secret-scanner"
    cid = skill_input.correlation_id
    params = skill_input.params or {}
    
    start_time = time.time()

    try:
        # 1. Path Resolution
        target = params.get("target") or skill_input.target_project or os.environ.get("TARGET_PROJECT")
        if not target:
            return SkillOutput.failure(agent, skill, "SECURITY LOCK: Target path missing for audit.", cid)

        project_path = Path(target).resolve()
        if not project_path.exists():
             return SkillOutput.failure(agent, skill, f"PHYSICAL_ERROR: Path {project_path} not found on disk.", cid)

        # 2. Gitignore Context
        gitignore_lines = []
        gitignore_path = project_path / ".gitignore"
        if gitignore_path.exists():
            gitignore_lines = gitignore_path.read_text(encoding="utf-8").splitlines()

        # 3. Execution
        network_preflight = params.get("network_preflight", False)
        findings = scan_project(project_path, gitignore_lines, network_preflight)
        
        # 4. Global Analysis
        secrets_found = len(findings)
        files_count = 0
        for root, _, files in os.walk(project_path):
            files_count += len(files)
            
        # 5. Result Payload (SI Compliant metrics)
        execution_time_s = time.time() - start_time
        
        result_payload = {
            "status": "PASS" if not findings else "AUDIT_FAIL",
            "summary": {
                "files_scanned": files_count,
                "secrets_found": secrets_found,
                "scan_duration_s": round(execution_time_s, 4)
            },
            "findings": findings,
            "recommendations": [
                "Always add .env to .gitignore.",
                "Rotate any keys that were flagged as CRITICAL.",
                "Use a Secret Manager (e.g. 1Password CLI, Doppler) for CI/CD.",
                "Check .env.example for accidental production values."
            ]
        }

        # 6. Physical Artifact Generation
        report_dir = project_path / "LOGS" / "AUDITS"
        report_dir.mkdir(parents=True, exist_ok=True)
        report_file = report_dir / f"SEC_SCAN_{cid}.json"
        report_file.write_text(json.dumps(result_payload, indent=2, ensure_ascii=False), encoding="utf-8")

        # 7. Success Return
        return SkillOutput.success(
            agent=agent,
            skill=skill,
            result=result_payload,
            correlation_id=cid,
            artifacts=[str(report_file)]
        )

    except Exception as e:
        return SkillOutput.failure(agent, skill, f"CRITICAL Audit Fault: {str(e)}", cid)