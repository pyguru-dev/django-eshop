from django.urls import reverse
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField()
    thumbnail = models.ImageField(upload_to='posts/')
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})
