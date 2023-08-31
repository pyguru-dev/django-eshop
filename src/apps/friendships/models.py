from django.db import models
from django.contrib.auth import get_user_model


class Friendship(models.Model):
    request_from = models.ForeignKey(
        to=get_user_model(), on_delete=models.PROTECT, related_name='friend_request_from')
    request_to = models.ForeignKey(
        to=get_user_model(), on_delete=models.PROTECT, related_name='friend_request_to')
    is_accepted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbos_name = 'Friendship'
        unique_togethe = ('request_from', 'request_to',)
