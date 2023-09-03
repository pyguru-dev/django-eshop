from django.urls import path
from .views import PostListView, PostDetailView, post_detail

# app_name = 'blog'

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('<int:pk>/', post_detail, name='post_detail'),
    # path('<int:post_id>/vote', VoteView.as_view(), name='post_detail'),
]
