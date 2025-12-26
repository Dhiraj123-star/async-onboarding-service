
# Async-Onboarding-Service

A high-performance, asynchronous user onboarding microservice built with **FastAPI**, **RabbitMQ**, **Celery**, and **Redis**.

This project demonstrates how to offload heavy, time-consuming tasks (like PDF generation and email dispatching) to background workers, ensuring the API remains responsive while allowing the client to track the task's progress.

## 🚀 The Architecture

* **FastAPI:** The "Front Desk." Receives signups and provides status updates.
* **RabbitMQ:** The "Message Broker." Safely queues onboarding tasks.
* **Celery:** The "Worker." Handles the heavy lifting (PDF/Email simulation).
* **Redis:** The "Result Backend." Stores the final outcome and status of each task.
* **Docker Compose:** Orchestrates all services into a single, isolated network.

## 🛠️ Tech Stack

* **Language:** Python
* **Framework:** FastAPI
* **Task Queue:** Celery
* **Broker:** RabbitMQ
* **Result Store:** Redis
* **Infrastructure:** Docker & Docker Compose

---

## 📂 Project Structure

```text
async-onboarding-service/
├── app/
│   ├── main.py        # API Endpoints & Task Status Logic
│   └── tasks.py       # Celery Worker Tasks & Backend Config
├── .gitignore         # Optimized for Python/Docker
├── Dockerfile         # Unified environment for API/Worker
├── docker-compose.yml # 4-Service Orchestration
└── requirements.txt   # Project dependencies (FastAPI, Celery, Redis)

```

---

## 🏃 How to Run

### 1. Clone the repository

```bash
git clone https://github.com/your-username/async-onboarding-service.git
cd async-onboarding-service

```

### 2. Start the services

```bash
docker-compose up --build

```

### 3. Test the Workflow

1. **Trigger Onboarding:** Go to [http://localhost:8000/docs](https://www.google.com/search?q=http://localhost:8000/docs) and `POST` to `/onboard`.
2. **Copy Task ID:** The API will return a unique `task_id`.
3. **Check Progress:** `GET` from `/status/{task_id}` to see if the worker is `PENDING` or `SUCCESS`.

### 4. Monitor Infrastructure

* **RabbitMQ Dashboard:** [http://localhost:15672](https://www.google.com/search?q=http://localhost:15672) (guest/guest)
* **Redis:** Accessible internally on port `6379`.

---

## 📝 Key Features

* **Asynchronous Processing:** API responses are returned in milliseconds.
* **State Persistence:** Task results are stored in Redis, allowing for status polling.
* **Fault Tolerance:** Tasks persist in RabbitMQ even if the worker service is temporarily down.
* **Scalability:** Easily scale workers using `docker-compose up --scale worker=3`.

---