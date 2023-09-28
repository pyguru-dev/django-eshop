from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Factor, IrBank, Payment


@admin.register(Payment)
class PaymentAdmin(ImportExportModelAdmin):
    list_display = ['id','user']


@admin.register(Factor)
class FactorAdmin(ImportExportModelAdmin):
    list_display = ['id', 'file', 'payment']


@admin.register(IrBank)
class IrBankAdmin(ImportExportModelAdmin):
    list_display = ['id', 'title', 'logo']
