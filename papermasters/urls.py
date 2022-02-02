from django.urls import path
from . import views

app_name='papermasters'

urlpatterns = [
    path('', views.index, {'slug':''}, name='home'),
    path('<slug:slug>', views.index, name= 'index'),
]
