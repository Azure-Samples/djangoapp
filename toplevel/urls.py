from django.urls import path

from . import views

app_name = 'toplevel'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('toplevel/', views.toplevel_view, name='toplevel_view'),
    path('services/<slug:slug>/', views.services_view, name='services_view'),
    path('resources/<slug:slug>/', views.resources_view, name='resources_view'),
]