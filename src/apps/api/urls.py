from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView, TokenVerifyView
)
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView


from .views import (
    CategoryListView,
    PostListView,
    ProductListView,
    TagListView,
)

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('schema/swagger-ui/',
         SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('schema/redoc/',
         SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

    path('categories', CategoryListView.as_view(),),
    path('tags', TagListView.as_view(),),
    path('posts', PostListView.as_view(),),
    path('products', ProductListView.as_view(),),
]
