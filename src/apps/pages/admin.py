from django.contrib import admin
from .models import ContactModel, ContactSubject, Faq, FaqGroup

@admin.register(ContactModel)
class ContactModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'mobile', 'message']
    
@admin.register(ContactSubject)
class ContactSubjectAdmin(admin.ModelAdmin):
    # list_display = ['name']
    pass

@admin.register(Faq)
class FaqAdmin(admin.ModelAdmin):
    # list_display = ['question', 'created_at]
    pass

@admin.register(FaqGroup)
class FaqGroupAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    