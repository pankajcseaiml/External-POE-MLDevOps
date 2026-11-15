# Python Arithmetic Program (Add, Subtract, Multiply, Divide)
### Integrated with FastAPI, Jenkins, Pytest, Evidently AI, MLflow & Git

A minimalist, single-file Python project that accepts two numbers and calculates all 4 arithmetic operations:
* **A. Addition** (`num1 + num2`)
* **B. Subtraction** (`num1 - num2`)
* **C. Multiplication** (`num1 * num2`)
* **D. Division** (`num1 / num2`)

---

## Project Structure (Minimal Code)

```text
External-POE/
├── main.py                   # Core program (CLI + FastAPI service)
├── evidently_monitor.py      # Evidently AI drift monitoring
├── train_and_track_mlflow.py # MLflow experiment tracking
├── requirements.txt          # Python dependencies
├── Dockerfile                # Docker container configuration
├── Jenkinsfile               # Jenkins CI/CD declarative pipeline
├── tests/
│   └── test_main.py          # Pytest unit & API test suite
└── README.md                 # Complete documentation
```

---

## 1. Run Python Arithmetic CLI (A, B, C, D)

* **Interactive prompt:**
  ```cmd
  python main.py
  ```
* **Command line arguments (e.g. 20 and 5):**
  ```cmd
  python main.py 20 5
  ```
  *Output:*
  ```text
  Addition:       20.0 + 5.0 = 25.0
  Subtraction:    20.0 - 5.0 = 15.0
  Multiplication: 20.0 * 5.0 = 100.0
  Division:       20.0 / 5.0 = 4.0
  ```

---

## 2. Run FastAPI Web Service

* **Start server (port 8000):**
  ```cmd
  python -m uvicorn main:app --reload --port 8000
  ```
* **Open Interactive Swagger Documentation:**
  [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
* **Endpoints:**
  * **All operations at once:** `curl "http://127.0.0.1:8000/?num1=20&num2=5"`
  * **A. Addition:** `curl "http://127.0.0.1:8000/add?num1=20&num2=5"`
  * **B. Subtraction:** `curl "http://127.0.0.1:8000/subtract?num1=20&num2=5"`
  * **C. Multiplication:** `curl "http://127.0.0.1:8000/multiply?num1=20&num2=5"`
  * **D. Division:** `curl "http://127.0.0.1:8000/divide?num1=20&num2=5"`

---

## 3. Run Pytest Test Suite

* **Run all tests (covers Add, Subtract, Multiply, Division, and Division-by-Zero):**
  ```cmd
  python -m pytest -p no:dash -v tests/
  ```

---

## 4. Run Evidently AI Data Drift Monitoring

* **Generate report:**
  ```cmd
  python evidently_monitor.py
  ```
* **Open report:**
  ```cmd
  start evidently_report.html
  ```

---

## 5. MLflow Experiment Tracking

* **Log runs for all 4 operations:**
  ```cmd
  python train_and_track_mlflow.py
  ```
* **Start MLflow UI:**
  ```cmd
  mlflow ui --port 5000
  ```
* **Open Dashboard:**
  [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 6. Git Version Control

* **Stage and commit changes:**
  ```cmd
  git add -A
  git commit -m "feat: implement Add, Subtract, Multiply, Division with FastAPI, Pytest, Evidently, MLflow, Jenkins"
  ```
* **Push to GitHub:**
  ```cmd
  git push origin main
  ```

---

## 7. Jenkins CI/CD Pipeline

* Jenkins URL: `http://localhost:8081`
* Automated stages:
  1. `Checkout Code`
  2. `Install Dependencies`
  3. `Run Pytest` (tests Add, Sub, Mul, Div)
  4. `Evidently Tool Monitoring`
  5. `MLflow Tracking`
  6. `Docker Build and Run`

---

## 8. Docker Container

* **Build image:**
  ```cmd
  docker build -t arithmetic-app:latest .
  ```
* **Run container:**
  ```cmd
  docker run --rm arithmetic-app:latest
  ```
