from celery import shared_task
from .models import Product


@shared_task
def count_products():
    return Product.objects.count()
