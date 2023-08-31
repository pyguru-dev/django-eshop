from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Product


@admin.register(Product)
class ProductAdmin(ImportExportModelAdmin):
    list_display = ['id', 'title', 'price', 'published_status', 'created_at']
    list_filter = ['price', 'published_status']
    search_fields = ['title']
