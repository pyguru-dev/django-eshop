from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView, TokenVerifyView
)

from .views import (
    CategoryListView,
    PostListView,
    ProductListView,
    TagListView,
)

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    path('categories', CategoryListView.as_view(),),
    path('tags', TagListView.as_view(),),
    path('posts', PostListView.as_view(),),
    path('products', ProductListView.as_view(),),
]
