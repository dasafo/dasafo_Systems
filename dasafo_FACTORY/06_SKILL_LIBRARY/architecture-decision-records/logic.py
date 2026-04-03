import os
import re
import time
from datetime import datetime
from pathlib import Path

# Mantener funciones auxiliares get_next_id y update_index del original...

def execute_adr(
    target_project: str,
    action: str = "new",
    title: str = None,
    context: str = None,
    decision: str = None,
    consequences: str = None,
    target_id: str = None,
    overwrite: bool = False
) -> tuple[dict, list]:
    """Lógica pura de gestión de ADRs (v5.0-MCP)."""
    start_time = time.time()
    project_path = Path(target_project).resolve()
    adr_dir = project_path / "DOCS" / "ADR"
    adr_dir.mkdir(parents=True, exist_ok=True)
    
    artifacts = []
    
    if action == "init":
        from .logic import update_index
        update_index(adr_dir)
        res = {"industrial_status": "ADR_INDEX_UPDATED"}
        artifacts.append(str(adr_dir / "README.md"))

    elif action == "finalize_blueprint":
        blueprint_file = project_path / "DOCS" / "ARCH" / "BLUEPRINT.md"
        blueprint_file.parent.mkdir(parents=True, exist_ok=True)
        # ... (Lógica de escaneo DAST de ADRs del original)
        blueprint_file.write_text(blueprint_content, encoding="utf-8")
        res = {"industrial_status": "SOLIDIFIED - BLUEPRINT CREATED"}
        artifacts.append(str(blueprint_file))

    elif action in ["new", "supersede"]:
        new_id = get_next_id(adr_dir)
        safe_title = re.sub(r'[^\w\s-]', '', title.lower()).replace(' ', '-')
        adr_file = adr_dir / f"{new_id}-{safe_title}.md"
        
        if adr_file.exists() and not overwrite:
            raise FileExistsError(f"REDUNDANCY LOCK: ADR {new_id} exists.")

        # ... (Lógica de escritura de MD y supersede del original)
        adr_file.write_text(adr_md, encoding="utf-8")
        update_index(adr_dir)
        res = {"industrial_status": "SOLIDIFIED - ADR RECORDED", "adr_id": new_id}
        artifacts.extend([str(adr_file), str(adr_dir / "README.md")])

    result = {
        **res,
        "execution_duration_seconds": round(time.time() - start_time, 4)
    }
    return result, artifacts