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
    list_display = ['id', 'title']
    inlines = [CommentInline]
    
