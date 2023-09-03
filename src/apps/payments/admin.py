from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Payment, Gateway


@admin.register(Gateway)
class GatewayAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']


@admin.register(Payment)
class PaymentAdmin(ImportExportModelAdmin):
    list_display = ['id', 'price']
