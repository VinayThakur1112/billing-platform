from celery import shared_task
import logging
logger = logging.getLogger(__name__)


@shared_task(bind=True, 
    autoretry_for=(Exception,), 
    retry_backoff=10, 
    retry_kwargs={"max_retries": 5},
    retry_jitter=True,
    acks_late=True,
)
def process_billing_event(self, billing_event_id: int):
    """
    Safe billing task:
    - retries on failure
    - won't lose task if worker crashes
    """
    logger.info("Processing billing event %s", billing_event_id)