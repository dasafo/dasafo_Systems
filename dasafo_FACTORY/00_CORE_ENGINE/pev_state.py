from typing import TypedDict, Annotated, List
import operator

class OrchestratorState(TypedDict):
    task_id: str
    target_project: str
    task_type: str
    plan_docs: str
    rule_inj_neo4j: List[str]
    draft_artifacts: Annotated[List[str], operator.add]
    execution_stdout: str
    review_notes: Annotated[List[str], operator.add]
    reviewer_pass: bool
    security_alerts: Annotated[List[str], operator.add]
    security_verdict: bool
    revision_count: int
    is_emergency: bool
    required_skill: str
    complexity: int # 1-10 (ROI Engine input)
    model_endpoint: str # CLOUD_LLM o LOCAL_LLM
    quality_score: float # Métrica de DeepEval
    security_breaches: int # Recuento de hallazgos críticos
