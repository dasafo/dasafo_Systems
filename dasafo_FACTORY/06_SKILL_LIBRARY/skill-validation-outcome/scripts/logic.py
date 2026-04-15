import json
from pathlib import Path
from deepeval.metrics import GEval
from deepeval.test_case import LLMTestCase, LLMTestCaseParams

def validate_outcome(target_project: str, target_skill: str, input_payload: str, actual_output: str, min_similarity: float = 0.8):
    """
    Compara el output usando LLM-as-a-Judge (DeepEval) contra el Golden Dataset (v5.2-MCP).
    """
    factory_root = Path(__file__).resolve().parent.parent.parent.parent
    dataset_dir = factory_root / "04_COMPLIANCE_AND_QUALITY" / "VALIDATION" / "GOLDEN_DATASETS"
    expectation_file = dataset_dir / f"EXPECTATION_{target_skill}.json"
    
    if not expectation_file.exists():
        return {"success": False, "error": f"Golden Dataset not found for {target_skill}", "industrial_status": "MISSING_DATASET"}, []

    try:
        with open(expectation_file, 'r', encoding='utf-8') as f:
            expectations = json.load(f)
            
        expected_str = json.dumps(expectations.get("expected_output", {}), sort_keys=True)
        
        # Métrica GEval: Evalúa la fidelidad semántica y penaliza alucinaciones
        correctness_metric = GEval(
            name="Semantic Correctness",
            criteria="Determine if the actual output fulfills the exact same technical constraints and logic as the expected output, without hallucinating extra features.",
            evaluation_params=[LLMTestCaseParams.INPUT, LLMTestCaseParams.ACTUAL_OUTPUT, LLMTestCaseParams.EXPECTED_OUTPUT],
        )
        
        test_case = LLMTestCase(
            input=str(input_payload),
            actual_output=str(actual_output),
            expected_output=expected_str
        )
        
        correctness_metric.measure(test_case)
        passed = correctness_metric.is_successful()
        
        result = {
            "success": passed,
            "similarity_score": round(correctness_metric.score, 4),
            "reason": correctness_metric.reason,  # El LLM explica POR QUÉ falló
            "target_skill": target_skill,
            "industrial_status": "VALIDATED" if passed else "VALIDATION_FAILED",
            "summary": f"DeepEval validation {'PASSED' if passed else 'FAILED'} with score {correctness_metric.score}"
        }
        return result, [str(expectation_file)]
        
    except Exception as e:
        return {"success": False, "error": str(e)}, []
