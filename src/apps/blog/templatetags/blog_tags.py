from django import template
import datetime
from ..models import BlogCategory, Post

register = template.Library()


@register.simple_tag
def title():
    return ''


@register.inclusion_tag("blog/partials/category_navbar")
def category_navbar():
    return {
        'categories': BlogCategory.objects.all()
    }


@register.inclusion_tag('partials/link.html')
def link(request, link_name, content):
    return {
        'request': request,
        'link_name': link_name,
        'link': '',
        'content': content
    }


@register.simple_tag
def number_of_posts(for_today=False):
    if for_today:
        today = datetime.date.today()
        return Post.published.filter(created_at__year=today.year, created_at__month=today.month, created_at__day=today.day).count()

    return Post.published.count()


@register.simple_tag
def latest_posts(count=8):
    return Post.published.order_by('-created_at')[:count]
