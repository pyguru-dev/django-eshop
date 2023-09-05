from datetime import timezone
from django.db import models
from django.db.models import Q
from ckeditor.fields import RichTextField
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from apps.blog.models import Category


User = get_user_model()

class ProductAttributeValue(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    attribute = models.ForeignKey('ProductAttribute', on_delete=models.CASCADE)

    value_text = models.TextField(null=True,blank=True)
    value_integer = models.IntegerField(null=True,blank=True)
    value_float = models.FloatField(null=True,blank=True)
    value_option =  models.ForeignKey('OptionGroupValue', on_delete=models.PROTECT)
    value_multi_option = models.ManyToManyField('OptionGroupValue', related_name='option_groups')
    
    
    class Meta:
        verbose_name = _('product attribute value')
        verbose_name_plural = _('محصولات')
        unique_together = ('product', 'attribute')
    
    
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
        'Product', on_delete=models.CASCADE, null=True, related_name='attributes')
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
    title = models.CharField(
        max_length=255, blank=False, null=False, unique=True)
    slug = models.SlugField(
        unique=True, allow_unicode=True, verbose_name=_('اسلاگ'))
    logo = models.ImageField(upload_to='brands/', null=False, blank=False)



class Product(models.Model):
    PUBLISHED_STATUS = (
        ('p', 'Published'),
        ('d', 'Draft'),
    )

    class ProductTypeChoice(models.TextChoices):
        standalone = 'standalone'
        parent = 'parent'
        child = 'child'
        
    structure = models.CharField(
        max_length=16, choices=ProductTypeChoice.choices, default=ProductTypeChoice.standalone)
    parent = models.ForeignKey(
        "self", related_name='children', on_delete=models.CASCADE, null=True, blank=True)
    
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='products', verbose_name=_('نویسنده'))
    title = models.CharField(
        max_length=255, unique=True, verbose_name=_('عنوان '))
    slug = models.SlugField(
        unique=True, allow_unicode=True, verbose_name=_('اسلاگ'),default=None)
    body = RichTextField(verbose_name=_('توضیحات '))
    price = models.PositiveBigIntegerField(
        null=False, blank=False, verbose_name=_('قیمت'))
    thumbnail = models.ImageField(
        upload_to="posts/%Y/%m/%d", verbose_name=_('تصویر شاخص'))
    published_status = models.CharField(
        max_length=1, choices=PUBLISHED_STATUS, default='d', verbose_name=_('وضعیت انتشار'))

    track_stock = models.BooleanField(default=True)
    require_shipping = models.BooleanField(default=True)
    options = models.ManyToManyField('Option', blank=True)

    category = models.ForeignKey(Category, verbose_name=_('دسته بندی'), on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, verbose_name=_('برند'), on_delete=models.CASCADE)
    
    # product_class = models.ForeignKey(ProductClass, on_delete=models.PROTECT, null=True, blank=True, related_name='products')
    # attributes = models.ManyToManyField('ProductAttribute', through='ProductAttributeValue')
    
    # tags = models.ManyToManyField("Tag", verbose_name='tags', related_name='posts')
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name=_('تاریخ بروزرسانی'))
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name=_('تاریخ ثبت'))

    class Meta:
        verbose_name = _('محصول')
        verbose_name_plural = _('محصولات')

    def __str__(self) -> str:
        return self.title

    def has_attribute(self):
        return self.attributes.exists()
