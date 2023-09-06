from django.db import models
from django.db.models import Q
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class SoftDeleteQuerySet(models.QuerySet):
    def delete(self):
        return self.update(is_deleted=True, deleted_at=timezone.now())


class SoftDeleteManager(models.Manager):
    def get_queryset(self):
        return SoftDeleteQuerySet(self.model, self._db).filter(Q(is_deleted=False) | Q(is_deleted__isnull=True))


class BaseModel(models.Model):
    class Meta:
        abstract = True

    objects = SoftDeleteManager()
    
    uuid = models.UUIDField(unique=True)
    is_deleted = models.BooleanField(null=True, blank=True, editable=False)
    deleted_at = models.DateTimeField(null=True, blank=True, editable=False)    
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name=_('تاریخ بروزرسانی'))
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name=_('تاریخ ثبت'))

    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()
    
    def restore(self):
        self.is_deleted = False
        self.deleted_at = None
        self.save()
        


class IPAddress(BaseModel):
    ip_address = models.GenericIPAddressField()
    hit_count = models.PositiveBigIntegerField(default=0)
    
    class Meta:
        db_table = 'ip_addresses'
        verbose_name = _("آدرس IP")
        verbose_name_plural = _("آدرس IP ها")

    def __str__(self) -> str:
        return self.ip_address + ' : ' + self.hit_count



class Tag(BaseModel):
    name = models.CharField(max_length=255, unique=True,
                            blank=False, null=False, verbose_name=_('عنوان'))
    slug = models.SlugField(max_length=255, unique=True,
                            verbose_name=_('اسلاگ'))    

    class Meta:
        db_table = 'tags'
        verbose_name = _("برچسب")
        verbose_name_plural = _("برچسب ها")

    def __str__(self) -> str:
        return self.name

