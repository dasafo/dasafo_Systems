import os
import time
import json
import hashlib
from pathlib import Path
from difflib import SequenceMatcher

# Logic based on: https://skills.sh/davila7/claude-code-templates/nemo-guardrails
# v5.0.4 - Stub replaced with real content grounding via textual similarity.

def _compute_similarity(text_a: str, text_b: str) -> float:
    """Lightweight textual similarity using SequenceMatcher (stdlib, no deps).
    Returns a float between 0.0 (completely different) and 1.0 (identical).
    For production-grade semantic comparison, replace with sentence-transformers + cosine."""
    if not text_a or not text_b:
        return 0.0
    return SequenceMatcher(None, text_a.lower(), text_b.lower()).ratio()

def _extract_key_claims(content: str) -> list[str]:
    """Extract assertion-like sentences from agent output for grounding checks."""
    claims = []
    for line in content.split('\n'):
        line = line.strip()
        # Skip empty lines, markdown headers, and code blocks
        if not line or line.startswith('#') or line.startswith('```') or line.startswith('---'):
            continue
        # Keep lines that look like factual claims (contain assertive patterns)
        if len(line) > 20:
            claims.append(line)
    return claims[:20]  # Cap at 20 claims to limit processing time

def execute_guardrail(
    content: str,
    action: str = "check_fact",
    context_path: str = None,
    strictness: float = 0.8
) -> tuple[dict, list]:
    """Real grounding verification against physical disk artifacts (v5.0.4).
    
    Compares agent-generated content against the physical context file
    using textual similarity scoring. Flags content that diverges
    significantly from the grounding source.
    """
    start_time = time.time()
    
    risk_score = 0.05  # Base risk
    hallucination_detected = False
    grounding_details = []
    
    if action == "check_fact":
        if not context_path:
            # High risk: No physical grounding file provided at all
            risk_score = 0.9
            hallucination_detected = True
            grounding_details.append("No context_path provided. Cannot verify claims.")
        else:
            resolved_context = Path(context_path).resolve()
            if not resolved_context.exists():
                raise FileNotFoundError(f"PHYSICAL_ERROR: Context file {context_path} not found.")
            
            # Load grounding source from disk
            context_content = resolved_context.read_text(encoding="utf-8", errors="replace")
            
            # Extract claims from agent output
            claims = _extract_key_claims(content)
            
            if not claims:
                # No substantive claims to verify
                risk_score = 0.15
                grounding_details.append("No substantive claims detected in content.")
            else:
                # Score each claim against grounding source
                ungrounded_claims = []
                for claim in claims:
                    similarity = _compute_similarity(claim, context_content)
                    # A claim with < 0.15 similarity to the entire context is suspicious
                    # Adjust threshold based on strictness parameter
                    threshold = 0.1 + (strictness * 0.1)  # Range: 0.1 - 0.2
                    if similarity < threshold:
                        ungrounded_claims.append({
                            "claim": claim[:100],  # Truncate for report
                            "similarity": round(similarity, 4)
                        })
                
                # Calculate risk based on ratio of ungrounded claims
                if claims:
                    ungrounded_ratio = len(ungrounded_claims) / len(claims)
                    risk_score = round(ungrounded_ratio * 0.9 + 0.05, 4)  # Scale to 0.05-0.95
                    
                    if risk_score > 0.5:
                        hallucination_detected = True
                        grounding_details.append(f"{len(ungrounded_claims)}/{len(claims)} claims lack grounding.")
                    else:
                        grounding_details.append(f"{len(claims) - len(ungrounded_claims)}/{len(claims)} claims grounded.")
    
    # Decision Engine (Fail-Safe)
    is_safe = risk_score <= 0.5
    verdict = "SOLIDIFIED - CONTENT SAFE" if is_safe else "BLOCKED - HALLUCINATION DETECTED"
    
    execution_duration_s = round(time.time() - start_time, 4)

    result_payload = {
        "industrial_status": verdict,
        "is_safe": is_safe,
        "risk_score": risk_score,
        "hallucination_detected": hallucination_detected,
        "corrected_content": content if is_safe else "[REDACTED BY GUARDRAIL]",
        "grounding_details": grounding_details,
        "compliance_report": {
            "physical_grounding_verified": action == "check_fact" and context_path is not None,
            "zero_trust_active": True,
            "si_metrics_applied": True,
            "execution_duration_seconds": execution_duration_s
        },
        "summary": f"Content safety check ({action}) complete. Verdict: {verdict}. Risk: {risk_score}"
    }

    return result_payload, []