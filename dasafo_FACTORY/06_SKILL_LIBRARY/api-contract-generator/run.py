from __future__ import annotations
import sys, os; sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
"""
run.py — API Designer & Contract Generator (ARCHITECT / BACKEND_DEV)
v3.4.0-S: Modular Toolbox | Industrial Scale.

Solidified: v3.4.0-S Redundancy Lock, Compliance Reporting & SI Mandate.
"""

import os
import re
import yaml
import time
from pathlib import Path
from skill_schema import SkillInput, SkillOutput

def create_pro_openapi(resource: str, version: str) -> dict:
    """Generates a professional OpenAPI 3.1.0 resource structure."""
    res_plural = f"{resource}s"
    res_title = resource.capitalize()
    
    return {
        "openapi": "3.1.0",
        "info": {
            "title": f"Industrial {res_title} API",
            "version": version,
            "description": f"Design-First API Contract (v3.4.0-S) for {resource} management.",
            "contact": {"name": "Architect Unit", "email": "architect@dasafo.factory"}
        },
        "servers": [{"url": "http://api.local/v1", "description": "Local Dev Server"}],
        "paths": {
            f"/{res_plural}": {
                "get": {
                    "summary": f"List {res_plural}",
                    "tags": [res_title],
                    "parameters": [
                        {"name": "offset", "in": "query", "schema": {"type": "integer", "default": 0}},
                        {"name": "limit", "in": "query", "schema": {"type": "integer", "default": 10}}
                    ],
                    "responses": {
                        "200": {"description": "Successful retrieval", "content": {"application/json": {"schema": {"$ref": f"#/components/schemas/{res_title}Collection"}}}},
                        "401": {"$ref": "#/components/responses/Unauthorized"}
                    }
                },
                "post": {
                    "summary": f"Create {resource}",
                    "tags": [res_title],
                    "requestBody": {"required": True, "content": {"application/json": {"schema": {"$ref": f"#/components/schemas/{res_title}Input"}}}},
                    "responses": {
                        "201": {"description": "Created", "content": {"application/json": {"schema": {"$ref": f"#/components/schemas/{res_title}"}}}},
                        "400": {"$ref": "#/components/responses/BadRequest"}
                    }
                }
            },
            f"/{res_plural}/{{id}}": {
                "parameters": [{"name": "id", "in": "path", "required": True, "schema": {"type": "string", "format": "uuid"}}],
                "get": {"summary": f"Get {resource}", "responses": {"200": {"description": "OK", "content": {"application/json": {"schema": {"$ref": f"#/components/schemas/{res_title}"}}}}, "404": {"$ref": "#/components/responses/NotFound"}}},
                "put": {"summary": f"Update {resource}", "requestBody": {"required": True, "content": {"application/json": {"schema": {"$ref": f"#/components/schemas/{res_title}Input"}}}}, "responses": {"200": {"description": "OK"}, "404": {"$ref": "#/components/responses/NotFound"}}},
                "delete": {"summary": f"Delete {resource}", "responses": {"204": {"description": "No Content"}}}
            }
        },
        "components": {
            "schemas": {
                res_title: {"type": "object", "properties": {"id": {"type": "string", "format": "uuid"}, "created_at": {"type": "string", "format": "date-time"}}},
                f"{res_title}Input": {"type": "object", "required": ["name"], "properties": {"name": {"type": "string"}}},
                f"{res_title}Collection": {"type": "object", "properties": {"items": {"type": "array", "items": {"$ref": f"#/components/schemas/{res_title}"}}, "total": {"type": "integer"}}},
                "Error": {
                    "type": "object",
                    "description": "RFC 7807 Problem Details",
                    "properties": {
                        "type": {"type": "string", "format": "uri", "default": "about:blank"},
                        "title": {"type": "string"},
                        "status": {"type": "integer"},
                        "detail": {"type": "string"},
                        "instance": {"type": "string", "format": "uri"}
                    }
                }
            },
            "responses": {
                "BadRequest": {"description": "Bad Request", "content": {"application/problem+json": {"schema": {"$ref": "#/components/schemas/Error"}}}},
                "Unauthorized": {"description": "Unauthorized", "content": {"application/problem+json": {"schema": {"$ref": "#/components/schemas/Error"}}}},
                "NotFound": {"description": "Not Found", "content": {"application/problem+json": {"schema": {"$ref": "#/components/schemas/Error"}}}}
            }
        }
    }

def run(skill_input: SkillInput) -> SkillOutput:
    """Dasafo Factory Entry Point for API Designer."""
    agent = skill_input.agent or "ARCHITECT"
    skill = "api-contract-generator"
    cid = skill_input.correlation_id
    params = skill_input.params or {}
    
    start_time = time.time()

    try:
        # 1. Path & Context Resolution
        target = params.get("target_project") or skill_input.target_project or os.environ.get("TARGET_PROJECT")
        if not target:
             return SkillOutput.failure(agent, skill, "SECURITY LOCK: Missing TARGET_PROJECT path.", cid)
        
        project_path = Path(target).resolve()
        resource = params.get("resource", "generic_resource")
        version = params.get("version", "1.0.0")
        overwrite = params.get("overwrite", False)

        # 2. Redundancy Lock Enforcement
        docs_dir = project_path / "DOCS"
        docs_dir.mkdir(parents=True, exist_ok=True)
        yaml_path = docs_dir / "API-CONTRACT.yaml"
        
        if yaml_path.exists() and not overwrite:
             return SkillOutput.failure(agent, skill, f"REDUNDANCY LOCK: {yaml_path.name} already exists. Set overwrite=True to update.", cid)

        # 3. Logic: Create Spec (OpenAPI 3.1)
        spec = create_pro_openapi(resource, version)

        # 4. Persistence
        with open(yaml_path, 'w', encoding='utf-8') as f:
            yaml.dump(spec, f, sort_keys=False, allow_unicode=True)
            
        # 5. Result Metrics (SI Compliance)
        endpoints_count = sum(len(methods) for methods in spec.get("paths", {}).values())
        execution_time_s = time.time() - start_time
        
        result_payload = {
            "status": "SOLIDIFIED - PRO DESIGN",
            "contract_path": str(yaml_path),
            "design_summary": {
                "resource_entity": resource,
                "endpoints_count": endpoints_count,
                "standards_compliance": "OpenAPI 3.1 + RFC 7807"
            },
            "compliance_report": {
                "openapi_standard": "3.1.0",
                "rfc7807_enabled": True,
                "lock_verified": True,
                "execution_duration_seconds": round(execution_time_s, 4)
            },
            "summary": f"API Contract for '{resource}' generated at DOCS/API-CONTRACT.yaml. {endpoints_count} endpoints defined."
        }

        return SkillOutput.success(
            agent=agent,
            skill=skill,
            result=result_payload,
            correlation_id=cid,
            artifacts=[str(yaml_path)]
        )

    except Exception as e:
        return SkillOutput.failure(agent, skill, f"CRITICAL Design Error: {str(e)}", cid)