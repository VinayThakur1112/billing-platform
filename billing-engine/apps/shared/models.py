from django.db import models
import uuid

class IdempotencyKey(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False
    )

    key = models.CharField(max_length=255, unique=True)
    endpoint = models.CharField(max_length=255)

    request_hash = models.CharField(max_length=64)

    response_status = models.IntegerField()
    response_body = models.JSONField()

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "idempotency_keys"
