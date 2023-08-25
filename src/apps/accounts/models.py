from django.db import models
from django.contrib.auth.models import AbstractUser


class DJUser(AbstractUser):
    mobile = models.CharField(null=False, blank=False, unique=True, max_length=11)
