from django.urls import path

from . import views

urlpatterns = [
    path('', views.toplevelView, name='toplevelView'),
]