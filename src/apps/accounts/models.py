from django.db import models
from django.contrib.auth.models import AbstractUser

class Country(models.Model):
    name = models.CharField(max_length=50)
    
    

class CustomUser(AbstractUser):
    mobile = models.CharField(null=True, blank=True,
                              unique=True, max_length=11)
    # mobile_verified = models.BooleanField(default=False)


class UserProfile(models.Model):
    class GenderChoices(models.TextChoices):
        male = 'male'
        female = 'female'
        unknown = 'unknown'
    user = models.OneToOneField(
        CustomUser, on_delete=models.CASCADE, related_name='profile')
    
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    gender = models.CharField(max_length=8, choices=GenderChoices.choices, default=GenderChoices.unknown)
    


# class CustomUserManager(BaseUserManager):
#     def create_user(self, email, password=None):
#         pass
