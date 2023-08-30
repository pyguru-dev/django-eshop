from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models import Post, Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['comment', 'is_approved', 'created_at']
    list_filter = ['is_approved']


class CommentInline(admin.StackedInline):
    model = Comment
    extra = False


@admin.register(Post)
class PostAdmin(ImportExportModelAdmin):
    list_display = ['id', 'title', 'author', 'published_status', 'created_at']
    list_filter = ['published_status']
    search_fields = ['title', 'author__username']
    inlines = [CommentInline]
    # fields = ['title', 'body', 'published_status']
    fieldsets = (
        (None, {'fields': ('title', 'body', 'author')}),
        ("Status", {'fields': ('published_status',)})
    )
    # filter_horizontal = ['tags']
    # resource_class = PostResource
