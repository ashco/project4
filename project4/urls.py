from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', include('posts.urls')),
    path('admin/', admin.site.urls),
    url(r'^posts/', include('posts.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



