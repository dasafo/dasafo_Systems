import sys, os; sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
import sys, os; sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
import os
import subprocess
import json
from skill_schema import SkillInput, SkillOutput

def run(skill_input: SkillInput) -> SkillOutput:
    """Industrialized entry point: Real Docker Pulse Check."""
    agent = "DEVOPS_SRE"
    skill = "resource-monitor"
    cid = skill_input.correlation_id
    project_id = skill_input.target_project or "ContentRepurpose"

    try:
        # 1. Logic: Physical Docker Inspection
        # Buscamos contenedores vinculados al proyecto (usualmente llevan el prefijo del proyecto)
        # Extraemos el nombre base si se pasó una ruta
        basename = os.path.basename(project_id.rstrip("/"))
        prefix = basename.lower().replace(" ", "-")
        cmd = ["docker", "ps", "--format", "{{.Names}} | {{.Status}} | {{.Image}}", "--filter", f"name={prefix}"]
        
        process = subprocess.run(cmd, capture_output=True, text=True, check=True)
        containers = process.stdout.strip().split("\n")
        
        real_metrics = []
        is_healthy = True
        warnings = []

        if not containers or (len(containers) == 1 and containers[0] == ""):
            is_healthy = False
            warnings.append(f"No active containers found for project: {project_id}")
        else:
            for line in containers:
                name, status, image = [i.strip() for i in line.split("|")]
                real_metrics.append({
                    "name": name,
                    "status": status,
                    "image": image
                })
                if "Up" not in status:
                    is_healthy = False
                    warnings.append(f"Container {name} is NOT healthy (Status: {status})")

        # 2. Heuristic check (Simulation of CPU/RAM to keep schema compatibility)
        # In a real PRO environment, we would use 'docker stats'
        health_status = "STABLE" if is_healthy else "CRITICAL"

        return SkillOutput.success(
            agent=agent,
            skill=skill,
            result={
                "health_status": health_status,
                "project": project_id,
                "containers": real_metrics,
                "total_containers": len(real_metrics) if real_metrics else 0,
                "analysis": "Verified via physical Docker socket"
            },
            correlation_id=cid,
            warnings=warnings,
            artifacts=[]
        )

    except subprocess.CalledProcessError as e:
        return SkillOutput.failure(agent, skill, f"Docker Execution Error: {e.stderr}", cid)
    except Exception as e:
        return SkillOutput.failure(agent, skill, f"Resource Monitoring Failed: {str(e)}", cid)

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--project", default="ContentRepurpose")
    args = parser.parse_args()
    
    # Mock input for direct CLI execution
    test_input = SkillInput(
        agent="CLI_TEST",
        skill="resource-monitor",
        params={},
        target_project=args.project
    )
    
    output = run(test_input)
    print(output.to_json())
