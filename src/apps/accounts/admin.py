from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from import_export.admin import ImportExportModelAdmin
# from .forms import CustomUserChangeForm, CustomUserCreationForm


admin.site.register(User,UserAdmin)

# @admin.register(User, UserAdmin)
# class UserAdmin(ImportExportModelAdmin):
#     # add_form = CustomUserCreationForm
#     # form = CustomUserChangeForm
#     model = User
#     list_display = ['username', 'email', 'mobile', 'is_staff', 'is_superuser']
#     search_fields = ['username', 'email', 'mobile']
#     list_filter = ['is_staff', 'is_superuser']
#     fieldsets = UserAdmin.fieldsets + (
#         (None, {'fields': ('mobile',)}),
#     )
#     add_fieldsets = UserAdmin.fieldsets + (
#         (None, {'fields': ('mobile',)})
#     )
#     class Meta:
#         pass
