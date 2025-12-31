
# Async-Onboarding-Service

A high-performance, asynchronous user onboarding microservice built with **FastAPI**, **RabbitMQ**, **Celery**, and **Redis**.

This project demonstrates how to offload heavy, time-consuming tasks (like PDF generation and email dispatching) to background workers, ensuring the API remains responsive while allowing the client to track progress.

## 🚀 The Architecture

* **FastAPI:** The "Front Desk." Handles incoming requests and status checks.
* **RabbitMQ:** The "Message Broker." Decouples the API from heavy processing.
* **Celery:** The "Worker." Executes background tasks with **Exponential Backoff** logic.
* **Redis:** The "Result Backend." Manages task states and final outputs.
* **Flower:** The "Control Tower." Real-time web dashboard for task monitoring.
* **NGINX Ingress:** The "Gatekeeper." Routes traffic to the correct service via custom local domains.
* **Self-Healing K8s:** Integrated Probes to monitor and recover unhealthy services automatically.

---

## 🛠️ Tech Stack

* **Backend:** FastAPI (Python 3.11)
* **Task Management:** Celery 5.x
* **Brokers/State:** RabbitMQ, Redis
* **Containerization:** Docker, Kubernetes (k8s)
* **Ingress:** NGINX Ingress Controller

---

## 📂 Project Structure

```text
async-onboarding-service/
├── app/
│   ├── main.py            # API Endpoints & Task Status Logic
│   └── tasks.py           # Celery Worker & Retry Logic
├── k8s/                   # Kubernetes Manifests
│   ├── rabbitmq-deployment.yaml
│   ├── redis-deployment.yaml
│   ├── app-deployment.yaml     # Includes Liveness/Readiness Probes
│   ├── flower-deployment.yaml
│   ├── onboarding-secrets.yaml # Encrypted Connection Strings
│   └── ingress.yaml            # NGINX Routing Rules
├── Dockerfile             # Unified image for API/Worker/Flower
├── docker-compose.yml     # Local orchestration
└── requirements.txt       # Project dependencies

```

---

## 🏃 How to Run (Kubernetes)

### 1. Start and Build

```bash
minikube start
minikube addons enable ingress
eval $(minikube docker-env)
docker build -t async-app:latest .

```

### 2. Deploy Infrastructure

```bash
kubectl apply -f k8s/

```

### 3. Setup Local DNS

Map the Minikube IP to your custom domains in your system's `hosts` file:

```text
# Replace <MINIKUBE_IP> with output of 'minikube ip'
<MINIKUBE_IP> api.onboarding.local flower.onboarding.local

```

### 4. Access the Dashboard

* **API Docs:** [http://api.onboarding.local/docs](https://www.google.com/search?q=http://api.onboarding.local/docs)
* **Flower Monitor:** [http://flower.onboarding.local](https://www.google.com/search?q=http://flower.onboarding.local)

---

## 📝 Key Features

* **Self-Healing (Liveness/Readiness):** Kubernetes automatically restarts containers if the API hangs or the Worker loses its RabbitMQ connection.
* **Exponential Backoff Retries:** Handles transient failures by retrying tasks with increasing delays ( seconds).
* **Ingress Routing:** Clean, production-like URLs using NGINX Ingress.
* **Secure Config:** Sensitive URLs and credentials managed via **Kubernetes Secrets**.
* **Fault Tolerance:** `acks_late=True` ensures tasks are re-queued if a worker pod is evicted or crashes.

---
