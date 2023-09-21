from django.urls import path
from .views import (PostListView, PostDetailView,
                    AuthorListView, AuthorDetailView,
                    BlogCategoryListView,BlogCategoryDetailView,)

# app_name = 'apps.blog'

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('<str:slug>/', PostDetailView.as_view(), name='post_detail'),
    # re_path(r'(?P<slug>[-\w]+)/',post_detail)
    
    path('categories', BlogCategoryListView.as_view(), name='blog_category_list'),
    path('categories/<str:slug>', BlogCategoryDetailView.as_view(), name='blog_category_detail'),
    
    # path('<int:post_id>/vote', VoteView.as_view(), name='post_detail'),
    path('authors', AuthorListView.as_view(), name='author_list'),
    # path('authors/<pk>', AuthorDetailView.as_view(), name='author_detail'),
]
