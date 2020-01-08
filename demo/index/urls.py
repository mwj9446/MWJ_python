from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^([a-zA-Z]+)/(\d{4})/$', views.index),
    url(r'^meta/$', views.index3, name='indexxx'),
    url(r'^post/$', views.index4),
    url(r'^non/post/$', views.index5),
    url(r'^$', views.index2),
]
