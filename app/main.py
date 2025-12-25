from fastapi import FastAPI
from pydantic import BaseModel
from celery.result import AsyncResult
from .tasks import process_onboarding_workflow,celery_app

app = FastAPI(
    title= "Async Onboarding Service",
    version="1.0.0"
)
class UserSignup(BaseModel):
    username: str
    email: str

@app.get("/health")
def health_check():
    return {"status":"OK"}

@app.post("/onboard",status_code=202)
def onboard_user(user:UserSignup):
    """
    Triggers the asynchronous onboarding workflow.
    Returns a 202 Accepted status and the task ID.
    """
    # Dispatch task to RabbitMQ via Celery
    task = process_onboarding_workflow.delay(user.email,user.username)

    return {
        "message":"Onboarding workflow initialized successfully.",
        "task_id":task.id,
        "status":"Processing"
    }
# Status Check Endpoint
@app.get("/status/{task_id}")
def get_task_status(task_id: str):
    task_result = AsyncResult(task_id, app=celery_app)
    return {
        "task_id":task_id,
        "status":task_result.status, # PENDING, STARTED, SUCCESS, FAILURE
        "task_result":task_result.result if task_result.ready() else None
    }