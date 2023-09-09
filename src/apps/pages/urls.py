from django.urls import path
from .views import (AboutView, ContactCreateView, HomePageView, FaqsView)

# app_name= 'apps.pages'

urlpatterns = [
    path('', HomePageView.as_view(), name='home_view'),
    path('about/', AboutView.as_view(), name='about_view'),
    path('contact/', ContactCreateView.as_view(), name='contact_view'),
    path('faqs/', FaqsView.as_view(), name='faqs_view'),
]
