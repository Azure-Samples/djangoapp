from django.urls import path
from . import views

urlpatterns = [
    path('.', views.topic, name= 'topic'),
    
]