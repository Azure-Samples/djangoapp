from django.urls import path
from . import views

app_name='topics'

urlpatterns = [
    path('', views.index, {'slug':''}, name='home'),
    path('<str:subject>/<str:subtopic>/<slug:slug>', views.index, name= 'index'),
]