from celery import Celery
from core.constants import BROKER
from celery.schedules import crontab

app = Celery("github_report", broker=BROKER)

app.conf.update(
    task_serializer='json',
    accept_content=['json'],
    result_serializer='json'
)

app.conf.beat_schedule = {
    'weekly-github-report': {
        'task': 'tasks.generate_github_report_task',
        'schedule': crontab(day_of_week='sunday', hour=23, minute=0),
    },
}