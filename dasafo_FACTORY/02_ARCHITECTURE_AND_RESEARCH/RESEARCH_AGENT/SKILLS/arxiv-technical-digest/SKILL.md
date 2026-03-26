# 📚 Skill | ArXiv Technical Digest
> **Version:** v3.1.5 "Solidity Guard"
> **Source:** https://skills.sh/karpathy/nanochat/read-arxiv-paper
> **Agent:** RESEARCH_AGENT

## Objective
Fetch and digest the technical core of scientific papers by analyzing their LaTeX source code, not just the PDF.

## Protocol
1.  **Normalize:** Identify the ArXiv ID and point to the `/src/` endpoint.
2.  **Fetch Source:** Download and unpack the tar.gz archive to a local cache.
3.  **Trace Logic:** Find the `main.tex` and follow includes to recreate the full logic (especially equations and algorithms).
4.  **Summary Generation:** Produce a technical breakdown in `$TARGET_PROJECT/LOCAL_KNOWLEDGE/research/PAPER_SUMMARY_{TAG}.md`.

## Output Focus
Focus on **formulas**, **pseudocode**, and **limitations**. The goal is to give the Architect actionable math and logic for implementation.
