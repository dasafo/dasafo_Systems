#!/bin/bash

# ==============================================================================
# dasafo_FACTORY | Project Initializer (Bootstrap)
# ==============================================================================
# This script provisions the strict $TARGET_PROJECT skeleton mandated by the factory.
# Usage: ./init_project.sh <PROJECT_NAME>
# ==============================================================================

set -e

if [ -z "$1" ]; then
    echo "ERROR: Target project name is required."
    echo "Usage: ./init_project.sh <PROJECT_NAME>"
    exit 1
fi

PROJECT_ROOT="../PROJECTS/$1"

echo "[*] Initializing factory skeleton for project: $1"

# Create core skeleton architecture
mkdir -p "$PROJECT_ROOT/LOCAL_KNOWLEDGE"
mkdir -p "$PROJECT_ROOT/LOGS/agents"
mkdir -p "$PROJECT_ROOT/LOGS/sessions"
mkdir -p "$PROJECT_ROOT/TASKS/01_PENDING"
mkdir -p "$PROJECT_ROOT/TASKS/02_IN_PROGRESS"
mkdir -p "$PROJECT_ROOT/TASKS/03_COMPLETED"
mkdir -p "$PROJECT_ROOT/TASKS/04_ARCHIVE"
mkdir -p "$PROJECT_ROOT/TASKS/05_REJECTED"
mkdir -p "$PROJECT_ROOT/WORKSPACE/backend"
mkdir -p "$PROJECT_ROOT/WORKSPACE/frontend"
mkdir -p "$PROJECT_ROOT/WORKSPACE/shared"

# Initialize consolidated project state and Meta-Agent memory constructs
echo '{"factory_status": "PENDING", "objective": "", "phases": {"M1": "PENDING", "M2": "PENDING", "M3": "PENDING", "M4": "PENDING", "M5": "PENDING"}}' > "$PROJECT_ROOT/PROJECT_STATE.json"
echo "# Semantic Context Index" > "$PROJECT_ROOT/LOCAL_KNOWLEDGE/SEMANTIC_INDEX.md"
echo "# Master Error Report" > "$PROJECT_ROOT/LOGS/ERROR_REPORT.md"
echo "task_id | status | timestamp" > "$PROJECT_ROOT/LOGS/EXECUTION_LOG.md"

echo "[+] Directory structure created dynamically at: $PROJECT_ROOT"
echo "[+] SUCCESS: Ready for Phase 1 (Discovery)"
