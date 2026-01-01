
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
* **Self-Healing K8s:** Integrated **Liveness and Readiness Probes** to monitor and recover unhealthy services automatically.

---

## 🛠️ Tech Stack

* **Backend:** FastAPI (Python 3.11)
* **Task Management:** Celery 5.x
* **Brokers/State:** RabbitMQ, Redis
* **Containerization:** Docker, Kubernetes (k8s)
* **Security:** OpenSSL (Self-signed TLS), K8s Secrets
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
│   ├── app-deployment.yaml     # API & Worker with Health Probes
│   ├── flower-deployment.yaml
│   ├── onboarding-secrets.yaml # Encrypted Connection Strings
│   ├── onboarding-tls-secret.yaml # TLS Certificates
│   └── ingress.yaml            # NGINX Routing with HTTPS Config
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

### 2. Security Setup (SSL/TLS)

Generate a self-signed certificate and create the Kubernetes secret:

```bash
openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
  -keyout onboarding.key -out onboarding.crt \
  -subj "/CN=api.onboarding.local"

kubectl create secret tls onboarding-tls-secret --key onboarding.key --cert onboarding.crt

```

### 3. Deploy Infrastructure

```bash
kubectl apply -f k8s/

```

### 4. Setup Local DNS

Map the Minikube IP to your custom domains in your system's `hosts` file:

```text
# Replace <MINIKUBE_IP> with output of 'minikube ip'
<MINIKUBE_IP> api.onboarding.local flower.onboarding.local

```

### 5. Access the Dashboard (HTTPS)

* **Secure API Docs:** [https://api.onboarding.local/docs](https://www.google.com/search?q=https://api.onboarding.local/docs)
* **Secure Flower Monitor:** [https://flower.onboarding.local](https://www.google.com/search?q=https://flower.onboarding.local)

---

## 📝 Key Features

* **HTTPS/TLS Encryption:** Secure communication via self-signed certificates managed by NGINX Ingress.
* **Self-Healing (Probes):** Kubernetes automatically detects process hangs or connection losses and restarts pods to maintain 99.9% availability.
* **Exponential Backoff Retries:** Intelligent task retries ( seconds) to handle transient downstream failures.
* **Secure Config:** Decoupled sensitive credentials using **Kubernetes Secrets**.
* **Fault Tolerance:** Configured `acks_late=True` to prevent task loss during unexpected worker evictions.

---
