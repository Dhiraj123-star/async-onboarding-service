import os
import time
from celery import Celery

# Configuration: RabbitMQ Broker URL
RABBITMQ_URL = os.getenv("CELERY_BROKER_URL","pyamqp://guest@rabbitmq//")
# Configuration: Redis Result Backend URL
REDIS_URL = os.getenv(
    "CELERY_RESULT_BACKEND",
    "redis://redis:6379/0",
    )

celery_app = Celery(
    "onboarding_worker",
    broker=RABBITMQ_URL,
    backend=REDIS_URL # Added backend
    )

@celery_app.task(name="process_onboarding_workflow")
def process_onboarding_workflow(user_email:str,username:str):
    """
    Simulate a sequence of heavy background tasks
    
    """
    print(f"ONBOARDING STARTED: Building profile for {username}....")

    # Simulate step 1: Generating a customized welcome PDF
    time.sleep(10)
    print(f"STEP 1 COMPLETE: PDF Welcome Kit generated for {user_email}")

    # Simulate step 2: Syncing data with 3rd party CRM/Email service
    time.sleep(5)
    print(f"STEP 2 COMPLETE: Welcome email dispatched to {user_email}")

    return f"Finalised onboarding for {username}"