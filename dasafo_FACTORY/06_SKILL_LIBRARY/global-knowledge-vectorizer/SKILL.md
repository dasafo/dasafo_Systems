---
version: 3.2.0-S
agent: MEMORY_OPTIMIZER
---

# 🧠 Skill | Global Knowledge Vectorizer

## Objective

Synchronize static Markdown files from the global knowledge base into a Vector Database to enable Retrieval-Augmented Generation (RAG) across all factory agents.

## 🛠️ Interface (v3.2.0-S)

### Input Schema (SkillInput.params)

- `sync_mode` (string, optional): "full" | "incremental". Default "incremental".
- `collection_name` (string, optional): Name of the vector collection.

### Output Schema (SkillOutput.result)

- `chunks_upserted`: (integer) Count of semantic chunks processed.
- `last_sync`: (string) ISO timestamp.
- `index_health`: (string) "OPTIMAL" | "OUT_OF_SYNC".

### ⚖️ Mandato SI (Sistema Internacional)

Cualquier métrica de rendimiento (latencia de embedding en ms, dimensiones de vectores, ocupación de RAM) debe reportarse en el SI.

## 🛡️ Industrial Constraints (Zero-Trust)

- **Vector API Lock:** This skill is physically locked if `PINECONE_API_KEY` or `VECTOR_DB_URL` is missing. Mocks of vector storage are rejected.
- **Physical Scan:** Requires physical file counting from `00_GLOBAL_KNOWLEDGE`.

## Protocol

1. **Scanning:** Periodic scan of `00_GLOBAL_KNOWLEDGE/` for content drift.
2. **Chunking:** Break files into semantic chunks to minimize token noise.
3. **Ingestion:** Upsert chunks with industrial versioning metadata.
4. **Retrieval:** Provide a standardized search interface for the `RESEARCH_AGENT`.

---
*Skill v3.2.0-S | Status: Standardized.*
