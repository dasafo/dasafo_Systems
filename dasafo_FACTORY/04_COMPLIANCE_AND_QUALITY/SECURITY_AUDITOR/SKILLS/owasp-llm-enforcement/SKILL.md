# Skill: OWASP LLM Top-10 Enforcement
> **Source:** https://owasp.org/www-project-top-10-for-llm-applications/ (Adapted)
> **Agent:** SECURITY_AUDITOR

## Objective
Specifically address the 10 most critical vulnerabilities in LLM-based applications.

## High-Priority Attacks to Stop
1.  **LLM01: Prompt Injection:** Direct and indirect injections into the model.
2.  **LLM02: Insecure Output Handling:** Preventing XSS or Command Injection vulnerabilities through outputs.
3.  **LLM06: Sensitive Data Disclosure:** Stopping the leakage of proprietary info (e.g. architectural trade-offs to outside parties).
4.  **LLM08: Insecure Plugin Design:** Auditing the `TOOLS.md` and MCP definitions for vulnerabilities.

## Audit Workflow
The Auditor must produce a weekly `SECURITY_ posture.md` report based on these 10 risk vectors.
