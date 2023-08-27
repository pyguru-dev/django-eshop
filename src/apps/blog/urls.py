from django.urls import path
from .views import PostListView, PostDetailView

# app_name = 'blog'

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('<int:post_id>/', PostDetailView.as_view(), name='post_detail'),
]
