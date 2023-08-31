import datetime
from django.db.models.query import QuerySet
from django.urls import reverse
from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from ckeditor.fields import RichTextField
from django.utils import timezone
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from treebeard.mp_tree import MP_Node


class Rate(models.Model):
    rate = models.PositiveBigIntegerField()
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveBigIntegerField()
    content_object = GenericForeignKey()

    class Meta:
        indexes = [
            models.Index(fields=['content_type', 'object_id'])
        ]


class PublishedManager(models.Manager):
    def get_queryset(self) -> QuerySet:
        return super(PublishedManager, self).get_queryset().filter(status='p')


class Post(models.Model):
    objects = models.Manager()
    published = PublishedManager()
    PUBLISHED_STATUS = (
        ('p', 'Published'),
        ('d', 'Draft'),
    )

    author = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(_('عنوان'), max_length=150)
    # slug = models.SlugField(unique=True)
    body = RichTextField()
    thumbnail = models.ImageField(upload_to="posts/%Y/%m/%d")
    published_status = models.CharField(
        max_length=1, choices=PUBLISHED_STATUS, default='d')
    # category = models.ForeignKey("Category", related_name='post', verbose_name='categories', on_delete=models.CASCADE)
    # tags = models.ManyToManyField("Tag", verbose_name='tags', related_name='posts')

    likes = models.PositiveBigIntegerField(default=0)
    dislikes = models.PositiveBigIntegerField(default=0)
    rates = GenericRelation(Rate)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = 'Posts'

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse("post_detail",  args=[str(self.id)])

    def posts_was_published_recently(self):
        return self.created_at >= timezone.now() - datetime.timedelta(days=1)


class Comment(models.Model):
    comment = models.TextField(max_length=250)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    article = models.ForeignKey(
        Post, related_name='comments', on_delete=models.CASCADE)

    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.comment

    def get_absolute_url(self):
        return reverse("post_list")


class Category(MP_Node):
    parent = models.ForeignKey(
        'self', verbose_name='parent', blank=True, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, unique=True,
                            blank=False, null=False, db_index=True)
    slug = models.SlugField()
    description = models.TextField(blank=True, null=True, max_length=2048)
    is_active = models.BooleanField(default=True)
    # image = models.

    class Meta:
        # db_table = 'categories'
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def __str__(self) -> str:
        return self.name


class Tag(models.Model):
    name = models.TextField(max_length=100, unique=True,
                            blank=False, null=False)

    def __str__(self) -> str:
        return self.name


class RecyclePost(Post):

    deleted = models.Manager()

    class Meta:
        proxy = True


class Vote(models.Model):
    class VoteChoice(models.TextChoices):
        like = 'l', _('like')
        dislike = 'd', _('dislike')

    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='votes')
    vote = models.CharField(max_length=12, choices=VoteChoice.choices)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _('Vote')


# @receiver(post_save, sender=Vote)
# def update_votes(sender,instance, **kwargs):
#     if instance.vote = Vote.VoteChoice.like:
#         Post.objects.filter(id=instance.post.id).update(likes=F("likes") + 1)
#     else:
#         Post.objects.filter(id=instance.post.id).update(likes=F("dislikes") + 1)
