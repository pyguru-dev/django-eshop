from django.urls import path
from .views import PostListView, PostDetailView, post_detail, AuthorListView, AuthorDetailView

# app_name = 'blog'

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('<int:pk>/', post_detail, name='post_detail'),
    # re_path(r'(?P<slug>[-\w]+)/',post_detail)
    # path('<int:post_id>/vote', VoteView.as_view(), name='post_detail'),
    path('authors', AuthorListView.as_view(), name='author_list'),
    # path('authors/<pk>', AuthorDetailView.as_view(), name='author_detail'),
]
