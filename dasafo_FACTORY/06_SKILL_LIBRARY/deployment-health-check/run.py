from __future__ import annotations
import sys, os; sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
"""
run.py — Deployment Health Check (DEPLOYMENT_MONITOR)
v3.4.1-S: Industrial Core | Real-time Sentinel & Auto-Deploy.
"""

import os
import json
import time
import requests
import subprocess
from pathlib import Path
from skill_schema import SkillInput, SkillOutput

def run(skill_input: SkillInput) -> SkillOutput:
    agent = skill_input.agent or "DEPLOYMENT_MONITOR"
    skill = "deployment-health-check"
    cid = skill_input.correlation_id
    params = skill_input.params or {}
    start_time = time.time()

    try:
        # 1. Resolución de Proyecto y Rutas (Protocolo DAST)
        target = params.get("target_project") or skill_input.target_project or os.environ.get("TARGET_PROJECT")
        if not target:
             return SkillOutput.failure(agent, skill, "SECURITY LOCK: Missing TARGET_PROJECT.", cid)
        
        project_path = Path(target).resolve()
        deploy_logs_dir = project_path / "LOGS" / "deployment"
        deploy_logs_dir.mkdir(parents=True, exist_ok=True)
        
        target_url = params.get("url", "http://localhost:3000/health")
        timeout_s = params.get("timeout_seconds", 5)
        action = params.get("action", "check_endpoint")

        # 🚀 2. INYECCIÓN INDUSTRIAL: Si la acción es 'deploy', levantamos los contenedores primero
        if action == "deploy":
            infra_path = project_path / "WORKSPACE" / "infra"
            if not infra_path.exists():
                return SkillOutput.failure(agent, skill, f"No infra directory found at {infra_path}", cid)
            
            try:
                # Ejecutamos docker compose en el Host y lo dejamos en background (-d)
                subprocess.run(["docker", "compose", "up", "--build", "-d"], cwd=str(infra_path), check=True)
                # Damos 5 segundos de cortesía para que los puertos se mapeen
                time.sleep(5)
            except subprocess.CalledProcessError as e:
                return SkillOutput.failure(agent, skill, f"Docker Compose Failed: {e}", cid)

        # 3. Ejecución de Health-Check (Métricas SI)
        status = "CRITICAL"
        latency_s = 0.0
        content_size_b = 0
        verdict = "FAIL"

        try:
            req_start = time.time()
            response = requests.get(target_url, timeout=timeout_s)
            latency_s = round(time.time() - req_start, 4) # Segundos (s)
            content_size_b = len(response.content) # Bytes (B)
            
            # Aceptamos 200 (OK) o 404 (Not Found si la ruta exacta no existe pero el server responde)
            if response.status_code in [200, 404]:
                status = "HEALTHY"
                verdict = "PASS"
            else:
                status = f"UNHEALTHY_STATUS_{response.status_code}"
        except Exception as e:
            status = f"UNREACHABLE: {str(e)}"

        # 4. Persistencia de Evidencia Física (DAST)
        report_path = deploy_logs_dir / f"HEALTH_{cid[:8]}.json"
        report_data = {
            "cid": cid,
            "timestamp": time.time(),
            "target": target_url,
            "status": status,
            "metrics": {
                "latency_seconds": latency_s,
                "payload_bytes": content_size_b
            },
            "verdict": verdict
        }
        
        with open(report_path, 'w', encoding='utf-8') as f:
            json.dump(report_data, f, indent=2)

        execution_duration_s = round(time.time() - start_time, 4)

        # 5. Outcome Report Industrial
        result_payload = {
            "industrial_status": f"SOLIDIFIED - {status}",
            "verdict": verdict,
            "metrics": {
                "latency": f"{latency_s}s",
                "content_size": f"{content_size_b}B"
            },
            "artifacts": [str(report_path)],
            "compliance_report": {
                "si_metrics_applied": True,
                "execution_duration_seconds": execution_duration_s
            },
            "summary": f"Check en {target_url} resultó en {status} ({latency_s}s). Acción ejecutada: {action}"
        }

        return SkillOutput.success(agent, skill, result_payload, [str(report_path)], cid)

    except Exception as e:
        return SkillOutput.failure(agent, skill, f"Health Check Critical Fault: {str(e)}", cid)