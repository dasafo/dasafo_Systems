# dasafo_FACTORY/06_SKILL_LIBRARY/api-contract-generator/logic.py
import os
import yaml
import time
from pathlib import Path

def create_pro_openapi(resource: str, version: str) -> dict:
    """Generates a professional OpenAPI 3.1.0 resource structure."""
    res_plural = f"{resource}s"
    res_title = resource.capitalize()
    
    return {
        "openapi": "3.1.0",
        "info": {
            "title": f"Industrial {res_title} API",
            "version": version,
            "description": f"Design-First API Contract (v5.0-MCP) for {resource} management.",
            "contact": {"name": "Architect Unit", "email": "architect@dasafo.factory"}
        },
        "servers": [{"url": "http://api.local/v1", "description": "Local Dev Server"}],
        "paths": {
            f"/{res_plural}": {
                "get": {
                    "summary": f"List {res_plural}",
                    "responses": {
                        "200": {"description": "Successful retrieval"}
                    }
                },
                "post": {
                    "summary": f"Create {resource}",
                    "responses": {
                        "201": {"description": "Created"}
                    }
                }
            }
        }
    }

def execute_design(target_project: str, resource: str = "generic_resource", version: str = "1.0.0", overwrite: bool = False) -> tuple[dict, list]:
    """Lógica pura de diseño y persistencia del contrato API."""
    start_time = time.time()
    project_path = Path(target_project).resolve()
    
    # Redundancy Lock Enforcement
    docs_dir = project_path / "DOCS"
    docs_dir.mkdir(parents=True, exist_ok=True)
    yaml_path = docs_dir / "API-CONTRACT.yaml"
    
    if yaml_path.exists() and not overwrite:
        raise FileExistsError(f"REDUNDANCY LOCK: {yaml_path.name} ya existe. Usa overwrite=True para actualizar.")

    # Generación del Spec
    spec = create_pro_openapi(resource, version)

    # Persistencia Física (DAST)
    with open(yaml_path, 'w', encoding='utf-8') as f:
        yaml.dump(spec, f, sort_keys=False, allow_unicode=True)
            
    execution_time_s = time.time() - start_time
    endpoints_count = sum(len(methods) for methods in spec.get("paths", {}).values())
    
    result_payload = {
        "industrial_status": "SOLIDIFIED - PRO DESIGN",
        "task_status": "COMPLETED",
        "design_summary": {
            "resource_entity": resource,
            "endpoints_count": endpoints_count,
            "standards_compliance": "OpenAPI 3.1"
        },
        "compliance_report": {
            "lock_verified": True,
            "execution_duration_seconds": round(execution_time_s, 4)
        },
        "summary": f"API Contract for '{resource}' generated at DOCS/API-CONTRACT.yaml. {endpoints_count} endpoints defined."
    }

    return result_payload, [str(yaml_path)]