import os
from qdrant_client import QdrantClient

class SemanticMemory:
    def __init__(self):
        url = os.getenv("QDRANT_URL", "http://localhost:6333")
        self.client = QdrantClient(url=url)

    async def search(self, task_id: str):
        # Lógica de búsqueda vectorial (emulada hasta tener embeddings)
        return f"Experiencia previa para {task_id}: Sin registros conflictivos."
