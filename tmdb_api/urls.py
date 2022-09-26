from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from .views import error_404
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("api.urls"))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handler404 = error_404
