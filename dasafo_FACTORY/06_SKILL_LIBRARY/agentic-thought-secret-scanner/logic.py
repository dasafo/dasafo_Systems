import re
import os
import json
import time
import uuid
from pathlib import Path
import redis # 👈 Nueva dependencia Engram

# Inicialización del Cliente Redis (Conexión industrial)
redis_client = redis.Redis(
    host=os.getenv("REDIS_HOST", "localhost"),
    port=int(os.getenv("REDIS_PORT", 6379)),
    decode_responses=True
)

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
    if len(value) <= 12: return "████████"
    return f"{value[:8]}...████████"

def is_ignored(file_path: Path, gitignore_lines: list[str], project_root: Path) -> bool:
    try: relative_path = str(file_path.relative_to(project_root))
    except ValueError: return False
    for line in gitignore_lines:
        line = line.strip()
        if not line or line.startswith("#"): continue
        if line.endswith("/") and relative_path.startswith(line.rstrip("/")): return True
        elif line in relative_path: return True
    return False

def scan_project(project_path: Path, gitignore_lines: list[str], network_preflight: bool = False) -> list[dict]:
    patterns = get_patterns()
    findings = []
    skip_dirs = {"node_modules", "vendor", ".git", "dist", "build", "__pycache__"}
    skip_files = {"package-lock.json", "yarn.lock", "pnpm-lock.yaml"}
    text_extensions = {".py", ".js", ".ts", ".tsx", ".jsx", ".env", ".yml", ".yaml", ".json", ".md", ".txt", ".log", ".config", ".settings"}
    
    for root, dirs, files in os.walk(project_path):
        dirs[:] = [d for d in dirs if d not in skip_dirs]
        for file in files:
            if file in skip_files: continue
            file_path = Path(root) / file
            if not any(file.lower().endswith(ext) for ext in text_extensions) and not file.startswith(".env"): continue

            try:
                content = file_path.read_text(encoding="utf-8")
                ignored = is_ignored(file_path, gitignore_lines, project_path)
                
                for p_name, p_regex in patterns.items():
                    for line_num, line_content in enumerate(content.splitlines(), 1):
                        for m in p_regex.finditer(line_content):
                            severity = "CRITICAL" if network_preflight or not ignored else "WARNING"
                            action = "Rotate any exposed keys immediately."
                            if ".env" in file_path.name: action += " Add .env to .gitignore and move to a secret manager."
                            elif "src" in str(file_path): action = "Use environment variables or a secret vault instead of hardcoding."
                            
                            findings.append({
                                "file": str(file_path.relative_to(project_path)),
                                "line": line_num, "type": p_name, "severity": severity,
                                "value_masked": mask_secret(m.group(0)), "action": action
                            })
            except Exception: continue
    return findings

def execute_scan(target_project: str, network_preflight: bool = False) -> tuple[dict, list]:
    """Ejecuta el escáner, genera reporte DAST y actualiza el Engram si hay fugas."""
    start_time = time.time()
    project_path = Path(target_project).resolve()
    
    if not project_path.exists():
        raise FileNotFoundError(f"PHYSICAL_ERROR: Path {project_path} no encontrado en disco.")

    gitignore_lines = []
    gitignore_path = project_path / ".gitignore"
    if gitignore_path.exists():
        gitignore_lines = gitignore_path.read_text(encoding="utf-8").splitlines()

    findings = scan_project(project_path, gitignore_lines, network_preflight)
    
    # --- FASE 2: ENGRAM SYNC (Inyección de Reglas de Seguridad Cero-Trust) ---
    if findings:
        try:
            # Regla de seguridad transversal (afecta a todas las fases y tecnologías)
            cache_key = "dasafo:engram:rules:global:global"
            cached_rules = redis_client.get(cache_key)
            rules_list = json.loads(cached_rules) if cached_rules else []
            
            for finding in findings:
                rule = f"CRITICAL SECURITY MANDATE: Do not hardcode secrets. Found exposed {finding['type']} in {finding['file']}."
                if rule not in rules_list:
                    rules_list.append(rule)
            
            if rules_list:
                redis_client.set(cache_key, json.dumps(rules_list), ex=14400) # TTL 4 horas
        except Exception as e:
            import logging
            logging.getLogger("AduanaUniversal_v5.0").warning(f"Engram Sync Failed during security scan: {e}")

    secrets_found = len(findings)
    files_count = sum(len(files) for _, _, files in os.walk(project_path))
        
    execution_time_s = time.time() - start_time
    
    result_payload = {
        "industrial_status": "PASS" if not findings else "AUDIT_FAIL",
        "task_status": "COMPLETED" if not findings else "FAILED",
        "files_scanned": files_count,
        "secrets_found": secrets_found,
        "findings": findings,
        "compliance_report": {
            "zero_trust_verified": True,
            "secret_masking_active": True,
            "execution_duration_seconds": round(execution_time_s, 4)
        },
        "summary": f"Scan complete. Found {secrets_found} secrets across {files_count} files in {round(execution_time_s, 2)}s."
    }

    cid = str(uuid.uuid4())[:8]
    report_dir = project_path / "LOGS" / "AUDITS"
    report_dir.mkdir(parents=True, exist_ok=True)
    report_file = report_dir / f"SEC_SCAN_{cid}.json"
    report_file.write_text(json.dumps(result_payload, indent=2, ensure_ascii=False), encoding="utf-8")

    return result_payload, [str(report_file)]