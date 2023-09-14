from django.db import models
from django.db.models import Q
from django.utils.translation import gettext_lazy as _
from treebeard.mp_tree import MP_Node
from ckeditor.fields import RichTextField
from apps.accounts.models import User
from apps.core.models import BaseModel
from apps.payments.models import Payment


class ProductAttributeValue(BaseModel):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    attribute = models.ForeignKey('ProductAttribute', on_delete=models.CASCADE)

    value_text = models.TextField(null=True, blank=True)
    value_integer = models.IntegerField(null=True, blank=True)
    value_float = models.FloatField(null=True, blank=True)
    value_option = models.ForeignKey(
        'OptionGroupValue', on_delete=models.PROTECT)
    value_multi_option = models.ManyToManyField(
        'OptionGroupValue', related_name='option_groups')

    class Meta:
        verbose_name = _('product attribute value')
        verbose_name_plural = _('محصولات')
        unique_together = ('product', 'attribute')


class OptionGroup(BaseModel):
    title = models.CharField(max_length=255, db_index=True)


class OptionGroupValue(BaseModel):
    title = models.CharField(max_length=255, db_index=True)
    group = models.ForeignKey(OptionGroup, on_delete=models.CASCADE)


class ProductAttribute(BaseModel):

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


class Option(BaseModel):
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


class Brand(BaseModel):
    # country_id, en_title, site_link, description
    title = models.CharField(
        max_length=255, blank=False, null=False, unique=True, verbose_name=_('عنوان'))
    slug = models.SlugField(
        unique=True, allow_unicode=True, verbose_name=_('اسلاگ'))
    logo = models.ImageField(
        upload_to='brands/', null=False, blank=False, verbose_name=_('لوگو'))

    class Meta:
        verbose_name = _("برند")
        verbose_name_plural = _("برند ها")


class ProductCategory(MP_Node):
    parent = models.ForeignKey(
        'self', verbose_name=_('دسته بندی والد'), blank=True, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, unique=True,
                            blank=False, null=False, db_index=True, verbose_name=_('عنوان'))
    slug = models.SlugField(max_length=255, unique=True,
                            verbose_name=_('اسلاگ'), allow_unicode=True)
    description = models.TextField(
        blank=True, null=True, max_length=2048, verbose_name=_('توضیحات'))
    is_active = models.BooleanField(
        default=True, verbose_name=_('دسته بندی فعال باشد?'))
    # image = models.
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'product_categories'
        verbose_name = _("دسته بندی")
        verbose_name_plural = _("دسته بندی ها")

    def __str__(self) -> str:
        return self.name


class Product(BaseModel):
    # en_title, sku,product_status : approved - rejected  , ...
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
        unique=True, allow_unicode=True, verbose_name=_('اسلاگ'), default=None)
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

    category = models.ForeignKey(ProductCategory, verbose_name=_(
        'دسته بندی'), on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, verbose_name=_(
        'برند'), on_delete=models.CASCADE)

    # product_class = models.ForeignKey(ProductClass, on_delete=models.PROTECT, null=True, blank=True, related_name='products')
    # attributes = models.ManyToManyField('ProductAttribute', through='ProductAttributeValue')

    # tags = models.ManyToManyField("Tag", verbose_name='tags', related_name='posts')
    # recommended_products = models.ManyToManyField('catalog.Proudct',through='ProductRecommendation', blank=True)
    
    class Meta:
        verbose_name = _('محصول')
        verbose_name_plural = _('محصولات')

    def __str__(self) -> str:
        return self.title

    def has_attribute(self):
        return self.attributes.exists()


class ProductImages(BaseModel):
    # product - image - alt -  order priority
    product = models.ForeignKey(
        Product, related_name='images', on_delete=models.CASCADE)

    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='uploads/', blank=True, null=True)

    def save(self, *args, **kwargs):
        self.thumbnail = self.make_thumbnail(self.image)

        super().save(*args, **kwargs)

    def make_thumbnail(self, image, size=(300, 200)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)

        thumbnail = File(thumb_io, name=image.name)

        return thumbnail


class ProductRecommendation(BaseModel):
    primary = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='primary_recommendation')
    recommendation = models.ForeignKey(Product, on_delete=models.CASCADE)
    rank = models.PositiveSmallIntegerField(default=0)

    class Meta:
        unique_together = ('primary', 'recommendation')
        ordering = ('primary', '-rank')


