from datetime import timezone
from django.db import models
from django.db.models import Q
from ckeditor.fields import RichTextField
from django.contrib.auth import get_user_model
# from apps.accounts.models import User


User = get_user_model()

class Product(models.Model):
    PUBLISHED_STATUS = (
        ('p', 'Published'),
        ('d', 'Draft'),
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='products')
    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(unique=True, allow_unicode=True)
    body = RichTextField()
    price = models.PositiveBigIntegerField(null=False, blank=False)
    thumbnail = models.ImageField(upload_to="posts/%Y/%m/%d")
    published_status = models.CharField(
        max_length=1, choices=PUBLISHED_STATUS, default='d')

    track_stock = models.BooleanField(default=True)
    require_shipping = models.BooleanField(default=True)
    options = models.ManyToManyField('Option', blank=True)
    
    # category = models.ForeignKey("Category", related_name='post', verbose_name='categories', on_delete=models.CASCADE)
    # tags = models.ManyToManyField("Tag", verbose_name='tags', related_name='posts')
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

        

    def __str__(self) -> str:
        return self.title

    def has_attribute(self):
        return self.attributes.exists()


class OptionGroup(models.Model):
    title = models.CharField(max_length=255, db_index=True)


class OptionGroupValue(models.Model):
    title = models.CharField(max_length=255, db_index=True)
    group = models.ForeignKey(OptionGroup, on_delete=models.CASCADE)


class ProductAttribute(models.Model):

    class AttributeTypeChoice(models.TextChoices):
        text = 'text'
        integer = 'integer'
        float = 'float'
        option = 'option'
        multi_option = 'multi_option'

    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, null=True, related_name='attributes')
    title = models.CharField(max_length=64)
    type = models.CharField(
        max_length=16, choices=AttributeTypeChoice.choices, default=AttributeTypeChoice.text)
    option_group = models.ForeignKey(
        OptionGroup, on_delete=models.PROTECT, null=True, blank=True)
    required = models.BooleanField(default=False)


class Option(models.Model):
    class OptionTypeChoice(models.TextChoices):
        text = 'text'
        integer = 'integer'
        float = 'float'
        option = 'option'
        multi_option = 'multi_option'

    title = models.CharField(max_length=64)
    type = models.CharField(
        max_length=16, choices=OptionTypeChoice.choices, default=OptionTypeChoice.text)
    option_group = models.ForeignKey(
        OptionGroup, on_delete=models.PROTECT, null=True, blank=True)
    required = models.BooleanField(default=False)


class Brand(models.Model):
    title = models.CharField(max_length=255, blank=False,null=False, unique=True)
    logo = models.ImageField(upload_to='brands/',null=False,blank=False)



class SoftDeleteQuerySet(models.QuerySet):
    def delete(self):
        return self.update(is_deleted=True, deleted_at=timezone.now())


class SoftDeleteManager(models.Manager):
    def get_queryset(self):
        return SoftDeleteQuerySet(self.model, self._db).filter(Q(is_deleted=False) | Q(is_deleted__isnull=True))


class SoftDelete(models.Model):
    is_deleted = models.BooleanField(null=True, blank=True, editable=False)
    deleted_at = models.DateTimeField(null=True, blank=True, editable=False)

    objects = SoftDeleteManager()

    class Meta:
        abstract = True

    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()


