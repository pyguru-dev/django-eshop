from typing import Any, List, Tuple
from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Product, ProductAttribute


class ProductAttributeInline(admin.TabularInline):
    model = ProductAttribute
    extra = 1

class AttributeCountFilter(admin.SimpleListFilter):
    parameter_name = 'attr_count'
    title = 'Attribute Count'
    
    def lookups(self, request, model_admin):
        return [
            ('more_5', 'More Than 5'),
            ('lower_5', 'Lower Than 5'),
        ]

@admin.register(Product)
class ProductAdmin(ImportExportModelAdmin):
    list_display = ['id', 'title', 'price', 'published_status', 'created_at']
    list_filter = ['price', 'published_status']
    search_fields = ['title']
    inlines = [ProductAttributeInline]

    def attribute_count(self, obj):
        return obj.attributes.count()

    