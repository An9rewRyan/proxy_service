from celery import Celery
app = Celery('core', broker='pyamqp://guest@rabbitmq//', backend='redis://redis:6379/0', include=['tasks'])
app.conf.beat_schedule = {
    'add-every-30-seconds': {
        'task': 'tasks.update',
        'schedule': 30.0,
    },
}
