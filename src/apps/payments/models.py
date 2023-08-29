from django.db import models
from apps.accounts.models import CustomUser


class Gateway(models.Model):
    title = models.CharField(max_length=50)


class Payment(models.Model):
    payment_status = ()

    user = models.ForeignKey(
        CustomUser, related_name='payments', on_delete=models.CASCADE)
    gateway = models.ForeignKey(Gateway, on_delete=models.CASCADE)
    price = models.PositiveBigIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
