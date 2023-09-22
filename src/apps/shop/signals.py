from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Product


# @receiver(post_save, sender=Product)
# def create_product_code(sender, instance, created, **kwargs):
#     if created:
#         pass
