from django.urls import path
from . import views

urlpatterns = [
    path('', views.topic, name= 'topic'),
    path('<int:pk>',  views.topic, name='topic'),

]