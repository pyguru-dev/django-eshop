from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from django.http.request import HttpRequest
from django.utils.translation import gettext_lazy as _
from import_export.admin import ImportExportModelAdmin
from treebeard.admin import TreeAdmin
from treebeard.forms import movenodeform_factory
from .models import Post, Comment, RecyclePost, BlogCategory

# admin.site.disable_action('delete_selected')
# admin.site.site_header = ''


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['comment', 'is_approved',]
    list_filter = ['is_approved']


class CommentInline(admin.StackedInline):
    model = Comment
    extra = False


@admin.register(Post)
class PostAdmin(ImportExportModelAdmin):
    list_display = ['id', 'title', 'category',
                    'author', 'published_status', 'created_at',]
    list_filter = ['published_status', 'author','created_at']
    search_fields = ['title', 'author__username']
    list_display_links = ['id', 'title']
    inlines = [CommentInline]
    prepopulated_fields = {
        'slug' : ['title']
    }
    # fields = ['title', 'body', 'published_status']
    fieldsets = (
        (None, {'fields': ('title','slug', 'body','thumbnail', 'author', 'category')}),
        ("وضعیت", {'fields': ('published_status',)})
    )
    # filter_horizontal = ['tags']
    # resource_class = PostResource

    def tags_to_str(self, obj):
        return ", ".join(tag.title for tag in obj.tags.all())
    tags_to_str.short_description = _('برسب ها')


@admin.register(RecyclePost)
class PostAdmin(admin.ModelAdmin):

    actions = ['recover']

    def get_queryset(self, request):
        return RecyclePost.deleted.filter(is_deleted=True)

    @admin.action(description='Recover deleted item')
    def recover(self, request, queryset):
        queryset.update(is_deleted=False, deleted_at=None)

    @admin.action(description="Draft posts to published")
    def draft_to_published_posts(self, request, queryset):
        rows_updated = queryset.update(status="p")
        if rows_updated == 1:
            message_bit = 'منتشر شد.'
        else:
            message_bit = 'منتشر شدند.'
        self.message_user(request, "{} مقاله {}".format(
            rows_updated, message_bit))

    @admin.action(description="Published posts to draft")
    def published_to_draft_posts(self, request, queryset):
        queryset.update(status="d")


@admin.register(BlogCategory)
class BlogCategoryAdmin(TreeAdmin):
    form = movenodeform_factory(BlogCategory)
    prepopulated_fields = {
        'slug' : ['name']
    }
