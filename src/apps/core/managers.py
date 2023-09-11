from django.db.models.query import QuerySet
from django.db import models
from django.db.models import Q
from django.utils import timezone


class PublishedManager(models.Manager):
    def get_queryset(self) -> QuerySet:
        return super(PublishedManager, self).get_queryset().filter(published_status='p')

class SoftDeleteQuerySet(models.QuerySet):
    def delete(self):
        return self.update(is_deleted=True, deleted_at=timezone.now())

class SoftDeleteManager(models.Manager):
    def get_queryset(self):
        return SoftDeleteQuerySet(self.model, using=self._db).filter(Q(is_deleted=False) | Q(is_deleted__isnull=True))
