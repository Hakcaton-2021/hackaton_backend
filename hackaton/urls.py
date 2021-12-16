from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from hackaton.frontend.views import View
from hackaton.apps.forms import urls as form_urls
from hackaton.apps.business import urls as business_urls

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(("hackaton.api.urls", "api"), namespace="api")),
    path("contact/", include(form_urls)),
    path("business/", include(business_urls)),
    path(r'forms', View.forms, name='forms'),
] + static(
    settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
