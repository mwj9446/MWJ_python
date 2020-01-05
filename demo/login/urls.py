from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^c*/$', views.index),
    url(r'^login/$', views.login, name='login'),
    url(r'^center/$', views.center)
]
