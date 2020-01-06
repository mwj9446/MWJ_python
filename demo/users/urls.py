from django.conf.urls import url, include

from . import views
from .views import decorator

urlpatterns = [
    url(r'^index3/$', decorator(views.ClassView.as_view())),
    # url(r'^c*/', include('login.urls')),
]

