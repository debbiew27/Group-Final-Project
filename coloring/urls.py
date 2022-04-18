from django.urls import path
from . import views

urlpatterns = [
  path('coloring/<slug:authorname>/', views.index),
  path('coloring/', views.index),
  path('', views.index),
]
