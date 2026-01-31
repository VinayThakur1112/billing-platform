import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "accounts.config.settings")

app = Celery("accounts")

# Read settings from Django
app.config_from_object("django.conf:settings", namespace="CELERY")

# Auto-discover tasks in all apps
app.autodiscover_tasks()