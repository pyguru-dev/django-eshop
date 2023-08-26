from django.contrib import admin
from .models import Post, Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['comment']


class CommentInline(admin.StackedInline):
    model = Comment
    extra = False


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author', 'published_status', 'created_at']
    list_filter = ['published_status']
    search_fields = ['title', 'author__username']
    inlines = [CommentInline]
    # fields = ['title', 'body', 'published_status']
    fieldsets = (
        (None, {'fields': ('title', 'body')}),
        ("Status", {'fields': ('published_status',)})
    )
