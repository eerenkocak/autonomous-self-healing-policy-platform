import os
import time
import subprocess
import urllib.request
from datetime import datetime, timezone

TARGET_URL = os.getenv("TARGET_URL", "http://critical-api:80")
TARGET_CONTAINER = os.getenv("TARGET_CONTAINER", "critical-payment-api")
CHECK_INTERVAL = int(os.getenv("CHECK_INTERVAL", "5"))
INCIDENT_DIR = "/app/incidents"

os.makedirs(INCIDENT_DIR, exist_ok=True)

def check_health():
    try:
        with urllib.request.urlopen(TARGET_URL, timeout=2) as response:
            return response.status == 200
    except Exception:
        return False

def generate_postmortem(incident_id, detected_at, recovered_at, mttr_seconds):
    filename = os.path.join(INCIDENT_DIR, f"POSTMORTEM_{incident_id}.md")
    report = f"""# SRE Automated Incident Post-Mortem: {incident_id}

- **Target Service:** `{TARGET_CONTAINER}`
- **Detection Timestamp (UTC):** {detected_at}
- **Recovery Timestamp (UTC):** {recovered_at}
- **Mean Time To Recovery (MTTR):** {mttr_seconds:.2f} seconds
- **Root Cause:** Service health check failed or container terminated unexpectedly (Chaos Injection / Runtime Fault).
- **Automated Action Taken:** Autonomous Self-Healing Engine executed `docker restart {TARGET_CONTAINER}` and verified HTTP 200 readiness.
- **Status:** RESOLVED (Zero Human Intervention)
"""
    with open(filename, "w", encoding="utf-8") as f:
        f.write(report)
    print(f"[POST-MORTEM] Generated automated SRE report: {filename}", flush=True)

def remediate():
    incident_id = datetime.now(timezone.utc).strftime("INC-%Y%m%d-%H%M%S")
    detected_at = datetime.now(timezone.utc).isoformat()
    start_time = time.time()
    print(f"[ALERT] Health check FAILED for {TARGET_CONTAINER}! Initiating self-healing ({incident_id})...", flush=True)

    subprocess.run(["docker", "restart", TARGET_CONTAINER], check=False)

    # Wait until service responds healthy again
    for _ in range(15):
        time.sleep(1)
        if check_health():
            recovered_at = datetime.now(timezone.utc).isoformat()
            mttr = time.time() - start_time
            print(f"[RECOVERED] {TARGET_CONTAINER} is back ONLINE! MTTR: {mttr:.2f}s", flush=True)
            generate_postmortem(incident_id, detected_at, recovered_at, mttr)
            return

    print(f"[ESCALATION] Automated recovery timed out for {TARGET_CONTAINER}. Escalating to On-Call SRE!", flush=True)

if __name__ == "__main__":
    print(f"Autonomous SRE Self-Healing Engine started. Monitoring {TARGET_CONTAINER}...", flush=True)
    while True:
        if not check_health():
            remediate()
        time.sleep(CHECK_INTERVAL)
