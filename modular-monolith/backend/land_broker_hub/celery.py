import os

from celery import Celery
from celery.schedules import crontab

app = Celery(os.environ["PROJECT"])
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()

app.conf.beat_schedule = {
    "monitor-parcel-offers": {
        "task": "land_broker_hub.parcel.tasks.monitor_parcel_offers",
        'schedule': crontab(minute=0, hour='*/1')
        #"schedule": crontab(minute="*")
    }
}