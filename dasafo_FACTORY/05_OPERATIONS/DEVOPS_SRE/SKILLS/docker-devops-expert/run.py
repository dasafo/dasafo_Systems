"""
run.py — Skill: Docker & Container DevOps Expert (DEVOPS_SRE)
Audits Dockerfiles for v3.1 Infra-Aware industrial standards.
v3.1: Infraestructura Blindada | Industrial Scale.
"""

from __future__ import annotations

import re
import sys
from datetime import datetime, timezone
from pathlib import Path

# Add GLOBAL_KNOWLEDGE to path for skill_schema import
sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "00_GLOBAL_KNOWLEDGE"))
from skill_schema import SkillInput, SkillOutput  # noqa: E402


def _find_dockerfiles(root: Path) -> list[Path]:
    return [
        p for p in root.rglob("Dockerfile*")
        if p.is_file() and not any(part.startswith(".") for part in p.parts)
    ]


def _audit_dockerfile(dockerfile: Path) -> dict:
    try:
        content = dockerfile.read_text(encoding="utf-8", errors="ignore")
    except OSError:
        return {"file": str(dockerfile), "error": "Could not read file."}

    issues: list[dict] = []
    lines = content.splitlines()

    # Multi-stage build check
    from_lines = [l.strip() for l in lines if re.match(r"^FROM\s+", l, re.IGNORECASE)]
    if len(from_lines) < 2:
        issues.append({
            "severity": "HIGH",
            "issue": "Missing multi-stage build",
            "detail": "Using multi-stage reduces final image size by up to 90%.",
            "fix": "Separate build stage: FROM node:20 AS builder ... FROM node:20-alpine AS runtime ...",
        })

    # Root user check
    user_lines = [l for l in lines if re.match(r"^USER\s+", l, re.IGNORECASE)]
    if not user_lines:
        issues.append({
            "severity": "CRITICAL",
            "issue": "Running as root (missing USER instruction)",
            "detail": "Never run the application as root inside a container.",
            "fix": "RUN addgroup -S appgroup && adduser -S appuser -G appgroup\nUSER appuser",
        })
    else:
        for ul in user_lines:
            if re.search(r"\broot\b", ul, re.IGNORECASE):
                issues.append({
                    "severity": "CRITICAL",
                    "issue": "Explicit USER root",
                    "detail": "USER root is explicitly defined.",
                    "fix": "Switch to a non-privileged user.",
                })

    # .dockerignore check
    dockerignore = dockerfile.parent / ".dockerignore"
    if not dockerignore.exists():
        issues.append({
            "severity": "MEDIUM",
            "issue": "Missing .dockerignore",
            "detail": "Without .dockerignore, node_modules, .git, and sensitive files are copied to the context.",
            "fix": "Create .dockerignore with: node_modules/, .git/, .env, __pycache__/, *.pyc",
        })

    # Cache invalidation: COPY before installing deps
    copy_lines = [(i, l) for i, l in enumerate(lines) if re.match(r"^COPY", l, re.IGNORECASE)]
    run_lines = [(i, l) for i, l in enumerate(lines) if re.match(r"^RUN", l, re.IGNORECASE)]
    if copy_lines and run_lines:
        first_copy = copy_lines[0][0]
        first_run = run_lines[0][0]
        if first_copy < first_run:
            # Check if they copy everything (.) before installing
            early_copies = [l for i, l in copy_lines if i < first_run and re.search(r"COPY\s+\.\s+", l)]
            if early_copies:
                issues.append({
                    "severity": "MEDIUM",
                    "issue": "COPY . before installing dependencies",
                    "detail": "Invalidates Docker cache with every code change. Copy only package.json/requirements.txt first.",
                    "fix": "COPY package*.json ./\nRUN npm ci --only=production\nCOPY . .",
                })

    # apt-get without cleanup
    for _, line in run_lines:
        if "apt-get install" in line.lower() and "rm -rf /var/lib/apt/lists" not in content:
            issues.append({
                "severity": "MEDIUM",
                "issue": "apt-get without list cleanup",
                "detail": "Package lists add unnecessary layers.",
                "fix": "RUN apt-get update && apt-get install -y pkg && rm -rf /var/lib/apt/lists/*",
            })
            break

    compliance = "PASS" if not any(i["severity"] in ("CRITICAL", "HIGH") for i in issues) else "FAIL"

    return {
        "file": str(dockerfile),
        "from_stages": len(from_lines),
        "issues": issues,
        "compliance": compliance,
    }


def _write_audit_report(report_path: Path, audits: list[dict]) -> None:
    date = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    lines = [
        "# 🐳 Dockerfile Audit Report",
        f"> Generated: {date}",
        f"> Dockerfiles audited: {len(audits)}",
        "",
        "---",
        "",
    ]
    for audit in audits:
        file_name = Path(audit["file"]).name
        status = "✅ PASS" if audit.get("compliance") == "PASS" else "❌ FAIL"
        lines.append(f"## {status} — `{file_name}`")
        lines.append(f"`{audit['file']}`")
        lines.append("")
        if not audit.get("issues"):
            lines.append("No issues found.")
        for issue in audit.get("issues", []):
            sev = issue["severity"]
            icon = "🚨" if sev == "CRITICAL" else "⚠️" if sev == "HIGH" else "💡"
            lines.append(f"### {icon} [{sev}] {issue['issue']}")
            lines.append(f"**Detail:** {issue['detail']}")
            lines.append(f"```dockerfile\n{issue['fix']}\n```")
        lines.append("")

    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text("\n".join(lines), encoding="utf-8")


def run(skill_input: SkillInput) -> SkillOutput:
    agent = skill_input.agent
    skill = skill_input.skill
    cid = skill_input.correlation_id

    target = skill_input.target_project or skill_input.params.get("target")
    if not target:
        return SkillOutput.failure(agent, skill, "TARGET_PROJECT or 'target' param is required.", cid)

    target_path = Path(target)
    if not target_path.exists():
        return SkillOutput.failure(agent, skill, f"Directory '{target}' does not exist.", cid)

    dockerfiles = _find_dockerfiles(target_path)
    if not dockerfiles:
        return SkillOutput(
            success=True,
            agent=agent,
            skill=skill,
            result={"message": "No Dockerfiles found in project.", "dockerfiles_found": 0},
            warnings=["No Dockerfiles to audit."],
            correlation_id=cid,
        )

    audits = [_audit_dockerfile(df) for df in dockerfiles]
    report_path = target_path / "DOCKERFILE_AUDIT.md"
    _write_audit_report(report_path, audits)

    failed = sum(1 for a in audits if a.get("compliance") == "FAIL")
    total_issues = sum(len(a.get("issues", [])) for a in audits)

    return SkillOutput(
        success=True,
        agent=agent,
        skill=skill,
        result={
            "dockerfiles_audited": len(audits),
            "failed": failed,
            "total_issues": total_issues,
            "overall_compliance": "PASS" if failed == 0 else "FAIL",
        },
        artifacts=[str(report_path)],
        warnings=[f"{failed} Dockerfile(s) with CRITICAL/HIGH issues."] if failed > 0 else [],
        correlation_id=cid,
    )
