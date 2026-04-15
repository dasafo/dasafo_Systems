---
name: ephemeral-code-execution
description: Use this skill to execute arbitrary Python or Bash code directly on the factory server in a sandbox environment.
compatibility: python3, bash
---
# Ephemeral Code Execution (Nivel 1)
An implementation of the "Code Execution via MCP" pattern for sandboxed logic.
<!-- LEVEL_1_END -->

## Usage Guide (Nivel 2)
1. Inject the code payload directly in `code_payload`.
2. Specify the `language` ("python" or "bash").
3. View the combined STDOUT/STDERR in the response.

## Parameters
- `target_project` (string): Path to the project root.
- `agent` (string): Your assigned role.
- `language` (string): "python" or "bash".
- `code_payload` (string): Raw code text.
<!-- LEVEL_2_END -->

## Internal Mechanics (Nivel 3)
1. Generates an isolated temporary file.
2. Invokes an isolated subprocess with a strict CPU timeout.
3. Captures output from STDOUT and STDERR.
4. Cleans up artifacts immediately.
5. Logs execution for DAST compliance.
