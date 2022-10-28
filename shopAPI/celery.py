import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shopAPI.settings')

app = Celery('shopAPI')
app.config_from_object('django.conf:settings',
                        namespace='CELERY')
app.autodiscover_tasks()


# celery spam task
app.conf.beat_schedule = {
    'send-spam-every-5-minutes':{
        'task': 'shopAPI.tasks.send_spam_email',
        'schedule': crontab(minute='*/1')
    }
}