from django.db import models
from apps.accounts.models import User
from apps.core.models import BaseModel


class Friendship(BaseModel):
    request_from = models.ForeignKey(
        to=User, on_delete=models.PROTECT, related_name='friend_request_from')
    request_to = models.ForeignKey(
        to=User, on_delete=models.PROTECT, related_name='friend_request_to')
    is_accepted = models.BooleanField(default=False)
    

    class Meta:
        verbose_name = 'Friendship'
        unique_together = ('request_from', 'request_to',)
