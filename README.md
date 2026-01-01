
# Async-Onboarding-Service

A high-performance, asynchronous user onboarding microservice built with **FastAPI**, **RabbitMQ**, **Celery**, and **Redis**.

This project demonstrates how to offload heavy, time-consuming tasks (like PDF generation and email dispatching) to background workers, ensuring the API remains responsive while allowing the client to track progress.

## 🚀 The Architecture

* **FastAPI:** The "Front Desk." Handles incoming requests and status checks.
* **RabbitMQ:** The "Message Broker." Decouples the API from heavy processing.
* **Celery:** The "Worker." Executes background tasks with **Exponential Backoff** logic.
* **Redis:** The "Result Backend." Manages task states and final outputs.
* **Flower:** The "Control Tower." Real-time web dashboard for task monitoring.
* **NGINX Ingress:** The "Gatekeeper." Routes traffic and manages **SSL/TLS termination**.
* **Self-Healing K8s:** Integrated **Liveness and Readiness Probes** for automated recovery.
* **CI/CD Pipeline:** Fully automated build-and-deploy workflow via **GitHub Actions**.

---

## 🛠️ Tech Stack

* **Backend:** FastAPI (Python 3.11)
* **Task Management:** Celery 5.x
* **Brokers/State:** RabbitMQ, Redis
* **Containerization:** Docker & Docker Hub (`dhiraj918106/async-app`)
* **Orchestration:** Kubernetes (k8s)
* **CI/CD:** GitHub Actions
* **Ingress:** NGINX Ingress Controller

---

## 📂 Project Structure

```text
async-onboarding-service/
├── .github/workflows/
│   └── deploy.yml         # GitHub Actions CI/CD Pipeline
├── app/
│   ├── main.py            # API Endpoints & Task Status Logic
│   └── tasks.py           # Celery Worker & Retry Logic
├── k8s/                   # Kubernetes Manifests
│   ├── rabbitmq-deployment.yaml
│   ├── redis-deployment.yaml
│   ├── app-deployment.yaml     # Uses ImagePullPolicy: Always
│   ├── flower-deployment.yaml
│   ├── onboarding-secrets.yaml 
│   ├── onboarding-tls-secret.yaml 
│   └── ingress.yaml            
├── Dockerfile             
├── docker-compose.yml     
└── requirements.txt       

```

---

## 🔄 CI/CD & Automation

This project features a complete automated pipeline:

1. **Build:** On every push to `main`, GitHub Actions builds the Docker image.
2. **Registry:** The image is pushed to **Docker Hub** as `dhiraj918106/async-app:latest`.
3. **Deploy:** The pipeline connects to the cluster using a `KUBECONFIG` secret and triggers a rolling update (`rollout restart`) to pull the fresh image.

---

## 🏃 How to Run (Kubernetes)

### 1. Initial Setup

```bash
minikube start
minikube addons enable ingress
# Ensure local hosts file is mapped to 'minikube ip'

```

### 2. Security & Credentials

Generate self-signed SSL certificates and create the K8s secrets (refer to `k8s/onboarding-secrets.yaml` for environment variable mapping).

### 3. Deploy

```bash
kubectl apply -f k8s/

```

*Note: The pods now use `imagePullPolicy: Always` to ensure they stay synced with the Docker Hub registry.*

---

## 📝 Key Features

* **Automated CI/CD:** Zero-downtime deployments triggered by GitHub commits.
* **Cloud-Ready Images:** Centralized image management via Docker Hub.
* **HTTPS/TLS Encryption:** Secure communication via self-signed certificates.
* **Self-Healing (Probes):** Kubernetes automatically restarts pods if connection to RabbitMQ/Redis is lost.
* **Exponential Backoff:** Intelligent task retries ( seconds) for high reliability.

---
