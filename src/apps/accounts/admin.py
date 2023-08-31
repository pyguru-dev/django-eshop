from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from import_export.admin import ImportExportModelAdmin
from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(ImportExportModelAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['username', 'email', 'mobile', 'is_staff', 'is_superuser']
    search_fields = ['username', 'email', 'mobile']
    list_filter = ['is_staff', 'is_superuser']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('mobile',)}),
    )
    add_fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('mobile',)})
    )
