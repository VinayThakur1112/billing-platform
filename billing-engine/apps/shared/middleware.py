import hashlib
import json
from django.http import JsonResponse
from apps.shared.models import IdempotencyKey

class IdempotencyMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        key = request.headers.get("Idempotency-Key")
        if not key or request.method != "POST":
            return self.get_response(request)

        request_hash = hashlib.sha256(
            json.dumps(request.data, sort_keys=True).encode()
        ).hexdigest()

        record = IdempotencyKey.objects.filter(
            key=key,
            endpoint=request.path
        ).first()

        if record:
            # Same key used with different payload → reject
            if record.request_hash != request_hash:
                return JsonResponse(
                    {"error": "Idempotency key reused with different payload"},
                    status=409
                )

            return JsonResponse(
                record.response_body,
                status=record.response_status
            )

        response = self.get_response(request)

        IdempotencyKey.objects.create(
            key=key,
            endpoint=request.path,
            request_hash=request_hash,
            response_status=response.status_code,
            response_body=response.json(),
        )

        return response