from celery import shared_task
from .alerts import AlertEngine


@shared_task(
    bind=True,
    autoretry_for=(Exception,),
    retry_backoff=True,
    retry_kwargs={"max_retries": 3},
)
def check_price_alerts(self):
    """
    Periodic task that checks all price alerts and triggers notifications.
    Retries automatically on failure.
    """
    AlertEngine.evaluate_all()
