from django.urls import path
from . import views

app_name = 'resources'

urlpatterns = [
    path('<slug:slug>', views.resource_view, name='resource_view'), 
]