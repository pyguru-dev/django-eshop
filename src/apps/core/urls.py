from django.urls import path

from apps.blog.sitemaps import PostSitemap
from apps.shop.sitemaps import ProductSitemap

# app_name = 'apps.core'

sitemaps = {
    'posts' : PostSitemap,
    'products' : ProductSitemap,
}

urlpatterns = [
    
]
