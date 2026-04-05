import os
import json
import time
import requests
import subprocess
import re
from pathlib import Path

# Logic based on dasafo_FACTORY Core v5.0-MCP
# Standard: Auto-Healing & Immune System Enabled

def trigger_emergency_heal(project_path: Path, error_text: str, cid: str) -> list:
    """Generates a physical EMERGENCY_SPEC.json to trigger FACTORY_EVOLVER."""
    rules = []
    error_lower = error_text.lower()
    
    if "address already in use" in error_lower or "bind" in error_lower:
        port_match = re.search(r':(\d+)', error_text)
        port = port_match.group(1) if port_match else "3000"
        rules.append(f"PORT_CONFLICT:{port}")
    elif "oom" in error_lower or "137" in error_lower or "memory" in error_lower:
        rules.append("MEMORY_LIMIT_EXCEEDED")
    else:
        rules.append("GENERAL_INFRA_FAULT")

    spec_payload = {
      "v3_code": "STARK-SOLIDITY-v5.0-MCP-LITE",
      "metadata": {
        "task_id": f"EMERGENCY-{cid[:4]}",
        "assigned_agent": "FACTORY_EVOLVER",
        "technology": "docker",
        "context_pointers": ["WORKSPACE/infra/docker-compose.yml"]
      },
      "specification": {
        "01_objective": "Auto-Heal Infrastructure Blockers",
        "02_success_evidence": [
          {"location": "WORKSPACE/infra/docker-compose.yml", "type": "File", "critical": True}
        ],
        "03_constraints": [
          "Apply Golden Rules via skill-refactor-pro", 
          "SI Units (s, B)"
        ],
        "04_execution_context": [
          f"EMERGENCY RULES TO APPLY: {rules}",
          "MANDATORY STEP 1: Invoke skill-refactor-pro with action='emergency_heal' on docker-compose.yml.",
          "MANDATORY STEP 2: Once refactored, you MUST invoke deployment-health-check with action='deploy' to restart the stack and verify the cure."
        ]
      }
    }
    
    spec_path = project_path / "TASKS" / "01_PENDING" / "EMERGENCY_SPEC.json"
    spec_path.parent.mkdir(parents=True, exist_ok=True)
    with open(spec_path, "w", encoding="utf-8") as f:
        json.dump(spec_payload, f, indent=2)
        
    return rules

def execute_health_check(
    target_project: str,
    action: str = "check_endpoint",
    url: str = "http://localhost:3000/health",
    timeout_seconds: int = 5,
    cid: str = "AUTO"
) -> tuple[dict, list]:
    """Pure logic for endpoint validation and atomic deployment (v5.0-MCP)."""
    start_time = time.time()
    project_path = Path(target_project).resolve()
    deploy_logs_dir = project_path / "LOGS" / "deployment"
    deploy_logs_dir.mkdir(parents=True, exist_ok=True)
    
    # 1. Deployment Logic (If requested)
    if action == "deploy":
        infra_path = project_path / "WORKSPACE" / "infra"
        if not infra_path.exists():
            raise FileNotFoundError(f"INFRA_ERROR: No directory at {infra_path}")
        try:
            subprocess.run(["docker", "compose", "up", "--build", "-d"], 
                           cwd=str(infra_path), capture_output=True, text=True, check=True)
            time.sleep(5)
        except subprocess.CalledProcessError as e:
            error_output = e.stderr or str(e)
            applied_rules = trigger_emergency_heal(project_path, error_output, cid)
            return {
                "industrial_status": "LOCKED - EMERGENCY HEAL TRIGGERED",
                "verdict": "FAIL",
                "healing_activated": True,
                "summary": f"Deployment failed. Emergency spec generated for: {applied_rules}."
            }, []

    # 2. Health Check Execution
    status = "CRITICAL"
    latency_s = 0.0
    content_size_b = 0
    verdict = "FAIL"

    try:
        req_start = time.time()
        response = requests.get(url, timeout=timeout_seconds)
        latency_s = round(time.time() - req_start, 4)
        content_size_b = len(response.content)
        
        if response.status_code in [200, 404]:
            status = "HEALTHY"
            verdict = "PASS"
        else:
            status = f"UNHEALTHY_STATUS_{response.status_code}"
    except Exception as e:
        status = f"UNREACHABLE: {str(e)}"
        if action == "deploy":
            trigger_emergency_heal(project_path, str(e), cid)

    # 3. DAST Persistence
    report_path = deploy_logs_dir / f"HEALTH_{int(time.time())}.json"
    report_data = {
        "timestamp": time.time(),
        "url": url,
        "status": status,
        "metrics": {"latency_s": latency_s, "payload_B": content_size_b},
        "verdict": verdict
    }
    with open(report_path, 'w', encoding='utf-8') as f:
        json.dump(report_data, f, indent=2)

    result = {
        "industrial_status": f"SOLIDIFIED - {status}",
        "verdict": verdict,
        "metrics": {"latency": f"{latency_s}s", "content_size": f"{content_size_b}B"},
        "summary": f"Check at {url} resulted in {status}.",
        "execution_duration_seconds": round(time.time() - start_time, 4)
    }
    
    return result, [str(report_path)]