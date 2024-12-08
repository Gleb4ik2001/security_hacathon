from django.conf import settings
from django.contrib import admin
from django.urls import (
    path,
    include
)
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include('api.urls'),name='api_urls'),
    path('api/v1/auth/', include('auths.urls')),
    path('', include('frontend.urls')),
    path('api/v1/parsers/', include('parsers.urls')),
]


if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, 
        document_root=settings.MEDIA_ROOT
    )