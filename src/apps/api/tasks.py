from celery import shared_task


@shared_task(name='Send Welcome Email')
def send_welcome_email_task():
    pass