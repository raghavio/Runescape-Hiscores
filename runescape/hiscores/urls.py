from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^player/(?P<user_name>.*)/$', views.player),
    url(r'^(?P<skill>[a-zA-Z]+)/$', views.show_skill),
]
