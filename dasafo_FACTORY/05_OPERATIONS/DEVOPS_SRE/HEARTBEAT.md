# dasafo_System | Operations Pulse
> **Version:** v3.1.5 "Solidity Guard"
>
> **Function:** Continuous Resource & Uptime Monitoring.

## ⏱️ Pulse Frequency

- **Check Interval:** Every 15 minutes.
- **Target:** System Resources & Service Endpoints.

## 💓 Routine

1. **Endpoint Ping:** Verify that the Backend API returns a 200 OK status.
2. **Metrics Collection:** Record CPU and Memory usage in `LOGS/agents/devops_sre.log`.
3. **Log Rotation:** Archive logs larger than 50MB to keep the system clean.
4. **Alerting:** If a service is down, move an URGENT task to `TASKS/01_PENDING` for the ARCHITECT.
