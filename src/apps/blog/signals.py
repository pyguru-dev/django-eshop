from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from .models import Comment, Post
from django.utils.text import slugify


@receiver(pre_save, sender=Post)
def create_post(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug = create_unique_slug(instance)

# @receiver(post_save, sender=Vote)
# def update_votes(sender,instance, **kwargs):
#     if instance.vote = Vote.VoteChoice.like:
#         Post.objects.filter(id=instance.post.id).update(likes=F("likes") + 1)
#     else:
#         Post.objects.filter(id=instance.post.id).update(likes=F("dislikes") + 1)


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

# @receiver(post_save, sender=Comment)
# def create_post_comment_reply_notification_sinal(sender, instance, created, *args, **kwargs):
#     """
#     create notification when user reply comment
#     """
#     if created and instance.parent_id:
#         if instance.parent.user != instance.user:
#             message = ''
#             post = instance.post
#             Notification.objects.create(user,instance.parent.user, message)
            

# @receiver(post_save, sender=Post)
# def create_new_post_notification_signal(sender, instance, *args, **kwargs):
#     """
#     create notification when created new post
#     """
#     if created:
#         message = f''
#         post = instance
#         users = User.objects.all()
#         brodcastNotification = BrodcastNotification.objects.create(message=message)
#         brodcastNotification.users.set(users)