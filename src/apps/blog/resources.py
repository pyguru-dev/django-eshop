from import_export import resources
from .models import Post, Category, Tag

class PostResource(resources.ModelResource):
    class Meta:
        model = Post
        fields = ['title', 'author__username', 'created_at']