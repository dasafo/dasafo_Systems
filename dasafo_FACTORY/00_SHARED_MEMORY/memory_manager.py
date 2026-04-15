import os
import sys

# Permitir importaciones relativas dentro de 00_SHARED_MEMORY
sys.path.append(os.path.dirname(__file__))

from .semantic.vector_store import SemanticMemory
from .episodic.redis_checkpointer import EpisodicMemory
from .procedural.neo4j_engram import ProceduralMemory

class UnifiedMemory:
    def __init__(self):
        self.semantic = SemanticMemory()   # Qdrant/Chroma
        self.episodic = EpisodicMemory()   # Redis
        self.procedural = ProceduralMemory() # Neo4j

    async def get_full_context(self, task_id: str, phase: str):
        # 1. Trae las "Reglas de Oro" de la fase (Neo4j)
        rules = self.procedural.get_rules(phase)
        # 2. Trae experiencias similares (Vector DB)
        past_experience = await self.semantic.search(task_id)
        
        return {
            "golden_rules": rules,
            "past_experience": past_experience
        }

memory_manager = UnifiedMemory()
