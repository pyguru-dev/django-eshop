from django.urls import path
from .views import UserlistView, RequestView, RequestListView

urlpatterns = [
    path('users/', UserlistView.as_view()),
    path('request/', RequestView.as_view()),
    path('requests-list/', RequestListView.as_view()),
    path('accept/'),
    path('friends/'),
]
