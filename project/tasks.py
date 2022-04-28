from celery import shared_task
import celery
from celery.utils.log import get_task_logger
from django.core.management import base, call_command

import random
import requests

logger = get_task_logger(__name__)

# Base class for automatically retrying task
class BaseTaskWithRetry(celery.Task):
    autoretry_for = (Exception, KeyError)
    retry_kwargs = {'max_retries':5}
    retry_backoff = True

@shared_task
def sample_task():
    logger.info("The sample task just run")


@shared_task
def periodic_task():
    call_command("my_custom_comand")


@shared_task(bind=True, base=BaseTaskWithRetry)
def task_process_notification(self):
    # if not random.choice([0, 1]):
        raise Exception()
        # requests.post('https://httpbin.org/delay/5')
