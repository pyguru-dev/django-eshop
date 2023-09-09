from django.urls import path
from .views import create_url, url_redirect

# app_name = 'apps.shortener'

urlpatterns = [
    # path('',),
    path('<str:slug>/', url_redirect, name='shortener_redirect')
]
