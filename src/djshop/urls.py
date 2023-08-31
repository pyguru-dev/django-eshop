from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('apps.pages.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('apps.accounts.urls')),
    path('shop/', include('apps.shop.urls')),
    path('blog/', include('apps.blog.urls')),
    path('api/', include('apps.api.urls')),
    path('payments/', include('apps.payments.urls')),
    path('friendships/', include('apps.friendships.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path("unicorn/", include("django_unicorn.urls")),
    path("__debug__/", include("debug_toolbar.urls")),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
