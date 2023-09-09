from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.core.models import BaseModel

class Vendor(BaseModel):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    logo = models.ImageField(upload_to='')
    short_description = models.CharField(max_length=255)
    description = models.TextField()
    
    class Meta:
        db_table = 'vendors'
        verbose_name = _('فروشنده')
        verbose_plural_name = _('فروشنده ها')
        
    def __str__(self) -> str:
        return self.title
    
    # user
    