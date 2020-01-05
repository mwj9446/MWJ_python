from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^([a-zA-Z]+)/(\d{4})/$', views.index)
]
