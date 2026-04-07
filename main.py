from monitor import monitor_log
from ai_engine import process_line
from responder import log_alert

LOG_FILE = "auth.log"

print("[SYSTEM] Production IDS started...")

for line in monitor_log(LOG_FILE):

    result = process_line(line)

    if result:
        log_alert(result["ip"])