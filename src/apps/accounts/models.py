from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

class Country(models.Model):
    name = models.CharField(max_length=50)
    slug = models.CharField(max_length=50)
    flag = models.CharField(max_length=50)
    
class Province(models.Model):
    name = models.CharField(max_length=50)
    slug = models.CharField(max_length=50)
    flag = models.CharField(max_length=50)
    
class City(models.Model):
    name = models.CharField(max_length=50)
    slug = models.CharField(max_length=50)
    flag = models.CharField(max_length=50)
    

class ActivationCode(models.Model):
    code = models.CharField(max_length=50)
    expired_at = models.CharField(max_length=50)
    
class User(AbstractUser):
    # mobile = models.CharField(null=True, blank=True,
    #                           unique=True, max_length=11)
    # mobile_verified = models.BooleanField(default=False)
    pass
    


class UserProfile(models.Model):
    # province, city, birthday, instagram,telegram
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


class Address(models.Model):
    pass
    # user, province, city, title, address, 
    # map , zip_code, receiver_self, receiver_name, 
    # receiver_mobile, last_used_at, default
    
class UserBank(models.Model):
    pass
    # user_id , bank_id, title, shaba, account_number 
    
class Wallet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='wallet')
    amount = models.PositiveBigIntegerField(verbose_name=_('موجودی'), default=0)


class AccountDeleteRequest(models.Model):
    pass
    # user_id , approved_at, complete_at 
    
    
# user metas: last_logout_at, last_login_at, last_login_ip, last_login_agent,
# email_verified_at , mobile_verified_at,password_changed_at, is_banned, banned_at, unbanned_at