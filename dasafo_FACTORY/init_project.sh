#!/bin/bash

# ==============================================================================
# dasafo_FACTORY | Project Initializer (Bootstrap) v3.1
# ==============================================================================
# This script provisions the strict $TARGET_PROJECT skeleton mandated by the 
# COMMUNICATION_PROTOCOL.md and UNIVERSAL_PIPELINE.md.
#
# Usage: ./init_project.sh <PROJECT_NAME>
# ==============================================================================

set -e

if [ -z "$1" ]; then
    echo "ERROR: Target project name is required."
    echo "Usage: ./init_project.sh <PROJECT_NAME>"
    exit 1
fi

PROJECT_ROOT="../../PROJECTS/$1"

echo "[*] Initializing factory skeleton for project: $1"

# 1. Create CORE skeleton architecture
mkdir -p "$PROJECT_ROOT/LOCAL_KNOWLEDGE"
mkdir -p "$PROJECT_ROOT/LOGS/agents"
mkdir -p "$PROJECT_ROOT/LOGS/sessions"
mkdir -p "$PROJECT_ROOT/LOGS/reports"
mkdir -p "$PROJECT_ROOT/LOGS/incidents"
mkdir -p "$PROJECT_ROOT/TASKS/01_PENDING"
mkdir -p "$PROJECT_ROOT/TASKS/02_IN_PROGRESS"
mkdir -p "$PROJECT_ROOT/TASKS/03_COMPLETED"
mkdir -p "$PROJECT_ROOT/TASKS/04_ARCHIVE"
mkdir -p "$PROJECT_ROOT/TASKS/05_REJECTED"
mkdir -p "$PROJECT_ROOT/WORKSPACE/backend"
mkdir -p "$PROJECT_ROOT/WORKSPACE/frontend"
mkdir -p "$PROJECT_ROOT/WORKSPACE/shared"

# 2. Initialize mandatory State & Memory constructs
# Meta-Agent State
cat <<EOF > "$PROJECT_ROOT/PROJECT_STATE.json"
{
  "factory_version": "3.1.0-INFRA",
  "project_status": "DISCOVERY",
  "objective": "",
  "phases": {
    "M1": "PENDING",
    "M2": "PENDING",
    "M3": "PENDING",
    "M4": "PENDING",
    "M5": "PENDING"
  }
}
EOF

# Semantic Memory Index (for MEMORY_OPTIMIZER)
echo "# Semantic Context Index" > "$PROJECT_ROOT/LOCAL_KNOWLEDGE/SEMANTIC_INDEX.md"

# Global Error & Execution Logs (with Lock placeholder)
echo "# Master Error Report" > "$PROJECT_ROOT/LOGS/ERROR_REPORT.md"
echo "task_id | status | timestamp | sequence_id | owner_agent_id" > "$PROJECT_ROOT/LOGS/EXECUTION_LOG.md"
touch "$PROJECT_ROOT/LOGS/EXECUTION_LOG.lock"

# 3. Seed the PRP_CONTRACT (Draft)
cat <<EOF > "$PROJECT_ROOT/LOCAL_KNOWLEDGE/PRP_CONTRACT.json"
{
  "project": "$1",
  "version": "1.0.0",
  "prp_status": "draft",
  "validated_at": null,
  "validated_by": null,
  "vision": {
    "what": "TBD",
    "why": "TBD",
    "who": "TBD"
  },
  "success_criteria": [],
  "constraints": [],
  "non_goals": []
}
EOF

# 4. Infrastructure Hint (v3.1)
echo "DOCKER_NETWORK=dasafo_network" > "$PROJECT_ROOT/.env"
echo "NEO4J_URI=bolt://dasafo-shared-kg:7687" >> "$PROJECT_ROOT/.env"

echo "[+] Directory structure created dynamically at: $PROJECT_ROOT"
echo "[+] PRP Contract seeded at: LOCAL_KNOWLEDGE/PRP_CONTRACT.json"
echo "[+] Environment hints for Infrav3.1 added to .env"
echo "[+] SUCCESS: Factory ready for Phase 1 (Discovery)"
