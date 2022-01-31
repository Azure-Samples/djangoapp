from django.urls import path
from django.urls import reverse
from . import views

app_name='papermasters'

urlpatterns = [
    path('', views.topic_view, name= 'topic_view'),
    path('<str:subject>/<str:subtopic>/<slug:slug>/', views.topic_view, name= 'topic_view')
    
]