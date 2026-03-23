# Skill: Agentic Thought & Secret Scanner
> **Source:** https://skills.sh/karpathy/nanochat/clutch-qa-security (Adapted)
> **Agent:** SECURITY_AUDITOR

## Objective
Detect accidental secret leakage and internal insecurity within the agents' internal chain-of-thought and logs.

## Audit Checklist
1.  **Thought Scan:** Monitor agent "Thinking" blocks for accidental extraction of hidden architectural secrets.
2.  **Secret Redaction:** If an agent accidentally logs an API key during an error, the Auditor must flag it for immediate rotation and redaction from `LOGS/`.
3.  **Privilege Decay:** Periodically review if an agent has more MCP tool access than it actually uses. Recommend "tool-pruning" in the `AGENT_REGISTRY.md`.

## Goal
Minimize the internal attack surface by enforcing "Least Privilege" and ensuring zero-trace of sensitive credentials.
