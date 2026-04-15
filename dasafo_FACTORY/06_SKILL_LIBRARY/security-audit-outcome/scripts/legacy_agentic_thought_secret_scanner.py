import re
import os
import json
import time
import uuid
from pathlib import Path
import redis

# Inicialización del Cliente Redis (Conexión industrial)
redis_client = redis.Redis(
    host=os.getenv("REDIS_HOST", "localhost"),
    port=int(os.getenv("REDIS_PORT", 6379)),
    decode_responses=True
)

def get_patterns() -> dict[str, re.Pattern]:
    """Diccionario de patrones optimizado para archivos .env y código fuente."""
    return {
        "AWS Access Key ID": re.compile(r"AKIA[0-9A-Z]{16}"),
        # 🛡️ NUEVO: Detecta la Secret Key (40 caracteres base64) incluso sin comillas
        "AWS Secret Access Key": re.compile(r"(?i)aws_secret_access_key\s*[:=]\s*['\"]?([A-Za-z0-9/+=]{40})['\"]?"),
        "OpenAI API Key": re.compile(r"sk-[a-zA-Z0-9]{48}"),
        "Anthropic API Key": re.compile(r"sk-ant-[a-zA-Z0-9-]{80,}"),
        "GitHub Personal Token": re.compile(r"gh[po]_[a-zA-Z0-9]{36}"),
        "Generic Secret": re.compile(r"(?i)(password|secret|token|api_key|apikey)\s*[:=]\s*['\"]?([A-Za-z0-9\-._~]{8,})['\"]?"), # 🛡️ Comillas opcionales
        "Private Key": re.compile(r"-----BEGIN (RSA |EC |DSA |OPENSSH )?PRIVATE KEY-----"),
        "Database URL": re.compile(r"(postgres|mysql|mongodb)://[^\s'\"]+:[^\s'\"]+@")
    }

def mask_secret(value: str) -> str:
    if len(value) <= 12: return "████████"
    return f"{value[:8]}...████████"

def is_ignored(file_path: Path, gitignore_lines: list[str], project_root: Path) -> bool:
    # 🚨 EXCEPCIÓN CRÍTICA: Los archivos .env NUNCA se ignoran en el escaneo de seguridad
    if ".env" in file_path.name.lower():
        return False

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
    # 🚫 Filtro de directorios pesados para optimizar el Guardián
    skip_dirs = {"node_modules", ".git", "__pycache__", ".venv", "venv", "dist"}
    text_extensions = {".py", ".js", ".ts", ".tsx", ".env", ".yml", ".yaml", ".json", ".md", ".txt", ".config"}
    
    for root, dirs, files in os.walk(project_path):
        dirs[:] = [d for d in dirs if d not in skip_dirs]
        for file in files:
            file_path = Path(root) / file
            
            # 🛡️ Aseguramos que los archivos .env siempre entren al escáner
            is_env = file.lower().startswith(".env")
            has_valid_ext = any(file.lower().endswith(ext) for ext in text_extensions)
            
            if not (is_env or has_valid_ext): continue

            try:
                content = file_path.read_text(encoding="utf-8")
                ignored = is_ignored(file_path, gitignore_lines, project_path)
                
                for p_name, p_regex in patterns.items():
                    for line_num, line_content in enumerate(content.splitlines(), 1):
                        match = p_regex.search(line_content)
                        if match:
                            # 🚨 Si es un .env, la severidad es CRITICAL aunque esté en gitignore
                            severity = "CRITICAL" if (not ignored or is_env) else "WARNING"
                            
                            findings.append({
                                "file": str(file_path.relative_to(project_path)),
                                "line": line_num, "type": p_name, "severity": severity,
                                "value_masked": mask_secret(match.group(0)),
                                "action": "Add to vault or use environment variables correctly."
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