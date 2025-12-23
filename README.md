
# Async-Onboarding-Service

A high-performance, asynchronous user onboarding microservice built with **FastAPI**, **RabbitMQ**, and **Celery**.

This project demonstrates how to offload heavy, time-consuming tasks (like PDF generation and email dispatching) to background workers, ensuring the API remains responsive for the end user.

## 🚀 The Architecture

* **FastAPI:** The entry point. It receives requests and hands them off immediately.
* **RabbitMQ:** The message broker. It safely stores tasks in a queue.
* **Celery:** The background worker. It picks up tasks from the queue and processes them.
* **Docker Compose:** Orchestrates all services into a single command.

## 🛠️ Tech Stack

* **Language:** Python
* **Framework:** FastAPI
* **Task Queue:** Celery
* **Broker:** RabbitMQ
* **Infrastructure:** Docker & Docker Compose

---

## 📂 Project Structure

```text
async-onboarding-service/
├── app/
│   ├── main.py        # API Endpoints
│   └── tasks.py       # Celery Worker Tasks
├── Dockerfile         # Shared environment for API and Worker
├── docker-compose.yml # Service orchestration
└── requirements.txt   # Project dependencies

```

---

## 🏃 How to Run

### 1. Clone the repository

```bash
git clone https://github.com/your-username/async-onboarding-service.git
cd async-onboarding-service

```

### 2. Start the services

Ensure you have Docker installed, then run:

```bash
docker-compose up --build

```

### 3. Test the API

* **Interactive Docs:** [http://localhost:8000/docs](https://www.google.com/search?q=http://localhost:8000/docs)
* **Endpoint:** `POST /onboard`
* **Payload:**
```json
{
  "username": "johndoe",
  "email": "john@example.com"
}

```



### 4. Monitor the Broker

You can view the RabbitMQ management dashboard at [http://localhost:15672](https://www.google.com/search?q=http://localhost:15672) (User: `guest` | Pass: `guest`).

---

## 📝 Key Features

* **Non-blocking API:** Responds in milliseconds while heavy work happens in the background.
* **Scalability:** You can scale the `worker` service independently in `docker-compose` to handle higher loads.
* **Reliability:** If the worker crashes, the task stays safe in RabbitMQ until it's processed.

---
