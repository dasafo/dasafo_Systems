"""
skill_schema.py — Contrato de datos unificado para todas las Skills de dasafo_FACTORY.

Todos los run.py deben importar SkillInput y SkillOutput desde aquí.
Esto garantiza un contrato explícito y tipado entre el motor de ejecución y cada skill.
"""

from __future__ import annotations

import json
from dataclasses import dataclass, field, asdict
from typing import Any, Dict, List, Optional


@dataclass
class SkillInput:
    """
    Payload de entrada estándar para cualquier skill ejecutable.

    Attributes:
        agent:       ID del agente que invoca la skill (ej: 'orchestrator').
        skill:       Nombre de la skill (ej: 'ra-agile-orchestration').
        params:      Diccionario libre de parámetros específicos de cada skill.
        target_project: Ruta absoluta al proyecto activo. Si es None, se lee de $TARGET_PROJECT.
        correlation_id: ID de trazabilidad para logging distribuido.
    """
    agent: str
    skill: str
    params: Dict[str, Any] = field(default_factory=dict)
    target_project: Optional[str] = None
    correlation_id: Optional[str] = None

    @classmethod
    def from_json(cls, raw: str) -> "SkillInput":
        data = json.loads(raw)
        return cls(
            agent=data["agent"],
            skill=data["skill"],
            params=data.get("params", {}),
            target_project=data.get("target_project"),
            correlation_id=data.get("correlation_id"),
        )

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class SkillOutput:
    """
    Resultado estándar devuelto por cualquier skill ejecutable.

    Attributes:
        success:     True si la skill completó sin errores críticos.
        agent:       ID del agente que ejecutó la skill.
        skill:       Nombre de la skill ejecutada.
        result:      Payload de resultado libre (depende de cada skill).
        artifacts:   Lista de rutas de archivos generados por la skill.
        warnings:    Advertencias no bloqueantes encontradas durante la ejecución.
        error:       Mensaje de error si success=False.
        correlation_id: ID de trazabilidad heredado del SkillInput.
    """
    success: bool
    agent: str
    skill: str
    result: Dict[str, Any] = field(default_factory=dict)
    artifacts: List[str] = field(default_factory=list)
    warnings: List[str] = field(default_factory=list)
    error: Optional[str] = None
    correlation_id: Optional[str] = None

    def to_json(self, indent: int = 2) -> str:
        return json.dumps(asdict(self), indent=indent, ensure_ascii=False)

    @classmethod
    def failure(
        cls,
        agent: str,
        skill: str,
        error: str,
        correlation_id: Optional[str] = None,
    ) -> "SkillOutput":
        """Factory para construir un resultado de error de forma expresiva."""
        return cls(
            success=False,
            agent=agent,
            skill=skill,
            error=error,
            correlation_id=correlation_id,
        )
