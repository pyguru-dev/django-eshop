import json
from django.db.models.signals import post_save
from django_celery_beat.models import PeriodicTask, CrontabSchedule
from .models import BroadcastNotification


@receiver(post_save, sender=BroadcastNotification)
def broadcast_notification_handler(sender, instance, created, *args, **kwargs):
    if created:
        schedule, created = CrontabSchedule.objects.get_or_create(hour=instance.broadcast_on.hour,
                                                                  minute=instance.broadcast_on.minute, day_of_month=instance.broadcast_on.day,
                                                                  month_on_year=instance.broadcast_on.month,)
        task = PeriodicTask.objects.create(
            crontab=schedule, name=f'broadcast-notification-{instance.id}', task='notification_app.tasks.broadcast_notification', args=json.dumps((instance.id)))
