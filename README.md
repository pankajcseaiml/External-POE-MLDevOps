# Multiplication Program with FastAPI, Jenkins, Pytest, Docker & Evidently AI

[![FastAPI](https://img.shields.io/badge/FastAPI-0.115+-009688.svg?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
[![Python](https://img.shields.io/badge/Python-3.11%20%7C%203.13-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Jenkins](https://img.shields.io/badge/Jenkins-CI%2FCD%20Automated-red.svg?logo=jenkins&logoColor=white)](https://www.jenkins.io/)
[![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED.svg?logo=docker&logoColor=white)](https://www.docker.com/)
[![Pytest](https://img.shields.io/badge/Pytest-7%20Passed-0A9EDC.svg?logo=pytest&logoColor=white)](https://docs.pytest.org/)
[![Evidently AI](https://img.shields.io/badge/Evidently%20AI-Data%20Drift%20Monitoring-purple.svg)](https://www.evidentlyai.com/)
[![GitHub Repo](https://img.shields.io/badge/GitHub-Internal--POE--MLDevOps-success.svg?logo=github&logoColor=white)](https://github.com/pankajcseaiml/Internal-POE-MLDevOps)

An end-to-end production MLOps/DevOps project based on the problem statement:
> **"Write a Python program to accept two numbers and display its Multiplication. Integrate this program using FastAPI, Jenkins, Pytest, Evidently tool."**

**GitHub Repository:** [https://github.com/pankajcseaiml/Internal-POE-MLDevOps](https://github.com/pankajcseaiml/Internal-POE-MLDevOps)

---

## 📁 Project Architecture & Structure

```text
Internal-POE-MLDevOps/
├── .vscode/
│   ├── settings.json            # VS Code workspace settings & pytest test discovery
│   └── launch.json              # 1-click debug/run profiles (CLI, FastAPI, Pytest, Evidently)
├── tests/
│   ├── test_multiplication.py   # Comprehensive Pytest suite (Core logic & FastAPI endpoints)
│   └── test_hello.py            # Entrypoint integration test
├── main.py                      # Core Python program & FastAPI application
├── hello.py                     # CLI module and default executable entrypoint
├── evidently_monitor.py         # Evidently AI data drift and data quality monitoring
├── Dockerfile                   # Lightweight Docker containerization (python:3.11-slim)
├── Jenkinsfile                  # Jenkins declarative CI/CD pipeline automation
├── requirements.txt             # Production dependencies
├── .gitignore                   # Clean Git ignore configuration
└── README.md                    # Complete technical documentation
```

---

## 🔄 End-to-End Workflow Diagram

```
┌─────────────────────────────────┐
│     Multiplication Program      │
│  (CLI: python main.py <n1> <n2> │
│   API: GET/POST /multiply)      │
└────────────────┬────────────────┘
                 │
                 ▼
     ┌──────────────────────┐
     │  Git / GitHub Repo   │
     └───────────┬──────────┘
                 │ (Triggers)
                 ▼
┌─────────────────────────────────┐
│     Jenkins Declarative CI/CD   │
└────────────────┬────────────────┘
                 │
                 ├─────────────────────────┐
                 │                         │
                 ▼                         ▼
      ┌─────────────────────┐   ┌────────────────────────┐
      │     Pytest Suite    │   │  Evidently AI Monitor  │
      │  (7 Unit/API Tests) │   │ (Data Drift & Quality) │
      └─────────────────────┘   └────────────────────────┘
                 │                         │
                 └────────────┬────────────┘
                              │
                              ▼
                 ┌─────────────────────────┐
                 │     Docker Container    │
                 │   (Build & Run Image)   │
                 └─────────────────────────┘
```

---

## 🚀 Step-by-Step Execution Guide (CMD)

### 1️⃣ Run Core Python Multiplication Program (CLI)
You can provide two numbers directly as arguments or interactively:
```cmd
python main.py 7 8
```
**Output:**
```text
==================================================
       Python Multiplication Program (CLI)        
==================================================
--------------------------------------------------
Calculation: 7.0 x 8.0 = 56.0
Multiplication Result: 56.0
==================================================
```

---

### 2️⃣ Run FastAPI Web Service
Start the FastAPI server using Uvicorn:
```cmd
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```
Once started, test the endpoints in your browser or with `curl`:
* **Swagger Interactive Docs:** [http://localhost:8000/docs](http://localhost:8000/docs)
* **GET Multiplication Endpoint:**  
  ```cmd
  curl "http://localhost:8000/multiply?num1=12.5&num2=4"
  ```
  *Response:* `{"num1": 12.5, "num2": 4.0, "operation": "multiplication", "result": 50.0}`
* **POST Multiplication Endpoint:**  
  ```cmd
  curl -X POST "http://localhost:8000/multiply" -H "Content-Type: application/json" -d "{\"num1\": 9.0, \"num2\": 8.0}"
  ```
  *Response:* `{"num1": 9.0, "num2": 8.0, "operation": "multiplication", "result": 72.0}`

---

### 3️⃣ Run Automated Pytest Suite
Run the 7 unit and API integration tests:
```cmd
python -m pytest -p no:dash -v -s tests/
```
**Output:**
```text
tests/test_hello.py::test_hello_multiplication PASSED
tests/test_multiplication.py::test_core_multiplication_positive PASSED
tests/test_multiplication.py::test_core_multiplication_negative_and_zero PASSED
tests/test_multiplication.py::test_fastapi_root_endpoint PASSED
tests/test_multiplication.py::test_fastapi_get_multiply PASSED
tests/test_multiplication.py::test_fastapi_post_multiply PASSED
tests/test_multiplication.py::test_fastapi_invalid_input PASSED
============================== 7 passed in 0.42s ==============================
```

---

### 4️⃣ Run Evidently AI Monitoring Tool
Monitors incoming multiplication request distributions (`num1`, `num2`, and `multiplication_result`) between baseline traffic and live production traffic to detect data drift:
```cmd
python evidently_monitor.py
start evidently_report.html
```
**Output:**
```text
==================================================
  Evidently AI Tool - Multiplication Monitoring   
==================================================
[INFO] Reference operations: 200 requests (Columns: ['num1', 'num2', 'multiplication_result'])
[INFO] Current production operations: 200 requests
[INFO] Baseline average product:   630.01
[INFO] Production average product: 13559.91
[INFO] Computing Data Drift and Data Summary metrics...
[SUCCESS] Evidently report generated successfully: evidently_report.html
```
*Opens an interactive visual dashboard in your browser displaying distribution curves, p-values, and statistical drift tests!*

---

### 5️⃣ Jenkins CI/CD Automation
The [`Jenkinsfile`](Jenkinsfile) automates the entire lifecycle:
1. **Checkout Code:** Pulls latest commit from GitHub repository.
2. **Install Dependencies:** Installs FastAPI, Uvicorn, Pytest, and Evidently.
3. **Run Pytest:** Executes all unit and API endpoint tests.
4. **Evidently AI Monitoring:** Generates data drift report for multiplication requests.
5. **Docker Build & Run:** Builds and validates the container image.
6. **Artifact Archival:** Archives `evidently_report.html`.

**Trigger Pipeline in Jenkins:**
1. Open [http://localhost:8081](http://localhost:8081).
2. Open job `Internal-POE-MLDevOps` ➔ Click **Build Now**.
3. Inspect the automated stages in **Console Output**.

---

### 6️⃣ Docker Containerization
Build the lightweight Docker container:
```cmd
docker build -t hello-mlops:latest .
```
Run the container:
```cmd
docker run --rm hello-mlops:latest
```
*Output:*
```text
Multiplication of 6.0 and 7.0 is: 42.0
```
Run as a live FastAPI server in Docker:
```cmd
docker run -p 8000:8000 --rm hello-mlops:latest uvicorn main:app --host 0.0.0.0 --port 8000
```
*(Now accessible at [http://localhost:8000/docs](http://localhost:8000/docs))*.

---

## 📊 Summary Checklist

| Component | Implementation | Verification | Status |
| :--- | :--- | :--- | :--- |
| **Multiplication Logic** | `multiply(a, b)` in `main.py` & `hello.py` | CLI & function return | ✅ Verified |
| **FastAPI** | REST API (`/`, `GET /multiply`, `POST /multiply`) | Swagger Docs & TestClient | ✅ Verified |
| **Pytest** | 7 tests in `tests/test_multiplication.py` & `tests/test_hello.py` | `pytest -v` | ✅ 7/7 Passed |
| **Evidently AI** | Input & Output Drift Analysis in `evidently_monitor.py` | `evidently_report.html` | ✅ Verified |
| **Jenkins** | Declarative pipeline in `Jenkinsfile` | Automated multi-stage build | ✅ Configured |
| **Docker** | Containerized FastAPI & CLI app in `Dockerfile` | Image build & container run | ✅ Verified |
