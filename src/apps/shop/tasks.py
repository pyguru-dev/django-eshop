from PIL import Image
from django.core.files.base import File
from io import BytesIO
from celery import shared_task
from .models import Product


@shared_task
def count_products():
    return Product.objects.count()


@shared_task()
def create_product_thumbnail(product_id):
    product = Product.objects.get(pk=product_id)
    image = Image.open(product.thumbnail.path)
    new_width, new_height = (160, 160)
    image.thumbnail((new_width, new_height))
    img_temp = BytesIO()
    image.save(img_temp, "PNG")
    product.thumbnail = File(img_temp, product.thumbnail.name.split("/")[-1])
    product.save()
