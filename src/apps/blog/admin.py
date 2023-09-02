from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from django.http.request import HttpRequest
from import_export.admin import ImportExportModelAdmin
from treebeard.admin import TreeAdmin
from treebeard.forms import movenodeform_factory
from .models import Post, Comment, RecyclePost, Category, Tag


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


@admin.register(RecyclePost)
class PostAdmin(admin.ModelAdmin):

    actions = ['recover']

    def get_queryset(self, request):
        return RecyclePost.deleted.filter(is_deleted=True)

    @admin.action(description='Recover deleted item')
    def recover(self, request, queryset):
        queryset.update(is_deleted=False, deleted_at=Null)


@admin.register(Category)
class CategoryAdmin(TreeAdmin):
    form = movenodeform_factory(Category)

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']