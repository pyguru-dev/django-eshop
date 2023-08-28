from django.db import models
from ckeditor.fields import RichTextField
from apps.accounts.models import CustomUser


class Product(models.Model):
    PUBLISHED_STATUS = (
        ('p', 'Published'),
        ('d', 'Draft'),
    )
    author = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name='products')
    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(unique=True)
    body = RichTextField()
    thumbnail = models.ImageField(upload_to="posts/%Y/%m/%d")
    published_status = models.CharField(
        max_length=1, choices=PUBLISHED_STATUS, default='d')
    # category = models.ForeignKey("Category", related_name='post', verbose_name='categories', on_delete=models.CASCADE)
    # tags = models.ManyToManyField("Tag", verbose_name='tags', related_name='posts')
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.title

class File(models.Model):
    pass