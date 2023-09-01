from django.db import models


class Url(models.Model):
    url = models.URLField(blank=False,null=False)
    slug = models.CharField(blank=False,null=False, max_length=255)
    visit_count = models.PositiveBigIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_at',)
        
    def __str__(self) -> str:
        return self.url