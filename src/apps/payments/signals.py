from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from .models import Payment

# @receiver(pre_save, sender=Payment)
