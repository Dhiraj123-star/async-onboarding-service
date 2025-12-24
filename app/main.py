from fastapi import FastAPI
from pydantic import BaseModel
from .tasks import process_onboarding_workflow

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
        "task_id":task.id
    }