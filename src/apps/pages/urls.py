from django.urls import path
from .views import AboutView, HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home_view'),
    path('about/',AboutView.as_view(), name='about_view'),
]
