from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^compare/(?P<player1>[\@\.\w-]+)/(?P<player2>[\@\.\w-]+)/$', views.compare, name='compare'),
    url(r'^player/(?P<user_name>.*)/$', views.player, name='player'),
    url(r'^(?P<skill>[a-zA-Z]+)/$', views.show_skill, name='skill'),
]