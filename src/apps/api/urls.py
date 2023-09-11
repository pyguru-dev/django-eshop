from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView, TokenVerifyView
)
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

from .views import (
    CategoryListView,    
    ProductListView,
    RequestOtpAPIView,
    UserChangePasswordAPIView,
    UserForgotPasswordAPIView,
    UserRegisterView,
    TagViewSet,
    UserLoginView,
    PostViewSet,
    ProductViewSet,
    BlogCategoryViewSet,
    # ProductCategoryViewSet,
    UserLogoutView,
    VerifyOtpAPIView,
)

router = routers.DefaultRouter()
router.register(r'tags', TagViewSet, basename='tag')
router.register(r'posts', PostViewSet, basename='post')
router.register(r'products', ProductViewSet, basename='product')
# router.register(r'banks', ProductViewSet, basename='bank')
# router.register(r'shippings', ProductViewSet, basename='shipping')
# router.register(r'products', ProductViewSet, basename='product')
# router.register(r'categories', CategoryViewSet)


urlpatterns = [
    path('auth/register/', UserRegisterView.as_view()),
    path('auth/token/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('auth/logout/', UserLogoutView.as_view()),
    path('auth/passwords/forgot/', UserForgotPasswordAPIView.as_view()),
    # path('auth/passwords/reset/<uid>/<token>/', UserForgotPasswordAPIView.as_view()),
    path('auth/otp/request/', RequestOtpAPIView.as_view()),
    path('auth/otp/verify/', VerifyOtpAPIView.as_view()),
    
    path('account/password_change', UserChangePasswordAPIView.as_view()),
    
    
        
    path('', include(router.urls)),
    path('categories/', CategoryListView.as_view(),),    
    
    
    
    
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('schema/swagger-ui/',
         SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('schema/redoc/',
         SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

]
