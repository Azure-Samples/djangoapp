from django.urls import path

from . import views

urlpatterns = [
    path('', views.toplevel, name='toplevel_view'),
]