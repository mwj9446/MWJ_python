from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^response/$', views.response),
    url(r'^json/$', views.my_json_response),
    url(r'^center/$', views.center),
    url(r'^set_cookie/$', views.set_cookie),
    url(r'^set_session/$', views.set_session, name='session'),
]
