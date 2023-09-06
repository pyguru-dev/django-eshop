from django import template
from ..models import BlogCategory

register = template.Library()

@register.simple_tag
def title():
    return ''

@register.inclusion_tag("blog/partials/category_navbar")
def category_navbar():
    return {
        'categories' : BlogCategory.objects.all()
    }
    
    
@register.inclusion_tag('partials/link.html')
def link(request,link_name,content):
    return {
        'request': request,
        'link_name': link_name,
        'link' : '',
        'content' : content
    }