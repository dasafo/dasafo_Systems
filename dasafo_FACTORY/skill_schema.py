"""
skill_schema.py — Definición de contratos para Skills (v3.4.0-S).
Define las estructuras de entrada y salida obligatorias para todas las skills industriales.
"""

from __future__ import annotations
import json
from dataclasses import dataclass, field, asdict
from typing import Any, Dict, List, Optional

@dataclass
class SkillInput:
    """Contrato de entrada para todas las skills del Top 18 Hub."""
    agent: str = ""
    skill: str = ""
    params: Dict[str, Any] = field(default_factory=dict)
    target_project: Optional[str] = None
    correlation_id: Optional[str] = None
    isolation_guard: bool = False

    @classmethod
    def from_json(cls, raw: str) -> "SkillInput":
        data = json.loads(raw)
        return cls(
            agent=data.get("agent", ""),
            skill=data.get("skill", ""),
            params=data.get("params", {}),
            target_project=data.get("target_project"),
            correlation_id=data.get("correlation_id"),
            isolation_guard=data.get("isolation_guard", False),
        )

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)

@dataclass
class SkillOutput:
    """Contrato de salida industrial. Éxito, Resultados y Artefactos físicos."""
    success: bool = False
    agent: str = ""
    skill: str = ""
    result: Dict[str, Any] = field(default_factory=dict)
    artifacts: List[str] = field(default_factory=list)
    warnings: List[str] = field(default_factory=list)
    error: Optional[str] = None
    correlation_id: Optional[str] = None

    def to_json(self, indent: int = 2) -> str:
        data = asdict(self)
        return json.dumps(data, indent=indent, ensure_ascii=False)

    @classmethod
    def success(cls, agent: str, skill: str, result: Optional[Dict[str, Any]] = None, artifacts: Optional[List[str]] = None, warnings: Optional[List[str]] = None, correlation_id: Optional[str] = None, **kwargs) -> "SkillOutput":
        # Retrocompatibilidad con skills antiguas que usan 'data'
        res = result or kwargs.get("data") or {}
        return cls(success=True, agent=agent, skill=skill, result=res, artifacts=artifacts or [], warnings=warnings or [], correlation_id=correlation_id)

    @classmethod
    def failure(cls, agent: str, skill: str, error: str, correlation_id: Optional[str] = None) -> "SkillOutput":
        return cls(success=False, agent=agent, skill=skill, error=error, correlation_id=correlation_id)
