from django.db import models
import uuid

# Create your models here.
class Account(models.Model):
    id = models.UUIDField(
        primary_key=True, 
        default=uuid.uuid4, 
        editable=False
    )
    external_id = models.CharField(
        max_length=100, 
        unique=True
    )  # e.g. Siebel ID
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    

class Subscription(models.Model):
    account = models.ForeignKey(
        Account, on_delete=models.CASCADE
    )
    service_name = models.CharField(max_length=100)  # voice, data, nrc, etc
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)


class BillingEvent(models.Model):
    EVENT_TYPES = (
        ("USAGE", "Usage"),
        ("NRC", "Non Recurring Charge"),
        ("MRC", "Monthly Recurring Charge"),
    )

    id = models.UUIDField(
        primary_key=True, 
        default=uuid.uuid4, 
        editable=False
    )
    account = models.ForeignKey(
        Account, 
        on_delete=models.CASCADE
    )
    subscription = models.ForeignKey(
        Subscription, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True
    )

    event_type = models.CharField(
        max_length=10, 
        choices=EVENT_TYPES
    )
    reference_id = models.CharField(
        max_length=100
    )  # CDR ID / Document ID / etc
    amount = models.DecimalField(
        max_digits=12, 
        decimal_places=2
    )

    processed = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("event_type", "reference_id")


class Invoice(models.Model):
    account = models.ForeignKey(
        Account, on_delete=models.CASCADE
    )
    invoice_number = models.CharField(
        max_length=50, unique=True
    )
    billing_period_start = models.DateField()
    billing_period_end = models.DateField()

    total_amount = models.DecimalField(
        max_digits=12, 
        decimal_places=2, 
        default=0
    )

    created_at = models.DateTimeField(auto_now_add=True)


class InvoiceLineItem(models.Model):
    invoice = models.ForeignKey(
        Invoice, 
        related_name="line_items", 
        on_delete=models.CASCADE
    )
    description = models.CharField(max_length=255)
    amount = models.DecimalField(
        max_digits=12, 
        decimal_places=2
    )
    billing_event = models.ForeignKey(
        BillingEvent, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True
    )