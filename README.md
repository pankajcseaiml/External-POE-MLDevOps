# Python Multiplication Program with FastAPI, Jenkins, Pytest, Evidently & MLflow

A minimalist Python project that accepts two numbers and displays their **Multiplication**, integrated with **FastAPI**, **Jenkins**, **Pytest**, **Evidently AI**, and **MLflow**.

---

## Project Structure (Minimal Files)

```text
External-POE/
├── main.py              # Multiplication program (CLI + FastAPI service)
├── evidently_monitor.py # Evidently AI data drift monitoring script
├── requirements.txt     # Python dependencies
├── Dockerfile           # Docker container configuration
├── Jenkinsfile          # Jenkins CI/CD declarative pipeline
├── tests/
│   └── test_main.py     # Pytest unit and API test suite
└── README.md            # Documentation
```

---

## 1. Run Python Multiplication (CLI)

* **Interactive prompt:**
  ```cmd
  python main.py
  ```
* **Command line arguments:**
  ```cmd
  python main.py 6 7
  ```

---

## 2. Run FastAPI Web Service

* **Start server:**
  ```cmd
  python -m uvicorn main:app --reload --port 8000
  ```
* **Open Interactive Docs (Swagger UI):**
  [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
* **API Endpoint:**
  ```cmd
  curl "http://127.0.0.1:8000/multiply?num1=6&num2=7"
  ```

---

## 3. Run Pytest Test Suite

```cmd
python -m pytest -p no:dash -v tests/
```

---

## 4. Run Evidently Tool

Generate data drift and summary report for multiplication inputs and outputs:
```cmd
python evidently_monitor.py
```
Open report:
```cmd
start evidently_report.html
```

---

## 5. MLflow Experiment Tracking

* **Start MLflow UI:**
  ```cmd
  mlflow ui --port 5000
  ```
* **Open Dashboard:**
  [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 6. Docker Container

* **Build image:**
  ```cmd
  docker build -t multiplication-app:latest .
  ```
* **Run container:**
  ```cmd
  docker run --rm multiplication-app:latest
  ```

---

## 7. Jenkins CI/CD Pipeline

* Jenkins URL: `http://localhost:8081`
* Automated stages:
  1. `Checkout Code`
  2. `Install Dependencies`
  3. `Run Pytest`
  4. `Evidently Tool Monitoring`
  5. `Docker Build and Run`
