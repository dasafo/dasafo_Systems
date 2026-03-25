"""
run.py — Resilient Error Handling (BACKEND_DEV)
Injects robust exception wrappers and retry logic.
v2.1: Project-agnostic.
"""

from skill_schema import SkillInput, SkillOutput

def run(skill_input: SkillInput) -> SkillOutput:
    """
    Generates a resilient wrapper for external calls.
    """
    service_name = skill_input.params.get("service", "external_api")
    
    wrapper = f"async def resilient_{service_name}_call(self, payload: Dict):\n"
    wrapper += f"    try:\n"
    wrapper += f"        return await self._call_with_retry(payload)\n"
    wrapper += f"    except ConnectionError as e:\n"
    wrapper += f"        # v2.1: Log to AutoShield and propagate\n"
    wrapper += f"        raise ServiceUnavailable(f'{service_name} failed') from e\n"
    
    return SkillOutput.success(
        agent=skill_input.agent,
        skill=skill_input.skill,
        data={"wrapper_code": wrapper},
        correlation_id=skill_input.correlation_id
    )
