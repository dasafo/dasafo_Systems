"""
run.py — Skill: Docker & Container DevOps Expert
Agent: DEVOPS_SRE

Audita Dockerfiles en $TARGET_PROJECT.
Detecta: ausencia de multi-stage builds, ejecución como root, sin .dockerignore, capas innecesarias.
Output: DOCKERFILE_AUDIT.md con recomendaciones accionables.
"""

from __future__ import annotations

import re
import sys
from datetime import datetime, timezone
from pathlib import Path

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
        return {"file": str(dockerfile), "error": "No se pudo leer el archivo."}

    issues: list[dict] = []
    lines = content.splitlines()

    # Multi-stage build check
    from_lines = [l.strip() for l in lines if re.match(r"^FROM\s+", l, re.IGNORECASE)]
    if len(from_lines) < 2:
        issues.append({
            "severity": "HIGH",
            "issue": "Sin multi-stage build",
            "detail": "Usar multi-stage reduce el tamaño de imagen final hasta 90%.",
            "fix": "Separar build stage: FROM node:20 AS builder ... FROM node:20-alpine AS runtime ...",
        })

    # Root user check
    user_lines = [l for l in lines if re.match(r"^USER\s+", l, re.IGNORECASE)]
    if not user_lines:
        issues.append({
            "severity": "CRITICAL",
            "issue": "Ejecución como root (sin USER instruction)",
            "detail": "Nunca ejecutar la aplicación como root dentro de un container.",
            "fix": "RUN addgroup -S appgroup && adduser -S appuser -G appgroup\nUSER appuser",
        })
    else:
        for ul in user_lines:
            if re.search(r"\broot\b", ul, re.IGNORECASE):
                issues.append({
                    "severity": "CRITICAL",
                    "issue": "USER root explícito",
                    "detail": "Se define explícitamente USER root.",
                    "fix": "Cambiar a un usuario no privilegiado.",
                })

    # .dockerignore check
    dockerignore = dockerfile.parent / ".dockerignore"
    if not dockerignore.exists():
        issues.append({
            "severity": "MEDIUM",
            "issue": "Sin .dockerignore",
            "detail": "Sin .dockerignore, node_modules, .git y archivos sensibles se copian al contexto.",
            "fix": "Crear .dockerignore con: node_modules/, .git/, .env, __pycache__/, *.pyc",
        })

    # Cache invalidation: COPY antes de instalar deps
    copy_lines = [(i, l) for i, l in enumerate(lines) if re.match(r"^COPY", l, re.IGNORECASE)]
    run_lines = [(i, l) for i, l in enumerate(lines) if re.match(r"^RUN", l, re.IGNORECASE)]
    if copy_lines and run_lines:
        first_copy = copy_lines[0][0]
        first_run = run_lines[0][0]
        if first_copy < first_run:
            # Busca si copian todo (.) antes de instalar
            early_copies = [l for i, l in copy_lines if i < first_run and re.search(r"COPY\s+\.\s+", l)]
            if early_copies:
                issues.append({
                    "severity": "MEDIUM",
                    "issue": "COPY . antes de instalar dependencias",
                    "detail": "Invalida caché de Docker con cada cambio de código. Copiar solo package.json/requirements.txt primero.",
                    "fix": "COPY package*.json ./\nRUN npm ci --only=production\nCOPY . .",
                })

    # apt-get sin cleanup
    for _, line in run_lines:
        if "apt-get install" in line.lower() and "rm -rf /var/lib/apt/lists" not in content:
            issues.append({
                "severity": "MEDIUM",
                "issue": "apt-get sin limpieza de listas",
                "detail": "Las listas de paquetes añaden capas innecesarias.",
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
        return SkillOutput.failure(agent, skill, "TARGET_PROJECT o param 'target' son requeridos.", cid)

    target_path = Path(target)
    if not target_path.exists():
        return SkillOutput.failure(agent, skill, f"Directorio '{target}' no existe.", cid)

    dockerfiles = _find_dockerfiles(target_path)
    if not dockerfiles:
        return SkillOutput(
            success=True,
            agent=agent,
            skill=skill,
            result={"message": "No se encontraron Dockerfiles en el proyecto.", "dockerfiles_found": 0},
            warnings=["No hay Dockerfiles que auditar."],
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
        warnings=[f"{failed} Dockerfile(s) con issues CRITICAL/HIGH."] if failed > 0 else [],
        correlation_id=cid,
    )
