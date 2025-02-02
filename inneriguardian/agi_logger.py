import json
import time
import requests
import os

LOG_FILE = "logs/agi_logs.json"
GITHUB_REPO = "BeeChains/inneriguardian"
GITHUB_API = f"https://api.github.com/repos/{GITHUB_REPO}/contents/logs/agi_logs.json"
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")  # Store your GitHub PAT as an env variable

def log_ai_decision(decision: str):
    """Logs AI decisions locally and pushes to GitHub"""
    
    # Load existing logs
    try:
        with open(LOG_FILE, "r") as f:
            logs = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        logs = []

    # Add new log
    log_entry = {"timestamp": time.time(), "decision": decision}
    logs.append(log_entry)

    # Save locally
    with open(LOG_FILE, "w") as f:
        json.dump(logs, f, indent=4)

    # Push to GitHub
    headers = {"Authorization": f"token {GITHUB_TOKEN}", "Accept": "application/vnd.github.v3+json"}
    sha = requests.get(GITHUB_API, headers=headers).json().get("sha", "")
    data = {
        "message": "Updated AGI logs",
        "content": json.dumps(logs).encode("utf-8").decode("utf-8"),
        "sha": sha
    }
    requests.put(GITHUB_API, headers=headers, json=data)
    print("✅ AI Log Updated on GitHub")
