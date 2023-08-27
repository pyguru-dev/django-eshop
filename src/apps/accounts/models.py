from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    mobile = models.CharField(null=True, blank=True,
                              unique=True, max_length=11)
    # mobile_verified = models.BooleanField(default=False)


class UserProfile(models.Model):
    user = models.OneToOneField(
        CustomUser, on_delete=models.CASCADE, related_name='profile')
    
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    


# class CustomUserManager(BaseUserManager):
#     def create_user(self, email, password=None):
#         pass
