
# Async-Onboarding-Service

A high-performance, asynchronous user onboarding microservice built with **FastAPI**, **RabbitMQ**, **Celery**, and **Redis**.

This project demonstrates how to offload heavy, time-consuming tasks to background workers, ensuring the API remains responsive while allowing the client to track progress.

## 🚀 The Architecture

* **FastAPI:** The "Front Desk." Receives signups and provides status updates.
* **RabbitMQ:** The "Message Broker." Safely queues onboarding tasks.
* **Celery:** The "Worker." Handles heavy lifting with built-in **Exponential Backoff** retries.
* **Redis:** The "Result Backend." Stores the final outcome and status of each task.
* **Flower:** The "Control Tower." Real-time monitoring dashboard for task health.
* **Kubernetes:** Production-ready orchestration using **Minikube**.

## 🛠️ Tech Stack

* **Framework:** FastAPI
* **Task Queue:** Celery (with `amqp` & `redis` transport)
* **Infrastructure:** Docker, Docker Compose, & Kubernetes (k8s)
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
│   └── app-deployment.yaml
├── Dockerfile             # Unified environment for API/Worker
├── docker-compose.yml     # 5-Service Orchestration (API, Worker, Redis, Rabbit, Flower)
└── requirements.txt       # Dependencies

```

---

## 🏃 How to Run

### Option A: Docker Compose (Local Development)

```bash
docker-compose up --build

```

* **API:** [http://localhost:8000/docs](https://www.google.com/search?q=http://localhost:8000/docs)
* **Flower Dashboard:** [http://localhost:5555](https://www.google.com/search?q=http://localhost:5555)

### Option B: Kubernetes (Minikube)

```bash
minikube start
eval $(minikube docker-env)
docker build -t async-app:latest .
kubectl apply -f k8s/

```

---

## 📝 Key Features

* **Exponential Backoff Retries:** Tasks automatically retry on failure (e.g., API timeouts) with increasing wait times.
* **Fault Tolerance:** Implemented `acks_late=True` to ensure tasks aren't lost if a worker crashes.
* **Real-time Monitoring:** Integrated Flower to visualize task success rates and retry counts.
* **K8s Ready:** Optimized manifests with Resource Limits and NodePort services.

---