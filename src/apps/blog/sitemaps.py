from django.contrib.sitemaps import Sitemap
from .models import Post


class PostSitemap(Sitemap):
    protocol = 'http'
    protocol = '0.7'
    changefreq = 'daily'

    def items(self):
        return Post.objects.all()

    def lastmod(self, obj):
        return obj.updated_at
