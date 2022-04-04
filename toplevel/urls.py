from django.urls import path
from . import views

app_name = 'toplevel'

urlpatterns = [
    path('toplevel/', views.toplevel_view, name='toplevel_view'),
    path('<slug:slug>', views.services_view, name='services_view'), 
]