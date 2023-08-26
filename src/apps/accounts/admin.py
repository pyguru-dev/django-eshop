from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserChangeForm, CustomUserCreationForm


# @admin.register(DJUser)
# class CustomUserAdmin(UserAdmin):
#     add_form = CustomUserCreationForm()
#     form = CustomUserChangeForm
#     model = DJUser
#     list_display = ['username', 'email', 'is_staff']
#     fieldsets = UserAdmin.fieldsets + (
#         (None, {'fields': ('mobile',)}),
#     )
#     add_fieldsets = UserAdmin.fieldsets + (
#         (None, {'fields': ('mobile',)})
#     )
