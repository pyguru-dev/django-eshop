from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Gateway(models.Model):
    title = models.CharField(max_length=50)


class Payment(models.Model):
    payment_status = ()

    user = models.ForeignKey(
        User, related_name='payments', on_delete=models.CASCADE)
    gateway = models.ForeignKey(Gateway, on_delete=models.CASCADE)
    price = models.PositiveBigIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
