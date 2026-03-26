# 🧠 Skill | NotebookLM Knowledge Nexus (NBLM)
> **Version:** v3.1.5 "Solidity Guard"
> **Agent:** DATA_SCIENTIST

## Objective
Leverage NotebookLM as a secondary technical mind for synthesizing research papers, datasets, and experiment logs.

## Workflow
1.  **Collect:** Import papers from the Research Agent and raw data from the DB.
2.  **Synthesis:** Use `ask_question` to find correlations between recent ArXiv papers and current project constraints.
3.  **Report Generation:** Use `audio_overview_create` or `report_create` to deliver high-level summaries for the PO.

## Integration
All significant findings from NotebookLM must be exported as Markdown to `$TARGET_PROJECT/LOCAL_KNOWLEDGE/synthesis/`.
