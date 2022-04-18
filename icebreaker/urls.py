from django.urls import path
from . import views

urlpatterns = [
  path('icebreaker/server', views.server, name='server'),
  path('icebreaker/player', views.player, name='player'),
  path('', views.index, name='index'),
]
