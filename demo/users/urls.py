from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^b.*/$', views.index,name='hello'),
    url(r'^c*/', include('login.urls')),
]
