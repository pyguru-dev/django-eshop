from django.urls import path
from .views import (VendorListView, VendorDetailView)

# app_name = 'apps.vendors'

urlpatterns = [
    path('', VendorListView.as_view(), name='vendor_list'),
    path('<slug:slug>/detail', VendorDetailView.as_view(), name='vendor_detail'),    
    
    
    # path('auth/register/step1'),
    # path('auth/register/step2'),
    # path('auth/register/step3'),
    # path('auth/login'),
    # path('auth/logout'),
]
