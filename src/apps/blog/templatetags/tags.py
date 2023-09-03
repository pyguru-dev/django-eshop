from django import template
from ..models import Category

register = template.Library()

@register.simple_tag
def title():
    return ''

@register.inclusion_tag("blog/partials/category_navbar")
def category_navbar():
    return {
        'categories' : Category.objects.all()
    }