class Order(BaseModel):

    class OrderStatus(models.TextChoices):
        processing = 'Processing'

    ORDER_STATUS = (
        ('p', 'Processing'),
        ('d', 'Delivered'),
        ('s', 'Shipped'),
    )

    class Meta:
        db_table = 'orders'
        verbose_name = _('سفارش')
        verbose_name_plural = _('سفارش ها')

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    tracking_code = models.CharField(
        max_length=150, null=False, blank=False, unique=True, verbose_name=_('کد پیگیری'))
    payment = models.ForeignKey(
        Payment, on_delete=models.CASCADE)
    order_status = models.CharField(
        max_length=40, choices=OrderStatus.choices, default='pending')
    # user, address, shipping, discount, user_description,
    # user_cancel_description, total_amount, payment_method,
    # payment_status

    def __str__(self):
        return '#' + self.tracking_code


class OrderItem(BaseModel):
    class Meta:
        db_table = 'order_items'
        verbose_name = _('آیتم های سفارش')
        verbose_name_plural = _('آیتم های سفارش ها')

    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name='orders')
    quantity = models.PositiveIntegerField(default=0)
    product_amount = models.PositiveBigIntegerField(default=0)
    total_product_amount = models.PositiveBigIntegerField(default=0)

    def __str__(self) -> str:
        return '#' + self.order.tracking_code


class Wishlist(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('علاقه مندی')
        verbose_name_plural = _('علاقه مندی ها')


class Cart(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)


class CartItem(BaseModel):
    pass


class Discount(BaseModel):
    title = models.CharField(
        max_length=255, unique=True, verbose_name=_('عنوان'))
    code = models.CharField(
        max_length=255, unique=True, verbose_name=_('کد'))
    description = models.CharField(
        max_length=255, unique=True, verbose_name=_('توضیحات'))
    value = models.CharField(
        max_length=255, unique=True, verbose_name=_('مقدار'))
    infinity = models.BooleanField(verbose_name=_('نامحدود'), default=False)
    count_use = models.PositiveIntegerField(
        default=0, verbose_name=_('تعداد قابل استفاده'))
    count_use_user = models.PositiveIntegerField(
        default=0, verbose_name=_('تعداد قابل استفاده برای کاربر'))
    used = models.PositiveIntegerField(
        default=0, verbose_name=_('تعداد استفاده شده'))
    start_at = models.DateTimeField(verbose_name=_('زمان شروع'))
    end_at = models.DateTimeField(verbose_name=_('زمان پایان'))
    #  type

    class Meta:
        verbose_name = _('تخفیف')
        verbose_name_plural = _('تخفیف ها')


class Giftcode(BaseModel):
    title = models.CharField(
        max_length=255, unique=True, verbose_name=_('عنوان'))
    code = models.CharField(
        max_length=255, unique=True, verbose_name=_('کد'))
    description = models.CharField(
        max_length=255, unique=True, verbose_name=_('توضیحات'))
    value = models.CharField(
        max_length=255, verbose_name=_('مقدار'))
    infinity = models.BooleanField(verbose_name=_('نامحدود'), default=False)
    count_use = models.PositiveIntegerField(
        default=0, verbose_name=_('تعداد قابل استفاده'))
    count_use_user = models.PositiveIntegerField(
        default=0, verbose_name=_('تعداد قابل استفاده برای کاربر'))
    used = models.PositiveIntegerField(
        default=0, verbose_name=_('تعداد استفاده شده'))

    class Meta:
        verbose_name = _('کد هدیه')
        verbose_name_plural = _('کد هدیه ها')

    def __str__(self):
        return self.code

    def can_use(self):
        is_active = True

        if self.active == False:
            is_active = False

        if self.num_used >= self.num_available and self.num_available != 0:
            is_active = False

        return is_active

    def use(self):
        self.num_used = self.num_used + 1

        if self.num_used == self.num_available:
            self.active = False

        self.save()


class Shipping(BaseModel):
    title = models.CharField(
        max_length=255, unique=True, verbose_name=_('عنوان'))
    amount = models.CharField(
        max_length=255, verbose_name=_('قیمت'))
    description = models.CharField(
        max_length=255, verbose_name=_('توضیحات'), null=True, blank=True)
    logo = models.CharField(
        max_length=255, verbose_name=_('لوگو'), null=True, blank=True)


class Warranty(BaseModel):
    title = models.CharField(
        max_length=255, unique=True, verbose_name=_('عنوان'))

    class Meta:
        verbose_name = _('گارانتی')
        verbose_name_plural = _('گارانتی ها')
