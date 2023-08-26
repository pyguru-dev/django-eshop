from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home_view'),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    # path('accounts/', include('accounts.urls')),
    # path('api-auth/', include('rest_framework.urls')),
    path('blog/', include('apps.blog.urls')),
    path('api/', include('apps.api.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
