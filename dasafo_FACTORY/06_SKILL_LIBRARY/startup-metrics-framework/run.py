from __future__ import annotations
import sys
import os
import time
import json
from pathlib import Path

# Inyección para resolver dependencias de la factoría
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

try:
    from skill_schema import SkillInput, SkillOutput
except ImportError:
    pass

def run(skill_input: SkillInput) -> SkillOutput:
    """Startup Metrics Framework (v4.0-S) - Financial Engine."""
    start_time = time.time()
    
    agent = skill_input.agent or "PRODUCT_OWNER"
    skill = "startup-metrics-framework"
    cid = skill_input.correlation_id
    params = skill_input.params or {}
    
    target = params.get("target_project") or skill_input.target_project or os.environ.get("TARGET_PROJECT")
    business_model = params.get("business_model", "").upper()
    audience = params.get("target_audience", "General")
    exec_time_s = float(params.get("estimated_execution_s", 1.5))
    
    if not target or not business_model:
        return SkillOutput.failure(agent, skill, "FINANCE_ERROR: Missing target_project or business_model.", cid)

    # 🧮 Lógica de Negocio (Baselines industriales)
    # Asumimos un costo base de $0.0002 por segundo de cómputo en la factoría
    cost_per_execution = round(exec_time_s * 0.0002, 5)
    
    if "B2B" in business_model:
        cac_target = "$150 - $500"
        ltv_target = "$1500+"
        roi_timeline = "6-9 Months"
    elif "B2C" in business_model:
        cac_target = "$5 - $20"
        ltv_target = "$60+"
        roi_timeline = "3-6 Months"
    else:
        cac_target = "TBD based on pilot"
        ltv_target = "3x CAC Minimum"
        roi_timeline = "12 Months"

    payload = (
        f"FINANCIAL_SUCCESS_CRITERIA:\n"
        f"- Unit Economics: LTV to CAC ratio must be >= 3:1.\n"
        f"- Target CAC: {cac_target} | Target LTV: {ltv_target}.\n"
        f"- Infra Cost: Max ${cost_per_execution} per core transaction (based on {exec_time_s}s execution).\n"
        f"- Break-even timeline: {roi_timeline}."
    )

    execution_duration_s = round(time.time() - start_time, 4)
    
    result_payload = {
        "financial_kpis": {
            "model": business_model,
            "cost_per_execution_usd": cost_per_execution,
            "target_cac": cac_target,
            "target_ltv": ltv_target,
            "ltv_cac_ratio_enforced": "3:1"
        },
        "prp_injection_payload": payload,
        "execution_time_s": execution_duration_s
    }
    
    return SkillOutput.success(
        agent, skill, result_payload, [], [], cid, 
        summary=f"Financial baseline generated for {business_model}. LTV/CAC ratio enforced."
    )