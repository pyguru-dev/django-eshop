from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from .exceptions import DuplicateImageException
from .models import Image


@receiver(pre_save, sender=Image)
def check_duplicate_hash(sender, instance, created, *args, **kwargs):
    existed = Image.objects.filter(file_hash=instance.file_hash).exists()
    if existed:
        raise DuplicateImageException("Duplicated")
