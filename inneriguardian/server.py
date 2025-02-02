from flask import Flask, request, jsonify
import json
import time
import os
import dns.resolver
from agi_model import query_agi  # Calls GPT-4, Bittensor, etc.

app = Flask(__name__)
LOG_FILE = "logs/agi_logs.json"

# =============================
# 🔹 Fetch AI Logs from Handshake Blockchain (HNSD)
# =============================
@app.route("/api/hns_logs", methods=["GET"])
def get_hns_logs():
    """ Fetch AI logs stored in Handshake DNS """
    resolver = dns.resolver.Resolver()
    resolver.nameservers = ["127.0.0.1"]  # Local hnsd resolver
    try:
        logs = resolver.resolve("AGI-logs.iinc", "TXT")
        return jsonify({"logs": [log.to_text() for log in logs]})
    except dns.resolver.NoAnswer:
        return jsonify({"error": "No logs found on Handshake DNS"}), 404

# =============================
# 🔹 Store AI Conversations in Local JSON File + GitHub Sync
# =============================
def log_conversation(user_input, ai_response):
    """ Logs AI interactions to a file & GitHub """
    log_entry = {
        "timestamp": time.time(),
        "user_input": user_input,
        "agi_response": ai_response
    }
    
    # Load existing logs
    try:
        with open(LOG_FILE, "r") as f:
            logs = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        logs = []

    logs.append(log_entry)
    
    # Save to local file
    with open(LOG_FILE, "w") as f:
        json.dump(logs, f, indent=4)

@app.route("/api/query", methods=["POST"])
def agi_query():
    """ AI Query Endpoint: User Sends Query → AGI Responds """
    data = request.get_json()
    user_input = data.get("query", "")
    
    if not user_input:
        return jsonify({"error": "No query provided"}), 400

    # Query AGI (GPT-4, Bittensor, O3-mini)
    ai_response = query_agi(user_input)
    
    # Log the conversation
    log_conversation(user_input, ai_response)
    
    return jsonify({"reply": ai_response})

# =============================
# 🔹 Run Flask Server
# =============================
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
