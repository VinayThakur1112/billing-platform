import uuid
from django.db import models

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

    active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "plans"
    
    def __str__(self):
        return self.code