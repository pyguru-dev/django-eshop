from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView, TokenVerifyView
)
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

from .views import (
    CategoryListView,
    PostListView,
    ProductListView,
    TagViewSet,
    RegisterView,
)

router = routers.DefaultRouter()
router.register(r'tags', TagViewSet)
# router.register(r'categories', TagViewSet)
# router.register(r'posts', TagViewSet)
# router.register(r'products', TagViewSet)

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    
    path('register/', RegisterView.as_view()),
        
    path('', include(router.urls)),
    path('categories/', CategoryListView.as_view(),),
    path('posts/', PostListView.as_view(),),
    path('products/', ProductListView.as_view(),),
    
    
    
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('schema/swagger-ui/',
         SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('schema/redoc/',
         SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

]
