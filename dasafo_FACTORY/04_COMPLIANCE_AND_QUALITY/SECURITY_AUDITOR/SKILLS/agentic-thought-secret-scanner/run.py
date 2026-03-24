"""
run.py — Skill: Agentic Thought & Secret Scanner
Agent: SECURITY_AUDITOR

Escanea recursivamente archivos .md y .log en un directorio buscando
patrones de credenciales expuestas. Genera SECRETS_SCAN_REPORT.md.
"""

from __future__ import annotations

import re
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "00_GLOBAL_KNOWLEDGE"))
from skill_schema import SkillInput, SkillOutput  # noqa: E402

# Patrones de detencción de secretos — nunca hardcoded en logs/MDs
_SECRET_PATTERNS: list[tuple[str, re.Pattern]] = [
    ("API_KEY",         re.compile(r"(?i)(api[-_]?key|api[-_]?secret)\s*[=:]\s*['\"]?[\w\-]{16,}", re.IGNORECASE)),
    ("JWT_TOKEN",       re.compile(r"eyJ[a-zA-Z0-9_-]{20,}\.[a-zA-Z0-9_-]{20,}\.[a-zA-Z0-9_-]{20,}")),
    ("AWS_KEY",         re.compile(r"AKIA[0-9A-Z]{16}")),
    ("GENERIC_SECRET",  re.compile(r"(?i)(secret|password|passwd|token|credential)\s*[=:]\s*['\"]?[^\s'\"]{8,}", re.IGNORECASE)),
    ("PRIVATE_KEY",     re.compile(r"-----BEGIN (RSA |EC |OPENSSH )?PRIVATE KEY-----")),
    ("SUPABASE_URL",    re.compile(r"https://[a-z0-9]+\.supabase\.co")),  # solo para catalogar, no es secreto per se
    ("BEARER_TOKEN",    re.compile(r"(?i)bearer\s+[a-zA-Z0-9\-_\.=]{20,}")),
]

_SCAN_EXTENSIONS = {".md", ".log", ".txt", ".env", ".yaml", ".yml", ".json", ".toml"}
_MAX_FILES = 500  # Guardarail: no escanear workspaces masivos sin límite


def _scan_file(file_path: Path) -> list[dict]:
    """Devuelve lista de hallazgos en el archivo."""
    findings: list[dict] = []
    try:
        lines = file_path.read_text(encoding="utf-8", errors="ignore").splitlines()
    except OSError:
        return findings

    for lineno, line in enumerate(lines, 1):
        for pattern_name, pattern in _SECRET_PATTERNS:
            if pattern.search(line):
                # Ofusca la línea antes de loggear para no replicar el secreto
                redacted = re.sub(r"['\"][^'\"]{4}[^'\"]*['\"]", "'[REDACTED]'", line.strip())
                findings.append({
                    "file": str(file_path),
                    "line": lineno,
                    "pattern": pattern_name,
                    "preview": redacted[:120],
                    "severity": "CRITICAL" if pattern_name not in ("SUPABASE_URL",) else "INFO",
                    "action": "ROTATE_AND_REDACT" if pattern_name != "SUPABASE_URL" else "REVIEW",
                })
    return findings


def _write_report(report_path: Path, findings: list[dict], scanned: int) -> None:
    date = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    lines = [
        "# 🔐 Secret Scanner Report",
        f"> Generated: {date}  ",
        f"> Files scanned: {scanned}  ",
        f"> Findings: {len(findings)}",
        "",
        "---",
        "",
    ]
    if not findings:
        lines.append("## ✅ No secrets detected.")
    else:
        critical = [f for f in findings if f["severity"] == "CRITICAL"]
        info = [f for f in findings if f["severity"] == "INFO"]
        lines.append(f"## 🚨 CRITICAL ({len(critical)} findings — ROTATE IMMEDIATELY)")
        for f in critical:
            lines.append(f"- **{f['pattern']}** → `{f['file']}` L{f['line']}")
            lines.append(f"  > `{f['preview']}`")
        lines.append(f"\n## ℹ️ INFO ({len(info)} findings — Review)")
        for f in info:
            lines.append(f"- **{f['pattern']}** → `{f['file']}` L{f['line']}")

    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text("\n".join(lines), encoding="utf-8")


def run(skill_input: SkillInput) -> SkillOutput:
    agent = skill_input.agent
    skill = skill_input.skill
    cid = skill_input.correlation_id

    target = skill_input.params.get("target") or skill_input.target_project
    if not target:
        return SkillOutput.failure(agent, skill, "Param 'target' (directorio a escanear) es requerido.", cid)

    scan_root = Path(target)
    if not scan_root.exists():
        return SkillOutput.failure(agent, skill, f"Directorio '{target}' no existe.", cid)

    # Recolectar archivos a escanear, excluyendo directorios de ruido y el propio reporte
    exclude_dirs = {"node_modules", ".git", "__pycache__", "dist", "build", ".next", ".venv"}
    exclude_files = {"SECRETS_SCAN_REPORT.md"}
    files_to_scan = []
    
    for p in scan_root.rglob("*"):
        if p.is_file() and p.suffix.lower() in _SCAN_EXTENSIONS:
            # Comprueba exclusión por directorio o por nombre de archivo específico
            if not any(part in exclude_dirs for part in p.parts) and p.name not in exclude_files:
                files_to_scan.append(p)
                if len(files_to_scan) >= _MAX_FILES:
                    break

    all_findings: list[dict] = []
    for file_path in files_to_scan:
        all_findings.extend(_scan_file(file_path))

    # Escribir reporte en carpeta estructurada
    report_path = scan_root / "LOGS/reports/SECRETS_SCAN_REPORT.md"
    _write_report(report_path, all_findings, len(files_to_scan))

    critical_count = sum(1 for f in all_findings if f["severity"] == "CRITICAL")

    return SkillOutput(
        success=True,
        agent=agent,
        skill=skill,
        result={
            "files_scanned": len(files_to_scan),
            "total_findings": len(all_findings),
            "critical_findings": critical_count,
            "overall_status": "PASS" if critical_count == 0 else "FAIL",
        },
        artifacts=[str(report_path)],
        warnings=[f"{critical_count} secreto(s) crítico(s) detectado(s). Rotar inmediatamente."] if critical_count > 0 else [],
        correlation_id=cid,
    )
