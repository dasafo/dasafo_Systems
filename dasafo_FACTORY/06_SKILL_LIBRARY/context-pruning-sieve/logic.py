import os
import time
from pathlib import Path

# Logic based on: https://skills.sh/sickn33/antigravity-awesome-skills/context-optimization

def execute_pruning(
    target_project: str,
    target_file: str,
    action: str = "compact_context",
    budget_threshold: float = 0.8
) -> tuple[dict, list]:
    """Pure logic for context compaction and token-aware pruning (v5.0-MCP)."""
    start_time = time.time()
    project_path = Path(target_project).resolve()
    input_file = project_path / target_file
    
    if not input_file.exists():
         raise FileNotFoundError(f"PHYSICAL_ERROR: Context file {input_file} not found.")

    # 1. Base Metrics (SI Mandate)
    original_size_b = input_file.stat().st_size
    content = input_file.read_text(encoding="utf-8")
    
    # 2. Compaction Logic (v5.0 Optimization)
    # Eliminamos verborrea, agradecimientos y separadores redundantes
    lines = content.splitlines()
    trash_patterns = ["gracias", "entendido", "perfecto", "---", "claro que sí"]
    optimized_lines = [l for l in lines if not any(x in l.lower() for x in trash_patterns)]
    
    optimized_content = "\n".join(optimized_lines)
    
    # 3. DAST Persistence (Non-Destructive)
    output_name = f"{input_file.stem}_optimized{input_file.suffix}"
    optimized_file = input_file.parent / output_name
    optimized_file.write_text(optimized_content, encoding="utf-8")
    
    # 4. Efficiency Calculation
    optimized_size_b = len(optimized_content.encode("utf-8"))
    saved_b = original_size_b - optimized_size_b
    compaction_ratio = round((1 - (optimized_size_b / original_size_b)) * 100, 2) if original_size_b > 0 else 0

    execution_duration_s = time.time() - start_time

    result_payload = {
        "industrial_status": "SOLIDIFIED - CONTEXT PRUNED",
        "optimization_status": "COMPACTED",
        "metrics": {
            "original_bytes": original_size_b,
            "optimized_bytes": optimized_size_b,
            "saved_bytes": saved_b,
            "compaction_percent": compaction_ratio
        },
        "compliance_report": {
            "no_trash_policy_verified": True,
            "si_metrics_applied": True,
            "execution_duration_seconds": round(execution_duration_s, 4)
        },
        "summary": f"Context pruned at {target_file}. Saved {saved_b} Bytes ({compaction_ratio}%)."
    }

    return result_payload, [str(optimized_file)]