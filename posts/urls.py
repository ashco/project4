from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'), # [r = route][^ = start with][$ = End with], checks in views.py file for method called index
    url(r'^details/(?P<id>\d+)/$', views.details, name='details') #
]