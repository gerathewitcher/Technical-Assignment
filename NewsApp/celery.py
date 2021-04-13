import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'NewsApp.settings')

app = Celery('NewsApp')

app.config_from_object('django.conf:settings', namespace='CELERY')


app.autodiscover_tasks()

app.conf.beat_schedule = {
    'creating-news': {
        'task': 'main.tasks.create_news',
        'schedule': 300.0
    }
}
