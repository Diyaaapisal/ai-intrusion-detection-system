def log_alert(ip):
    with open("alerts.log", "a") as f:
        f.write(f"{ip},Blocked\n")

    print(f"[ALERT] Action taken on {ip}")