from django.contrib import admin
from .models import Payment, Gateway


@admin.register(Gateway)
class GatewayAdmin(admin.ModelAdmin):
    list_display = []


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = []
