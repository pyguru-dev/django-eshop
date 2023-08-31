from datetime import timezone
from django.db import models
from django.db.models import Q
from ckeditor.fields import RichTextField
from apps.accounts.models import CustomUser


class Product(models.Model):
    PUBLISHED_STATUS = (
        ('p', 'Published'),
        ('d', 'Draft'),
    )
    author = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name='products')
    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(unique=True)
    body = RichTextField()
    price = models.PositiveBigIntegerField(null=False, blank=False)
    thumbnail = models.ImageField(upload_to="posts/%Y/%m/%d")
    published_status = models.CharField(
        max_length=1, choices=PUBLISHED_STATUS, default='d')
    # category = models.ForeignKey("Category", related_name='post', verbose_name='categories', on_delete=models.CASCADE)
    # tags = models.ManyToManyField("Tag", verbose_name='tags', related_name='posts')
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Products'

    def __str__(self) -> str:
        return self.title


class File(models.Model):
    pass


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
