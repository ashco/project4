from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url

urlpatterns = [
    url(r'^$', include('posts.urls')),
    path('admin/', admin.site.urls),
    url(r'^posts/', include('posts.urls')),
]
