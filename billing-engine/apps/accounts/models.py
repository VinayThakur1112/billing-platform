import uuid
from django.db import models


class Account(models.Model):
    id = models.UUIDField(
        primary_key=True, 
        default=uuid.uuid4, 
        editable=False
    )
    name = models.CharField(
        max_length=255
    )
    email = models.EmailField(
        unique=True
    )
    phone_number = models.CharField(
        max_length=20, 
        blank=True, 
        null=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        db_table = "accounts"


class Subscription(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4, 
        editable=False
    )
    account = models.ForeignKey(
        Account, 
        on_delete=models.CASCADE, 
        related_name="subscriptions"
    )
    plan_name = models.CharField(
        max_length=100
    )
    start_date = models.DateField()
    end_date = models.DateField(
        blank=True, 
        null=True
    )
    active = models.BooleanField(
        default=True
    )
    class Meta:
        db_table = "subscriptions"


class AccountBalance(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4, 
        editable=False
    )
    account = models.OneToOneField( # each row corresponds to one account
        Account, 
        on_delete=models.CASCADE, 
        related_name="balance"
    )
    balance_amount = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        default=0.00
    )
    last_updated = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        db_table = "account_balance"
