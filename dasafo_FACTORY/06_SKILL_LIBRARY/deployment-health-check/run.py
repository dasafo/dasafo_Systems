from __future__ import annotations
import sys, os; sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
"""
run.py — Deployment Health Check (DEPLOYMENT_MONITOR)
v4.0-MCP: Industrial Core | Auto-Healing & Immune System Enabled.
"""

import os
import json
import time
import requests
import subprocess
import re
from pathlib import Path
from skill_schema import SkillInput, SkillOutput

def run(skill_input: SkillInput) -> SkillOutput:
    agent = skill_input.agent or "DEPLOYMENT_MONITOR"
    skill = "deployment-health-check"
    cid = skill_input.correlation_id or "AUTO"
    params = skill_input.params or {}
    start_time = time.time()

    try:
        target = params.get("target_project") or skill_input.target_project or os.environ.get("TARGET_PROJECT")
        if not target:
             return SkillOutput.failure(agent, skill, "SECURITY LOCK: Missing TARGET_PROJECT.", cid)
        
        project_path = Path(target).resolve()
        deploy_logs_dir = project_path / "LOGS" / "deployment"
        deploy_logs_dir.mkdir(parents=True, exist_ok=True)
        
        target_url = params.get("url", "http://localhost:3000/health")
        timeout_s = params.get("timeout_seconds", 5)
        action = params.get("action", "check_endpoint")

        # 🚑 Función Interna de Auto-Sanación (Generador de Emergency Specs)
        def trigger_emergency_heal(error_text: str) -> list:
            rules = []
            error_lower = error_text.lower()
            
            # Detectar conflicto de puertos
            if "address already in use" in error_lower or "bind" in error_lower:
                port_match = re.search(r':(\d+)', error_text)
                port = port_match.group(1) if port_match else "3000"
                rules.append(f"PORT_CONFLICT:{port}")
            # Detectar límite de memoria u Out-Of-Memory (OOM)
            elif "oom" in error_lower or "137" in error_lower or "memory" in error_lower:
                rules.append("MEMORY_LIMIT_EXCEEDED")
            else:
                rules.append("GENERAL_INFRA_FAULT")

            # Generar Spec de Emergencia (DAST)
            spec_payload = {
              "v3_code": "STARK-SOLIDITY-v4.0-MCP-LITE",
              "metadata": {
                "task_id": f"EMERGENCY-{cid[:4]}",
                "assigned_agent": "FACTORY_EVOLVER",
                "technology": "docker", # <--- AÑADIDO: Permite inyección JIT de reglas de infra
                "context_pointers": ["WORKSPACE/infra/docker-compose.yml"]
              },
              "specification": {
                "01_objective": "Auto-Heal Infrastructure Blockers",
                "02_success_evidence": [
                  {"location": "WORKSPACE/infra/docker-compose.yml", "type": "File", "critical": True}
                ],
                "03_constraints": ["Apply Golden Rules via skill-refactor-pro", "SI Units (s, B)"],
                "04_execution_context": [f"EMERGENCY RULES TO APPLY: {rules}"]
              }
            }
            
            # Escritura física para activar el Double-Gating
            spec_path = project_path / "TASKS" / "01_PENDING" / "EMERGENCY_SPEC.json"
            spec_path.parent.mkdir(parents=True, exist_ok=True)
            with open(spec_path, "w", encoding="utf-8") as f:
                json.dump(spec_payload, f, indent=2)
                
            return rules

        # 🚀 INYECCIÓN INDUSTRIAL: Despliegue con Sensor de Traumas
        if action == "deploy":
            infra_path = project_path / "WORKSPACE" / "infra"
            if not infra_path.exists():
                return SkillOutput.failure(agent, skill, f"No infra directory found at {infra_path}", cid)
            
            try:
                # Usamos capture_output para poder leer el stderr si explota
                result = subprocess.run(["docker", "compose", "up", "--build", "-d"], cwd=str(infra_path), capture_output=True, text=True, check=True)
                time.sleep(5)
            except subprocess.CalledProcessError as e:
                # 🔴 INCENDIO DETECTADO: Disparar Auto-Sanación
                error_output = e.stderr or e.stdout or str(e)
                applied_rules = trigger_emergency_heal(error_output)
                
                result_payload = {
                    "industrial_status": "LOCKED - EMERGENCY HEAL TRIGGERED",
                    "verdict": "FAIL",
                    "metrics": {"latency": "0.0s", "content_size": "0B"},
                    "healing_protocol_activated": True,
                    "rules_sent_to_evolver": applied_rules,
                    "summary": f"Despliegue fallido. EMERGENCY_SPEC asignada a FACTORY_EVOLVER con reglas: {applied_rules}."
                }
                return SkillOutput.success(agent, skill, result_payload, [], cid, summary=result_payload["summary"])

        # 3. Ejecución de Health-Check (Métricas SI)
        status = "CRITICAL"
        latency_s = 0.0
        content_size_b = 0
        verdict = "FAIL"

        try:
            req_start = time.time()
            response = requests.get(target_url, timeout=timeout_s)
            latency_s = round(time.time() - req_start, 4)
            content_size_b = len(response.content)
            
            if response.status_code in [200, 404]:
                status = "HEALTHY"
                verdict = "PASS"
            else:
                status = f"UNHEALTHY_STATUS_{response.status_code}"
        except Exception as e:
            status = f"UNREACHABLE: {str(e)}"
            
            # 🔴 CAÍDA EN TIEMPO REAL: Disparar Auto-Sanación si no es check de rutina
            if action == "deploy":
                applied_rules = trigger_emergency_heal(str(e))
                status += f" | AUTO-HEAL INITIATED: {applied_rules}"

        # 4. Persistencia de Evidencia Física (DAST)
        report_path = deploy_logs_dir / f"HEALTH_{cid[:8]}.json"
        report_data = {
            "cid": cid,
            "timestamp": time.time(),
            "target": target_url,
            "status": status,
            "metrics": {"latency_seconds": latency_s, "payload_bytes": content_size_b},
            "verdict": verdict
        }
        
        with open(report_path, 'w', encoding='utf-8') as f:
            json.dump(report_data, f, indent=2)

        execution_duration_s = round(time.time() - start_time, 4)

        result_payload = {
            "industrial_status": f"SOLIDIFIED - {status}",
            "verdict": verdict,
            "metrics": {"latency": f"{latency_s}s", "content_size": f"{content_size_b}B"},
            "artifacts": [str(report_path)],
            "compliance_report": {"si_metrics_applied": True, "execution_duration_seconds": execution_duration_s},
            "summary": f"Check en {target_url} resultó en {status} ({latency_s}s)."
        }

        return SkillOutput.success(agent, skill, result_payload, [str(report_path)], cid)

    except Exception as e:
        return SkillOutput.failure(agent, skill, f"Health Check Critical Fault: {str(e)}", cid)