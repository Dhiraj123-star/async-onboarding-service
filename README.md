
# Async-Onboarding-Service

A high-performance, asynchronous user onboarding microservice built with **FastAPI**, **RabbitMQ**, **Celery**, and **Redis**.

This project demonstrates how to offload heavy, time-consuming tasks (like PDF generation and email dispatching) to background workers, ensuring the API remains responsive while allowing the client to track progress via polling or monitoring tools.

## 🚀 The Architecture

* **FastAPI:** The "Front Desk." Handles incoming requests and status checks.
* **RabbitMQ:** The "Message Broker." Decouples the API from heavy processing.
* **Celery:** The "Worker." Executes background tasks with **Exponential Backoff** logic.
* **Redis:** The "Result Backend." Manages task states and final outputs.
* **Flower:** The "Control Tower." Provides a real-time web dashboard for task monitoring.
* **Kubernetes (Minikube):** Production-grade orchestration with automated scaling and secret management.

---

## 🛠️ Tech Stack

* **Backend:** FastAPI, Python 3.11
* **Task Management:** Celery 5.x
* **Brokers/State:** RabbitMQ, Redis
* **Containerization:** Docker, Kubernetes (k8s)
* **Monitoring:** Flower

---

## 📂 Project Structure

```text
async-onboarding-service/
├── app/
│   ├── main.py            # API Endpoints & Task Status Logic
│   └── tasks.py           # Celery Worker, Retry Logic & Backend Config
├── k8s/                   # Kubernetes Manifests
│   ├── rabbitmq-deployment.yaml
│   ├── redis-deployment.yaml
│   ├── app-deployment.yaml
│   ├── flower-deployment.yaml
│   └── onboarding-secrets.yaml # Encrypted Connection Strings
├── Dockerfile             # Unified environment for API/Worker
├── docker-compose.yml     # Local orchestration
└── requirements.txt       # Project dependencies

```

---

## 🏃 How to Run

### Option A: Docker Compose (Local Dev)

```bash
docker-compose up --build

```

* **Interactive Docs:** [http://localhost:8000/docs](https://www.google.com/search?q=http://localhost:8000/docs)
* **Flower Dashboard:** [http://localhost:5555](https://www.google.com/search?q=http://localhost:5555)

### Option B: Kubernetes (Minikube)

1. **Start and Build:**
```bash
minikube start
eval $(minikube docker-env)
docker build -t async-app:latest .

```


2. **Deploy Manifests:**
```bash
kubectl apply -f k8s/

```


3. **Access Services:**
```bash
minikube service api-service --url    # For the API
minikube service flower-service --url # For Monitoring

```



---

## 📝 Key Features

* **Exponential Backoff Retries:** Automatically handles transient errors (e.g., API timeouts) by retrying with increasing delays ( seconds).
* **Security:** Uses **Kubernetes Secrets** to decouple sensitive connection strings from deployment logic.
* **Fault Tolerance:** Uses `acks_late=True` and `track_started=True` for reliable task delivery even during worker crashes.
* **Scalability:** Horizontal scaling supported via `kubectl scale deployment onboarding-worker --replicas=5`.

---
