import json
import os
import re

HISTORY_FILE = "history.json"

def load_history():
    if not os.path.exists(HISTORY_FILE):
        return {}
    with open(HISTORY_FILE, "r") as f:
        return json.load(f)

def save_history(history):
    with open(HISTORY_FILE, "w") as f:
        json.dump(history, f, indent=4)

def extract_ip(line):
    match = re.search(r"\d+\.\d+\.\d+\.\d+", line)
    return match.group() if match else None


def process_line(line):
    history = load_history()

    if "Failed password" not in line:
        return None

    ip = extract_ip(line)
    if not ip:
        return None

    # Learning
    past = history.get(ip, {"avg": 0, "count": 0})
    new_count = past["count"] + 1
    new_avg = ((past["avg"] * past["count"]) + 1) / new_count

    history[ip] = {"avg": new_avg, "count": new_count}
    save_history(history)

    # Detection
    if past["count"] > 3 and 1 > (past["avg"] * 2):
        return {"ip": ip, "status": "Blocked"}

    return None