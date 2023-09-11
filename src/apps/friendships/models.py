from django.utils.translation import gettext_lazy as _
from django.db import models
from apps.accounts.models import User
from apps.core.models import BaseModel


class FriendshipRequest(BaseModel):
    class FriendshipRequestChoices(models.TextChoices):
        SENT = 's', _('Sent')
        ACCEPTED = 'a', _('Accepted')
        REJECTED = 'r', _('Rejected')
        
    class Meta:
        db_table = 'friendship_requests'    


class Friendship(BaseModel):
    request_from = models.ForeignKey(
        to=User, on_delete=models.PROTECT, related_name='friend_request_from')
    request_to = models.ForeignKey(
        to=User, on_delete=models.PROTECT, related_name='friend_request_to')
    is_accepted = models.BooleanField(default=False)
    accepted_at = models.DateTimeField(_('accepted at'), null=True, blank=True)

    class Meta:
        db_table = 'friendships'
        verbose_name = 'Friendship'
        unique_together = ('request_from', 'request_to',)

    