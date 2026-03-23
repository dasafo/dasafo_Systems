# Skill: Deep Semantic Search (Exa)
> **Source:** https://skills.sh/sundial-org/awesome-openclaw-skills/exa-web-search-free
> **Agent:** RESEARCH_AGENT

## Objective
Go beyond keyword search to find semantically relevant technical documentation, research, and high-quality code examples for the ARCHITECT.

## Core Capabilities
- **`web_search_exa`:** Map technical concepts (e.g. "Event-driven architecture using Redis Streams") directly to modern implementations.
- **`get_code_context_exa`:** Find existing open-source code that matches a needed pattern for $TARGET_PROJECT.
- **`company_research_exa`:** Understand how top tier tech companies solve specific scale problems.

## Workflow
1.  **Define Concept:** Break a request into a non-keyword semantic query.
2.  **Filter:** Focus exclusively on technical sources (GitHub, Medium Engineering, ArXiv, Tech Documentation).
3.  **Synthesize:** Connect findings to the current architecture in `$TARGET_PROJECT/LOCAL_KNOWLEDGE/research_nexus.md`.
