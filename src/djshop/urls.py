from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView
from admin_notification.views import check_notification_view
from apps.core.schema import schema
from apps.core.urls import sitemaps
from apps.core.views import error404_handler
from django.conf.urls import handler404

urlpatterns = [
    path('', include('apps.pages.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('apps.accounts.urls')),
    path('shop/', include('apps.shop.urls')),
    path('blog/', include('apps.blog.urls')),
    path('payments/', include('apps.payments.urls')),
    path('friendships/', include('apps.friendships.urls')),
    path('shortener/', include('apps.shortener.urls')),
    path('vendors/', include('apps.vendors.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include('apps.api.urls')),
    path("unicorn/", include("django_unicorn.urls")),
    path("__debug__/", include("debug_toolbar.urls")),
    path("graphql", csrf_exempt(GraphQLView.as_view(graphiql=True, schema=schema))),
    path('check/notification', check_notification_view,
         name="check_notifications"),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]

# if settings.DEBUG:
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = error404_handler
