from django.db import models
from django.utils.translation import gettext_lazy as _ 
from apps.core.models import BaseModel


class NotificationMessage(BaseModel):
    class NotificationSentStatus(models.TextChoices):
        sent = 's', _('Sent')
        
    message = models.TextField()


class BroadcastNotification(BaseModel):
    title = models.CharField(max_length=250)
    message = models.TextField()
    broadcast_on = models.DateTimeField()
    status = models.CharField(max_length=8)


class PrivateNotification(BaseModel):
    message = models.TextField()
