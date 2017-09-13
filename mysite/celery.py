import os
from celery import celery

os.environ.setdefault('DJANDO_SETTINGS_MODULE', 'mysite.settings')

app = celery ('mysite')
app.config_from_object ('django.conf:settings', namespace = 'CELERY')
app.autodiscover_tasks()