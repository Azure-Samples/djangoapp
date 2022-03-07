from django.urls import path
from . import views

app_name='topics'

urlpatterns = [
    path('', views.topic_view, name='home'),
]