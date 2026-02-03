import uuid
from django.db import models
from django.db.models import Q, CheckConstraint


# Create your models here.
class Plan(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    
    code = models.CharField(
        max_length=50, unique=True)
    
    name = models.CharField(
        max_length=100)
    
    price = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.00)
    
    billing_cycle = models.CharField(
        max_length=20,
        choices=[
            ("MONTHLY", "Monthly"),
            ("QUARTERLY", "Quarterly"),
            ("YEARLY", "Yearly"),
        ]
    )

    currency = models.CharField(
        max_length=3,
        default="USD"
    )

    active = models.BooleanField(default=True)

    # Audit fields
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )
    created_by = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )

    class Meta:
        db_table = "plans"
        indexes = [
            models.Index(fields=["code"]),
            models.Index(fields=["active"]),
        ]
        constraints = [
            CheckConstraint(
                condition=Q(price__gt=0),
                name="price_must_be_positive"
            ),
        ]
    
    def __str__(self):
        return f"{self.code} - {self.name}"