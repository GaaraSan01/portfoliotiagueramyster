from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('myportifolio/', admin.site.urls),
    path('', include('portifolio.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
