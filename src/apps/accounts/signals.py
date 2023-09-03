import os
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User

@receiver(post_save, sender=User)
def create_user_signal(sender, instance, created, **kwargs):
    if created:
        os.mkdir(f"statics/users/{instance.username}")        
    
    