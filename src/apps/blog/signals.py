from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Post
from django.utils.text import slugify


@receiver(pre_save, sender=Post)
def create_post(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug = create_unique_slug(instance)


def create_unique_slug(instance, new_slug=None):
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.title, allow_unicode=True)

    instanceClass = instance.__class__
    qs = instanceClass.objects.filter(slug=slug)

    if qs.exists():
        new_slug = f"{slug}-{qs.first().id}"
        return create_unique_slug(instance, new_slug)

    return slug
