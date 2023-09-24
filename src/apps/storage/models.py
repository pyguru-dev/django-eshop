import hashlib
from django.db import models

from apps.core.models import BaseModel


class Media(BaseModel):
    file_hash = models.CharField(max_length=40, db_index=True, editable=False)
    file_size = models.PositiveIntegerField(
        null=True, blank=True, editable=False)
    mime_type = models.CharField(
        max_length=250, null=True, blank=True, editable=False)

    def save(self, *args, **kwargs):
        self.file_size = self.image.size
        hasher = hashlib.sha1()
        for chunk in self.image.file.chunks():
            hasher.update(chunk)
        self.file_hash = hasher.hexdigest()
        super().save(*args, **kwargs)


class Image(Media):
    image = models.ImageField(
        width_field='width', height_field='height', upload_to='images/')
    image_alt = models.CharField(max_length=255, null=True, blank=True)
    width = models.PositiveIntegerField(editable=False)
    height = models.PositiveIntegerField(editable=False)
