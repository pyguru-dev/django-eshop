import os

from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djshop.envs.common')

app = Celery('djshop')

app.config_from_object('django.conf:settings', namespace='CELERY')


# Load task modules from all registered Django apps.
app.autodiscover_tasks()

app.conf.beat_schedule = {}

@app.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f'Request: {self.request!r}')