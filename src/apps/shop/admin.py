from import_export.admin import ExportActionModelAdmin
from typing import Any, List, Tuple
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from django.contrib import admin
from .models import Brand, Discount, Giftcode, Product, ProductAttribute, Order, OrderItem, ProductCategory, ProductImages, ProductRecommendation, Shipping, Warranty


class ProductImagesInline(admin.TabularInline):
    model = ProductImages


class ProductAttributeInline(admin.TabularInline):
    model = ProductAttribute
    extra = 1


class ProductRecommendationInline(admin.StackedInline):
    model = ProductRecommendation
    extra = 2
    fk_name = 'primary'


class AttributeCountFilter(admin.SimpleListFilter):
    parameter_name = 'attr_count'
    title = 'Attribute Count'

    def lookups(self, request, model_admin):
        return [
            ('more_5', 'More Than 5'),
            ('lower_5', 'Lower Than 5'),
        ]

    def queryset(self, request, queryset):
        if self.value() == 'more_5':
            return queryset.annotate(attr_count=Count('attributes')).filter(attr_count__gt=2)
        if self.value() == 'lower_5':
            return queryset.annotate(attr_count=Count('attributes')).filter(attr_count__lte=2)


@admin.register(Product)
class ProductAdmin(ImportExportModelAdmin):
    list_display = ['id', 'title', 'price', 'published_status', 'created_at']
    list_filter = ['price', 'published_status']
    search_fields = ['title']
    inlines = [ProductAttributeInline]
    actions = ['enable_track_stock']
    prepopulated_fields = {
        'slug': ('title',)
    }
    raw_id_fields = ['author']
    # list_editable = ['publish_status']
    list_display_links = ('title',)

    def attribute_count(self, obj):
        return obj.attributes.count()

    def enable_track_stock(self, request, queryset):
        queryset.update(track_stock=True)


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = False


@admin.register(Order)
class OrderAdmin(ImportExportModelAdmin):
    list_display = []
    # inlines = [OrderItemInline]


@admin.register(Shipping)
class ShippingAdmin(ImportExportModelAdmin):
    list_display = []


@admin.register(Warranty)
class WarrantyAdmin(ImportExportModelAdmin):
    list_display = []


@admin.register(Giftcode)
class GiftcodeAdmin(ImportExportModelAdmin):
    list_display = []


@admin.register(Discount)
class DiscountAdmin(ImportExportModelAdmin):
    list_display = []


class BrandResource(resources.ModelResource):
    class Meta:
        model = Brand
        fields = ('id','title')


@admin.register(Brand)
class BrandAdmin(ExportActionModelAdmin, ImportExportModelAdmin):
    resource_class = BrandResource
    list_display = ['title', 'slug', 'en_title', 'site_link', 'created_at']
    prepopulated_fields = {
        'slug': ('title',)
    }


@admin.register(ProductCategory)
class ProductCategoryAdmin(ImportExportModelAdmin):
    list_display = []
    prepopulated_fields = {
        'slug': ('name',)
    }
