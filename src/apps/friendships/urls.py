from django.urls import path
from .views import (UserlistView, RequestView, RequestListView,
                    AcceptView, FriendListView,)

# app_name = 'apps.friendships'

urlpatterns = [
    path('users/', UserlistView.as_view()),
    path('request/', RequestView.as_view()),
    path('requests-list/', RequestListView.as_view()),
    path('accept/', AcceptView.as_view()),
    path('friends/', FriendListView.as_view()),
]
