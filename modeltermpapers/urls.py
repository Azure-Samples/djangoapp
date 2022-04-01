from django.urls import path
from . import views

app_name = 'modeltermpapers'
urlpatterns = [ 
    path('', views.home, name='home'),
    path('prices/', views.prices, name='prices'),
   
] 