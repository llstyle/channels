from celery import Celery
from config import settings
from asgiref.sync import async_to_sync
from send_email import send_email_async
from pydantic import EmailStr
from typing import List

celery = Celery("worker")
celery.conf.broker_url = settings.CELERY_BROKER_URL


@celery.task(name="celery_email")
def celery_email(subject: str, email: List[EmailStr], body: dict, template: str):
    async_to_sync(send_email_async)(subject, email, body, template)