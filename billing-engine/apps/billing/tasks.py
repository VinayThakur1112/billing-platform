from celery import shared_task
from django.db import transaction
from django.db.models import Q
from apps.billing.models import BillingEvent, Invoice, InvoiceLineItem
import logging
logger = logging.getLogger(__name__)


@shared_task(
    bind=True, 
    autoretry_for=(Exception,), 
    retry_backoff=10, 
    retry_kwargs={"max_retries": 5},
    retry_jitter=True,
    acks_late=True,
)
def process_billing_event(self, billing_event_id: int):
    """
    Consumes a BillingEvent and creates an InvoiceLineItem.
    """
    logger.info("Processing billing event %s", billing_event_id)

    with transaction.atomic():
        # Lock the event row to prevent double processing
        event = (
            BillingEvent.objects
            .select_for_update() # Lock the row
            .get(id=billing_event_id, processed=False) # gets one row
        )

        logger.info(event)

        # Get or create draft invoice for account
        invoice, _ = (
            Invoice.objects
            .select_for_update()
            .get_or_create(account = event.account, 
                           status = 'draft',)
        )

        logger.info(invoice)

        # Create Line item (DB constraint ensures idempotency)
        InvoiceLineItem.object.create(
            invoice=invoice,
            billing_event=event,
            description=f"{event.event_type} charge",
            amount=event.amount,
        )

        # Mark event as processed
        event.processed = True
        event.save(update_fields=['processed']) 

    logger.info("BillingEvent %s processed successfully", billing_event_id)
    return "processed"