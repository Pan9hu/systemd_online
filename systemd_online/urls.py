from systemd_online import settings
from django.contrib import admin
from django.contrib.staticfiles.views import serve
from django.urls import path, re_path

urlpatterns = [
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns.append(
        re_path('^static/(?P<path>.*)', serve, {
            "document_root": settings.STATIC_ROOT
        })
    )
