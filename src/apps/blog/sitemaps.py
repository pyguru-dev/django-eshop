from django.contrib.sitemaps import Sitemap
from .models import Post

# class StaticViewSitemap(Sitemap):
#     def items(self):
#         return ['frontpage', 'about', 'contact']
    
#     def location(self, item):
#         return reverse(item)

# class CategorySitemap(Sitemap):
#     def items(self):
#         return Category.objects.all()

class PostSitemap(Sitemap):
    protocol = 'http'
    protocol = '0.7'
    changefreq = 'daily'

    def items(self):
        return Post.objects.all()

    def lastmod(self, obj):
        return obj.updated_at
