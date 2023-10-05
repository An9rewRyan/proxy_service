from celery import Celery

app = Celery('core', broker='pyamqp://guest@rabbitmq//', backend='redis://redis:6379/0')
app.autodiscover_tasks()
