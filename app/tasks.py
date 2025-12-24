import os
import time
from celery import Celery

# Configuration: RabbitMQ Broker URL
RABBITMQ_URL = os.getenv("CELERY_BROKER_URL","pyamqp://guest@rabbitmq//")

celery_app = Celery("onboarding_worker",broker=RABBITMQ_URL)

@celery_app.task(name="process_onboarding_workflow")
def process_onboarding_workflow(user_email:str,username:str):
    """
    Simulate a sequence of heavy background tasks
    
    """
    print(f"ONBOARDING STARTED: Building profile for {username}....")

    # Simulate step 1: Generating a customized welcome PDF
    time.sleep(4)
    print(f"STEP 1 COMPLETE: PDF Welcome Kit generated for {user_email}")

    # Simulate step 2: Syncing data with 3rd party CRM/Email service
    time.sleep(3)
    print(f"STEP 2 COMPLETE: Welcome email dispatched to {user_email}")

    return f"Finalised onboarding for {username}"