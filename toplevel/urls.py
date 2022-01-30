from django.urls import path

from . import views

urlpatterns = [
    path('', views.toplevel_view, name='toplevel_view'),
    path('<slug:slug>', views.toplevel_view, name='toplevel_view'),




]