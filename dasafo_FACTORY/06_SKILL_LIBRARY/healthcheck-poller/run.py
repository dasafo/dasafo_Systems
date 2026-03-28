import sys, os; sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
import os
import time
import urllib.request
from pathlib import Path
from datetime import datetime
from skill_schema import SkillInput, SkillOutput

def run(skill_input: SkillInput) -> SkillOutput:
    """Industrialized entry point: Real Physical Healthcheck."""
    agent = "DEVOPS_SRE"
    skill = "healthcheck-poller"
    cid = skill_input.correlation_id

    try:
        # 1. Resolve Target
        endpoint = skill_input.params.get("endpoint", "http://localhost:3000")
        target = skill_input.target_project or os.environ.get("TARGET_PROJECT")
        
        # 2. Logic: Physical HTTP Pulse
        start_time = time.time()
        timeout = skill_input.params.get("timeout_s", 5)
        
        status = "CRITICAL"
        latency_ms = 0
        response_code = 0
        body_sample = ""

        try:
            with urllib.request.urlopen(endpoint, timeout=timeout) as response:
                response_code = response.getcode()
                latency_ms = int((time.time() - start_time) * 1000)
                if response_code == 200:
                    status = "OPTIMAL"
                    # Opcional: leer una muestra para detectar "pantallas blancas" por falta de montaje
                    body_sample = response.read(500).decode("utf-8").lower()
                    if "id=\"root\"" not in body_sample and "id=\"app\"" not in body_sample and "bundle" not in body_sample:
                        status = "WARNING"
                        warnings = ["Service is up but may have mounting issues (root/app div not detected)."]
                    else:
                        warnings = []
                else:
                    status = "WARNING"
                    warnings = [f"Service returned non-200 code: {response_code}"]
        except Exception as e:
            status = "CRITICAL"
            warnings = [f"Physical Connection Failed: {str(e)}"]

        # 3. Telemetry Persistence
        artifacts = []
        if target:
            # Intentamos localizar la ruta del proyecto si es un ID
            project_base = Path("/home/david/Documents/AI/AGENTES/PROJECTS") / str(target)
            if project_base.exists():
                telemetry_path = project_base / "LOGS/reports/PROJECT_TELEMETRY.md"
                telemetry_path.parent.mkdir(parents=True, exist_ok=True)
                
                log_entry = f"[{datetime.now().isoformat()}] HEALTHCHECK: {endpoint} | Status: {status} | Latency: {latency_ms}ms | Code: {response_code}\n"
                with open(telemetry_path, "a", encoding="utf-8") as f:
                    f.write(log_entry)
                artifacts.append(str(telemetry_path))

        return SkillOutput.success(
            agent=agent,
            skill=skill,
            result={
                "status": status,
                "endpoint": endpoint,
                "latency_ms": latency_ms,
                "http_code": response_code,
                "industrial_verification": True
            },
            correlation_id=cid,
            warnings=warnings,
            artifacts=artifacts
        )

    except Exception as e:
        return SkillOutput.failure(agent, skill, f"Healthcheck Poller Failure: {str(e)}", cid)
