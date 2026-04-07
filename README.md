# 🚀 AI-Based Intrusion Detection System

## 📌 Overview
This project is a production-style Intrusion Detection System (IDS) that monitors authentication logs in real-time, detects brute-force attacks using adaptive AI logic, and visualizes alerts through a web dashboard.

---

## ⚙️ Features
- Real-time log monitoring
- Adaptive anomaly detection (auto-learning)
- Brute-force attack detection
- Automated alert logging
- Live dashboard using Flask API

---

## 🧠 Architecture
Logs → Monitor → AI Engine → Responder → API → Dashboard


---

## 🛠️ Tech Stack
- Python
- Flask
- JSON (for learning history)

---

## 🚀 How to Run

### 1. Install dependencies
pip install -r requirements.txt


### 2. Start IDS Engine

python main.py


### 3. Start Dashboard

python api.py

### 4. Open browser

http://127.0.0.1:5000


---

## 🧪 Simulate Attack

echo Failed password from 192.168.1.99 >> auth.log


---

## 🧠 Key Concept
This system uses adaptive learning instead of fixed thresholds. It builds a behavioral baseline for each IP and detects anomalies dynamically.

---

## 📌 Resume Statement
**Built a production-style AI-based Intrusion Detection System