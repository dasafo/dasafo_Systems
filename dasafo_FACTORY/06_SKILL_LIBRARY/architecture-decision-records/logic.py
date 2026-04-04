import os
import re
import time
from datetime import datetime
from pathlib import Path

# Funciones Auxiliares Industriales (v5.0-MCP)
def get_next_id(adr_dir: Path) -> str:
    """Calcula el siguiente ID numérico disponible en el directorio DOCS/ADR."""
    existing_ids = []
    if adr_dir.exists():
        for f in adr_dir.glob("*.md"):
            match = re.match(r"^(\d+)-", f.name)
            if match:
                existing_ids.append(int(match.group(1)))
    
    next_id = max(existing_ids + [0]) + 1
    return f"{next_id:04d}"

def update_index(adr_dir: Path):
    """Genera/Actualiza el README.md de DOCS/ADR como índice Single-Source-of-Truth."""
    index_path = adr_dir / "README.md"
    adrs = []
    if adr_dir.exists():
        for f in sorted(adr_dir.glob("*.md")):
            if f.name == "README.md": continue
            match = re.match(r"^(\d+)-(.*)\.md$", f.name)
            if match:
                adrs.append(f"| {match.group(1)} | [{match.group(2).replace('-', ' ').title()}]({f.name}) |")
    
    content = "# 📜 Industrial Architecture Decision Records (ADR)\n\n"
    content += "| ID | Decision | Status |\n|---|---|---|\n"
    content += "\n".join(adrs)
    content += "\n\n*v5.0-Solidified | Dasafo Factory.*"
    index_path.write_text(content, encoding="utf-8")

def execute_adr(
    target_project: str,
    agent: str = "ARCHITECT",
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
        safe_title = re.sub(r'[^\w\s-]', '', title.lower()).strip().replace(' ', '-')
        adr_file = adr_dir / f"{new_id}-{safe_title}.md"
        
        if adr_file.exists() and not overwrite:
            raise FileExistsError(f"REDUNDANCY LOCK: ADR {new_id} exists.")

        adr_md = f"""# ADR {new_id}: {title}

| Field | Details |
|---|---|
| Status | SOLIDIFIED |
| Date | {datetime.now().strftime('%Y-%m-%d')} |
| Agent | {agent} |

## 1. Context
{context or "TBD"}

## 2. Decision
{decision or "TBD"}

## 3. Consequences
{consequences or "TBD"}

---
*v5.0-MCP Architectural Mandate.*
"""
        adr_file.write_text(adr_md, encoding="utf-8")
        update_index(adr_dir)
        
        res = {"industrial_status": "SOLIDIFIED - ADR RECORDED", "adr_id": new_id, "summary": f"ADR {new_id} recorded at {adr_file.name}."}
        artifacts.extend([str(adr_file), str(adr_dir / "README.md")])

    result = {
        **res,
        "execution_duration_seconds": round(time.time() - start_time, 4)
    }
    return result, artifacts