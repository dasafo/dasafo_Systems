# dasafo_FACTORY/06_SKILL_LIBRARY/api-docs-generator/logic.py
import os
import yaml
import time
from pathlib import Path

# Mantener funciones auxiliares generate_code_examples y get_pro_docs del original...

def execute_docs_generation(
    target_project: str, 
    contract_path: str = "API-CONTRACT.yaml", 
    output_name: str = "API_REFERENCE_PRO.md", 
    include_examples: bool = True, 
    overwrite: bool = False
) -> tuple[dict, list]:
    """Lógica pura de generación de documentación (v5.0-MCP)."""
    start_time = time.time()
    project_path = Path(target_project).resolve()
    input_path = project_path / "DOCS" / contract_path
    output_path = project_path / "DOCS" / output_name

    if not input_path.exists():
        raise FileNotFoundError(f"Source contract {input_path} not found.")

    with open(input_path, 'r', encoding='utf-8') as f:
        spec = yaml.safe_load(f)

    # Auditoría Industrial de Endpoints y Errores
    endpoints_count = 0
    errors_count = 0
    paths = spec.get("paths", {})
    for path_key, methods in paths.items():
        for method, details in methods.items():
            endpoints_count += 1
            for code in details.get("responses", {}).keys():
                try:
                    if int(str(code)) >= 400 or code == "default": errors_count += 1
                except: pass

    # Generación y Persistencia
    from .logic import get_pro_docs # Importación local de las funciones auxiliares
    docs_content = get_pro_docs(spec, include_examples)

    if output_path.exists() and not overwrite:
         raise FileExistsError(f"REDUNDANCY LOCK: {output_path.name} already exists.")

    output_path.write_text(docs_content, encoding="utf-8")

    result = {
        "industrial_status": "SOLIDIFIED - PRO DOCS GENERATED",
        "path": str(output_path),
        "summary": f"API Reference generated for {endpoints_count} endpoints ({errors_count} errors) at DOCS/.",
        "execution_duration_seconds": round(time.time() - start_time, 4)
    }
    return result, [str(output_path)]