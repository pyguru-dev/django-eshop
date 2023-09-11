import uuid
from django.db import models
from django.db.models import Q
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from apps.core.managers import SoftDeleteManager

class BaseModel(models.Model):
    class Meta:
        abstract = True

    objects = SoftDeleteManager()
    
    uuid = models.UUIDField(unique=True, default=str(uuid.uuid4()), editable=False)
    is_deleted = models.BooleanField(null=True, blank=True, editable=False)
    deleted_at = models.DateTimeField(null=True, blank=True, editable=False, verbose_name=_('تاریخ حذف'))    
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name=_('تاریخ بروزرسانی'))
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name=_('تاریخ ثبت'))

    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()

    def hard_delete(self):
        pass
    
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
    name = models.CharField(max_length=255, unique=True, verbose_name=_('عنوان'))
    slug = models.SlugField(max_length=255, unique=True, verbose_name=_('اسلاگ'), blank=True)    

    class Meta:
        db_table = 'tags'
        verbose_name = _("برچسب")
        verbose_name_plural = _("برچسب ها")

    def __str__(self) -> str:
        return self.name

# class Notification(BaseModel):
#     user = models.ForeignKey(User, on_delete=models.CASCADE,
#                              null=True,blank=True, related_name='notifications')
#     message = models.TextField()
    
# class PublicNotification(BaseModel):
#     pass