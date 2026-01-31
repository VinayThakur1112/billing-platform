from celery import shared_task

@shared_task(bind=True, autoretry_for=(Exception,), retry_backoff=5, retry_kwargs={"max_retries": 3})
def test_billing_task(self, account_id):
    print(f"Running billing task for account {account_id}")
    return {"status": "SUCCESS", "account_id": account_id}