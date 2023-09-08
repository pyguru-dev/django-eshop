import os
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User, UserProfile


@receiver(post_save, sender=User)
def create_user_signal(sender, instance, created, *args, **kwargs):
    if created:
        # os.mkdir(f"statics/users/{instance.username}")
        UserProfile.objects.create(user=instance)
        # UserMeta.objects.create(user=instance)
