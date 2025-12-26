import os
import time
import random
import logging
from celery import Celery
from celery.exceptions import MaxRetriesExceededError

# Setup logging for better visibility in Docker logs
logger = logging.getLogger(__name__)

RABBITMQ_URL = os.getenv("CELERY_BROKER_URL", "pyamqp://guest@rabbitmq//")
REDIS_URL = os.getenv("CELERY_RESULT_BACKEND", "redis://redis:6379/0")

celery_app = Celery(
    "onboarding_worker",
    broker=RABBITMQ_URL,
    backend=REDIS_URL
)

@celery_app.task(
    name="process_onboarding_workflow",
    bind=True,                
    max_retries=3,            
    track_started=True,       # Reports 'STARTED' state to Redis
    acks_late=True            # Task is only acknowledged after it finishes
)
def process_onboarding_workflow(self, user_email: str, username: str):
    try:
        logger.warning(f"ONBOARDING ATTEMPT {self.request.retries + 1}: {username}")

        # Simulate a failure (forced for testing)
        if random.random() < 0.1:
            raise Exception("External API Connection Timeout")

        # Step 1: PDF Generation
        time.sleep(5)
        print(f"STEP 1 COMPLETE: PDF generated for {user_email}")

        return f"Finalised onboarding for {username}"

    except Exception as exc:
        # Check if we have exhausted all retries
        if self.request.retries >= self.max_retries:
            logger.error(f"FATAL ERROR: Max retries reached for {username}. Manual intervention required.")
            # We return a custom message instead of raising, so it shows as a 
            # successful "Failure Log" in your results rather than a crash.
            return {"error": "Max retries exceeded", "user": user_email}

        logger.warning(f"RETRYING: {username} in {2 ** self.request.retries}s...")
        
        # raise self.retry is the ONLY correct way to trigger a retry
        raise self.retry(exc=exc, countdown=2 ** self.request.retries)