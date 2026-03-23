---
description: Sychronizes static Markdown files from 00_GLOBAL_KNOWLEDGE to a Vector DB for RAG.
---

# 🧠 SKILL: global-knowledge-vectorizer

1. **Source Scanning:** Periodic scan of `00_GLOBAL_KNOWLEDGE/` for changes in MD files.
2. **Knowledge Chunking:** Break down large files into semantic chunks to avoid token bloat.
3. **Vector Ingestion:** Upsert chunks to the local or cloud Vector DB (Chroma/Pinecone) using MCP.
4. **Metadata Tagging:** Ensure each chunk is tagged with its original file and version ID.
5. **Retrieval Ready:** Provide a search interface for other agents to query specific rules without reading full files.
