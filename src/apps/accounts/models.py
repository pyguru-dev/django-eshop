from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.contrib.auth import get_user_model

# User = get_user_model()

class Country(models.Model):
    name = models.CharField(max_length=50)
    
    

# class CustomUser(AbstractUser):
#     mobile = models.CharField(null=True, blank=True,
#                               unique=True, max_length=11)
    # mobile_verified = models.BooleanField(default=False)
    


class UserProfile(models.Model):
    class GenderChoices(models.TextChoices):
        male = 'male'
        female = 'female'
        unknown = 'unknown'
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='profile')
    
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True, default='default_avatar.jpg')
    gender = models.CharField(max_length=8, choices=GenderChoices.choices, default=GenderChoices.unknown)
    bio = models.CharField(max_length=255, null=True,blank=True)
    
    def __str__(self) -> str:
        return self.user.username


# class CustomUserManager(BaseUserManager):
#     def create_user(self, email, password=None):
#         pass
