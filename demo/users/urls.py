from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^i*/$', views.index),
    # url(r'^d*/$', include('my.urls')),
]
