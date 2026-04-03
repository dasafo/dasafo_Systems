# 🛠️ dasafo_FACTORY | Global Infrastructure Services (v5.0-MCP)

## 🌐 Central Node (The Power Grid)

This directory hosts the shared services for the entire factory ecosystem under the **Native Industrial Core** standard.

### 🍱 Main Services Stack

- **Supabase (Industrial Hub)**: Managed through cloud (Standard) or self-hosted (Custom).
- **Neo4j (`kg-db`)**: Central Knowledge Graph (Graph-based orchestration).
- **Postgres (`shared-db`)**: Relational Storage for operational metadata.
- **Redis (`cache-node`)**: Fast session and task state caching.
- **Glances**: Real-time performance and health monitoring node (Port 61208).

### 🚀 Usage

1. `cd INFRA`
2. **Security Gate:** Copy `.env.shared` to `.env` and configure your secure credentials.
   `cp .env.shared .env`
3. Launch the mainframe:
   `docker-compose up -d`
4. Projects will automatically connect via the internal `dasafo_network`.

---
*Infrastructure v5.0-MCP | Status: Industrial Core Active.*
