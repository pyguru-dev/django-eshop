from django.urls import path
from .views import AboutView, ContactCreateView, HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home_view'),
    path('about/', AboutView.as_view(), name='about_view'),
    path('contact/', ContactCreateView.as_view(), name='contact_view'),
]
