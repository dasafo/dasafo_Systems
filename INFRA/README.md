# 🛠️ dasafo_FACTORY | Global Infrastructure Services (v3.2.0-S)

## 🌐 Central Node
This directory hosts the shared services for the entire factory ecosystem under the **Modular Toolbox** standard.

### Services:
- **Neo4j**: Graph Database (Central Knowledge Graph)
- **Postgres**: Relational Database (Operational Data)
- **Glances**: Health Monitoring Dashboard

### Usage:
1. `cd dasafo_Systems/INFRA`
2. **Security Gate:** Copy `.env.shared` to `.env` and configure your secure passwords.
   `cp .env.shared .env`
3. Launch the mainframe:
   `docker-compose up -d`
4. Projects will automatically connect via `dasafo_network`.

---
*Infrastructure v3.2.0-S | Status: Solidified.*
