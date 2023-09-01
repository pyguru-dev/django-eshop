from django.contrib import admin
from .models import Url


@admin.register(Url)
class UrlAdmin(admin.ModelAdmin):
    list_display = ['url', 'slug', 'visit_count', 'created_at']
    readonly_fields = ['visit_count']
    list_filter = ['created_at']
    search_fields = ['url', 'slug']
