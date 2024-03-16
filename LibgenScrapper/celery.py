from __future__ import absolute_import, unicode_literals


import os
from celery import Celery, shared_task
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibgenScrapper.settings')

app = Celery('LibgenScrapper', broker=settings.CELERY_BROKER_URL, backend=settings.CELERY_RESULT_BACKEND)

app.conf.broker_connection_retry_on_startup = True

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()


@shared_task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
