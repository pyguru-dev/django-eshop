from django.urls import reverse
from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils.translation import gettext as _


class Post(models.Model):
    PUBLISHED_STATUS = (
        ('p', 'Published'),
        ('d', 'Draft'),
    )

    author = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(_('عنوان'), max_length=150)
    # slug = models.SlugField(unique=True)
    body = models.TextField()
    thumbnail = models.ImageField(upload_to='posts/')
    published_status = models.CharField(
        max_length=1, choices=PUBLISHED_STATUS, default='d')
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})


class Comment(models.Model):
    comment = models.TextField()
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    article = models.ForeignKey(
        Post, related_name='comments', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.comment

    def get_absolute_url(self):
        return reverse("post_list")


class Category(models.Model):
    name = models.TextField(max_length=100, unique=True,
                            blank=False, null=False)
