from flask import Flask, jsonify, render_template
import os

app = Flask(__name__)

def read_alerts():
    alerts = []
    if not os.path.exists("alerts.log"):
        return alerts

    with open("alerts.log", "r") as f:
        for line in f:
            ip, status = line.strip().split(",")
            alerts.append({"ip": ip, "status": status})
    return alerts


@app.route("/")
def dashboard():
    return render_template("dashboard.html")

@app.route("/alerts")
def alerts():
    return jsonify(read_alerts())


if __name__ == "__main__":
    app.run(debug=True)