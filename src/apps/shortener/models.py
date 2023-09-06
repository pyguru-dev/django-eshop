from django.db import models

from apps.core.models import BaseModel


class Url(BaseModel):
    url = models.URLField(blank=False,null=False)
    slug = models.CharField(blank=False,null=False, max_length=255)
    visit_count = models.PositiveBigIntegerField(default=0)    

    class Meta:
        ordering = ('-created_at',)
        
    def __str__(self) -> str:
        return self.url