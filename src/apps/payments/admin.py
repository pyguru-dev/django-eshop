from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Payment, Gateway


@admin.register(Gateway)
class GatewayAdmin(admin.ModelAdmin):
    list_display = []


@admin.register(Payment)
class PaymentAdmin(ImportExportModelAdmin):
    list_display = ['id','price']
