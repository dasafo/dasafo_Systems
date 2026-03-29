from __future__ import annotations
import sys, os; sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
"""
run.py — Async FastAPI & Domain Logic (BACKEND_DEV / ARCHITECT)
v3.3.0-S: Modular Toolbox | Industrial Scale.

Advanced module to scaffold and manage domain-driven FastAPI microservices.
Based on jezweb/claude-skills/fastapi logic.
"""

import os
import re
from pathlib import Path
from skill_schema import SkillInput, SkillOutput

def get_router_template(domain: str) -> str:
    return f"""from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from . import schemas, service, dependencies

router = APIRouter(prefix="/{domain.replace('_', '-')}", tags=["{domain.capitalize()}"])

@router.get("/", response_model=List[schemas.{domain.capitalize()}])
async def list_{domain}s(
    domain_service: service.{domain.capitalize()}Service = Depends(dependencies.get_{domain}_service)
):
    \"\"\" List all {domain}s (v3.3.0-S) \"\"\"
    return await domain_service.get_all()
"""

def get_schemas_template(domain: str) -> str:
    return f"""from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime
from typing import Optional

class {domain.capitalize()}Base(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    description: Optional[str] = Field(None, max_length=500)

class {domain.capitalize()}Create({domain.capitalize()}Base):
    pass

class {domain.capitalize()}({domain.capitalize()}Base):
    model_config = ConfigDict(from_attributes=True)
    
    id: int
    created_at: datetime
"""

def get_service_template(domain: str) -> str:
    return f"""from typing import List
from . import models, schemas

class {domain.capitalize()}Service:
    \"\"\" Business logic for {domain} (v3.3.0-S) \"\"\"
    async def get_all(self) -> List[models.{domain.capitalize()}]:
        # Implementation here
        return []
"""

def run(skill_input: SkillInput) -> SkillOutput:
    """Industrial Entry Point for FastAPI Backend Logic."""
    agent = skill_input.agent or "BACKEND_DEV"
    skill = "async-fastapi-logic"
    cid = skill_input.correlation_id
    params = skill_input.params or {}

    try:
        # 1. Path & Context Resolution
        target = params.get("target_project") or skill_input.target_project or os.environ.get("TARGET_PROJECT")
        if not target:
             return SkillOutput.failure(agent, skill, "SECURITY LOCK: Missing TARGET_PROJECT path.", cid)
        
        project_path = Path(target).resolve()
        action = params.get("action", "scaffold")
        src_dir = project_path / "src"
        
        artifacts = []

        # 2. Logical Core
        if action == "scaffold":
            # Initial Project Structure (Domain-Based)
            subdirs = ["auth", "items", "shared"]
            for sd in subdirs:
                d_path = src_dir / sd
                d_path.mkdir(parents=True, exist_ok=True)
                (d_path / "__init__.py").touch()
            
            main_py = src_dir / "main.py"
            main_py.write_text("from fastapi import FastAPI\n\napp = FastAPI(title='Industrial API v3.3.0-S')\n", encoding="utf-8")
            artifacts.append(str(main_py))
            
            return SkillOutput.success(agent, skill, {"status": "SCAFFOLDED"}, artifacts, correlation_id=cid)

        elif action == "add_domain":
            domain = params.get("domain_name")
            if not domain:
                 return SkillOutput.failure(agent, skill, "INPUT_ERROR: Missing 'domain_name'.", cid)
            
            domain_path = src_dir / domain
            domain_path.mkdir(parents=True, exist_ok=True)
            
            files = {
                "__init__.py": "",
                "router.py": get_router_template(domain),
                "schemas.py": get_schemas_template(domain),
                "service.py": get_service_template(domain),
                "models.py": "# SQLAlchemy Models (v3.3.0-S)\n",
                "dependencies.py": f"def get_{domain}_service():\n    pass\n"
            }
            
            for name, content in files.items():
                f_path = domain_path / name
                f_path.write_text(content, encoding="utf-8")
                artifacts.append(str(f_path))

            return SkillOutput.success(
                agent=agent,
                skill=skill,
                result={"status": "DOMAIN_ADDED", "domain": domain},
                artifacts=artifacts,
                correlation_id=cid
            )

        elif action == "add_endpoint":
            domain = params.get("domain_name")
            route = params.get("route_name", "new_endpoint")
            method = params.get("method", "GET").lower()
            
            if not domain:
                 return SkillOutput.failure(agent, skill, "INPUT_ERROR: Missing 'domain_name'.", cid)
            
            router_path = src_dir / domain / "router.py"
            if not router_path.exists():
                 return SkillOutput.failure(agent, skill, f"DOMAIN_ERROR: Domain '{domain}' not found.", cid)

            new_code = f"\n@router.{method}(\"/{route.replace('_', '-')}\")\nasync def {route}():\n    return {{\"status\": \"solidified\"}}\n"
            
            with open(router_path, 'a', encoding='utf-8') as f:
                f.write(new_code)
            
            artifacts.append(str(router_path))

            return SkillOutput.success(
                agent=agent,
                skill=skill,
                result={"status": "ENDPOINT_SOLIDIFIED", "route": route},
                artifacts=artifacts,
                correlation_id=cid
            )

        else:
             return SkillOutput.failure(agent, skill, f"Invalid FastAPI action: {action}", cid)

    except Exception as e:
        return SkillOutput.failure(agent, skill, f"CRITICAL FastAPI Fault: {str(e)}", cid)
