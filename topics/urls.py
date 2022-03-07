from django.urls import path
from . import views

app_name='topics'

urlpatterns = [
    path('', views.home, {'slug':''}, name='home'),
]